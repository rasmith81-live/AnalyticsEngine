
import openai
from typing import List, Dict, Any, Optional
import json
from .config import settings
from .models import BusinessIntent, CompanyValueChainModel, ValueChainNode, ValueChainLink

class LLMClient:
    def __init__(self):
        self.provider = settings.LLM_PROVIDER
        self.model = settings.LLM_MODEL
        
        if self.provider == "azure":
            self.client = openai.AzureOpenAI(
                api_key=settings.AZURE_OPENAI_API_KEY,
                api_version="2023-12-01-preview",
                azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
            )
        else:
            self.client = openai.OpenAI(
                api_key=settings.OPENAI_API_KEY
            )

    async def generate_value_chain(self, context: List[Dict[str, str]]) -> CompanyValueChainModel:
        """
        Generate a Company Value Chain Model from the conversation history.
        """
        system_prompt = """
        You are an expert Enterprise Architect.
        Analyze the conversation history to construct a Company Value Chain Model.
        Identify key Processes, Activities, and Metrics discussed.
        Determine the relationships (links) between them.
        
        Return the result as a JSON object matching this structure:
        {
            "name": "Derived Value Chain",
            "nodes": [
                {
                    "name": "Order Management",
                    "type": "Process",
                    "description": "Handling customer orders",
                    "properties": {"criticality": "High"}
                },
                {
                    "name": "Order Cycle Time",
                    "type": "Metric",
                    "description": "Time from order to delivery"
                }
            ],
            "links": [
                {
                    "source_name": "Order Management",
                    "target_name": "Order Cycle Time",
                    "type": "measures"
                }
            ]
        }
        Note: The 'links' in the JSON should reference node names for convenience, the code will map them to IDs.
        """
        
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # Add full context for model generation
        messages.extend(context)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                response_format={ "type": "json_object" },
                temperature=0.2
            )
            
            content = response.choices[0].message.content
            data = json.loads(content)
            
            # Construct the model
            model = CompanyValueChainModel(name=data.get("name", "Generated Value Chain"))
            
            # Map names to IDs for linking
            name_to_id = {}
            
            for node_data in data.get("nodes", []):
                node = ValueChainNode(
                    name=node_data["name"],
                    type=node_data["type"],
                    description=node_data.get("description"),
                    properties=node_data.get("properties", {})
                )
                model.nodes.append(node)
                name_to_id[node.name] = node.id
            
            for link_data in data.get("links", []):
                source_name = link_data.get("source_name")
                target_name = link_data.get("target_name")
                
                if source_name in name_to_id and target_name in name_to_id:
                    link = ValueChainLink(
                        source_id=name_to_id[source_name],
                        target_id=name_to_id[target_name],
                        type=link_data.get("type", "related_to")
                    )
                    model.links.append(link)
                
            return model
            
        except Exception as e:
            print(f"LLM Error during value chain generation: {e}")
            # Return empty model on error
            return CompanyValueChainModel(name="Error Generating Model")

    async def extract_intents(self, text: str, context: List[Dict[str, str]]) -> List[BusinessIntent]:
        """
        Analyze text to extract business intents using LLM.
        """
        system_prompt = """
        You are an expert Business Analyst. Your goal is to extract structured Business Intents from the user's input.
        Identify what the user wants to measure, analyze, or achieve.
        Return the result as a JSON object containing a list of intents with 'name', 'confidence' (0-1), 'parameters', and 'description'.
        Example JSON structure:
        {
            "intents": [
                {
                    "name": "Analyze Revenue",
                    "confidence": 0.95,
                    "parameters": {"metric": "revenue", "dimension": "region"},
                    "description": "User wants to see revenue breakdown by region"
                }
            ]
        }
        """
        
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # Add recent context (last 5 messages)
        # Assuming context is a list of dicts with 'role' and 'content' or mapped from Utterance
        messages.extend(context[-5:])
        messages.append({"role": "user", "content": text})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                response_format={ "type": "json_object" },
                temperature=0.3
            )
            
            content = response.choices[0].message.content
            data = json.loads(content)
            
            intents = []
            for item in data.get("intents", []):
                intents.append(BusinessIntent(**item))
                
            return intents
            
        except Exception as e:
            print(f"LLM Error during intent extraction: {e}")
            return []

    async def generate_response(self, text: str, context: List[Dict[str, str]], intents: List[BusinessIntent]) -> str:
        """
        Generate a conversational response based on the user's input and identified intents.
        """
        system_prompt = """
        You are a helpful Data Architecture Assistant.
        Based on the user's input and the identified business intents, clarify their requirements or suggest analytics solutions.
        Be concise and professional.
        """
        
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        messages.extend(context[-5:])
        
        # Add intent context
        if intents:
            intent_summary = ", ".join([f"{i.name} ({i.confidence})" for i in intents])
            messages.append({"role": "system", "content": f"Identified Intents: {intent_summary}"})
            
        messages.append({"role": "user", "content": text})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"LLM Error during response generation: {e}")
            return "I apologize, but I'm having trouble processing your request right now."

llm_client = LLMClient()
