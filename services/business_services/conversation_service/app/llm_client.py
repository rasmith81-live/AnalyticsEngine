"""
LLM Client for Conversation Service

This module provides LLM integration using Anthropic Claude as the primary provider.
The multi-agent architecture uses Claude Opus 4.5 for coordination and Claude Sonnet 4
for specialized sub-agents.

Legacy OpenAI support is maintained for backward compatibility but Claude is preferred.
"""

import json
import logging
from typing import List, Dict, Any, Optional

import anthropic
from .config import settings
from .models import BusinessIntent, CompanyValueChainModel, ValueChainNode, ValueChainLink

logger = logging.getLogger(__name__)


class LLMClient:
    """
    LLM Client that uses Anthropic Claude as the primary provider.
    
    This client provides:
    - Intent extraction using Claude
    - Response generation using Claude
    - Value chain generation using Claude
    
    The multi-agent system (agents/) provides more sophisticated capabilities
    and should be preferred for complex design tasks.
    """
    
    def __init__(self):
        self.provider = settings.LLM_PROVIDER
        
        # Use Anthropic Claude as primary
        if settings.ANTHROPIC_API_KEY:
            self.client = anthropic.Anthropic(api_key=settings.ANTHROPIC_API_KEY)
            self.model = settings.ANTHROPIC_SUBAGENT_MODEL or "claude-sonnet-4-20250514"
            self.provider = "anthropic"
            logger.info(f"LLMClient initialized with Anthropic Claude: {self.model}")
        else:
            # Fallback to OpenAI if no Anthropic key (legacy support)
            import openai
            self.model = settings.LLM_MODEL
            if self.provider == "azure":
                self.client = openai.AzureOpenAI(
                    api_key=settings.AZURE_OPENAI_API_KEY,
                    api_version="2023-12-01-preview",
                    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT
                )
            else:
                self.client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
            logger.info(f"LLMClient initialized with OpenAI: {self.model}")

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
        
        # Build conversation content
        conversation_text = "\n".join([
            f"{msg.get('role', 'user')}: {msg.get('content', '')}" 
            for msg in context
        ])

        try:
            if self.provider == "anthropic":
                # Use Anthropic Claude API
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=4096,
                    system=system_prompt,
                    messages=[{"role": "user", "content": f"Conversation history:\n{conversation_text}\n\nPlease analyze and return JSON."}]
                )
                content = response.content[0].text
            else:
                # Legacy OpenAI API
                messages = [{"role": "system", "content": system_prompt}]
                messages.extend(context)
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    response_format={"type": "json_object"},
                    temperature=0.2
                )
                content = response.choices[0].message.content
            
            # Parse JSON from response (handle markdown code blocks)
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
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
        
        For each intent, you MUST extract:
        - name: A short name for the intent
        - confidence: A score from 0-1 indicating how confident you are
        - parameters: Key-value pairs of relevant parameters mentioned
        - description: A brief description of the intent
        - domain: The business domain (e.g., "supply_chain", "finance", "sales", "hr", "operations", "marketing")
        - target_entities: A list of business entities mentioned (e.g., "Customer", "Order", "Product", "Invoice", "Employee", "Supplier", "Inventory")
        - requested_metrics: A list of KPIs or metrics mentioned (e.g., "Revenue", "Order Fulfillment Rate", "Inventory Turnover", "Customer Satisfaction")
        
        Return the result as a JSON object containing a list of intents.
        Example JSON structure:
        {
            "intents": [
                {
                    "name": "Analyze Revenue",
                    "confidence": 0.95,
                    "parameters": {"dimension": "region"},
                    "description": "User wants to see revenue breakdown by region",
                    "domain": "finance",
                    "target_entities": ["Customer", "Order", "Region"],
                    "requested_metrics": ["Revenue", "Sales Volume", "Average Order Value"]
                }
            ]
        }
        
        IMPORTANT: Always populate target_entities and requested_metrics arrays based on what is mentioned or implied in the conversation.
        """
        
        # Build conversation content
        recent_context = context[-5:]
        conversation_text = "\n".join([
            f"{msg.get('role', 'user')}: {msg.get('content', '')}" 
            for msg in recent_context
        ])

        try:
            if self.provider == "anthropic":
                # Use Anthropic Claude API
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=2048,
                    system=system_prompt,
                    messages=[{"role": "user", "content": f"Context:\n{conversation_text}\n\nNew message: {text}\n\nPlease extract intents and return JSON."}]
                )
                content = response.content[0].text
            else:
                # Legacy OpenAI API
                messages = [{"role": "system", "content": system_prompt}]
                messages.extend(recent_context)
                messages.append({"role": "user", "content": text})
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    response_format={"type": "json_object"},
                    temperature=0.3
                )
                content = response.choices[0].message.content
            
            # Parse JSON from response (handle markdown code blocks)
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
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
        
        # Build conversation content
        recent_context = context[-5:]
        conversation_text = "\n".join([
            f"{msg.get('role', 'user')}: {msg.get('content', '')}" 
            for msg in recent_context
        ])
        
        # Add intent context
        intent_summary = ""
        if intents:
            intent_summary = f"\n\nIdentified Intents: " + ", ".join([f"{i.name} ({i.confidence})" for i in intents])

        try:
            if self.provider == "anthropic":
                # Use Anthropic Claude API
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=2048,
                    system=system_prompt,
                    messages=[{"role": "user", "content": f"Context:\n{conversation_text}{intent_summary}\n\nUser message: {text}"}]
                )
                return response.content[0].text
            else:
                # Legacy OpenAI API
                messages = [{"role": "system", "content": system_prompt}]
                messages.extend(recent_context)
                if intents:
                    messages.append({"role": "system", "content": f"Identified Intents: {', '.join([f'{i.name} ({i.confidence})' for i in intents])}"})
                messages.append({"role": "user", "content": text})
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    temperature=0.7
                )
                return response.choices[0].message.content
        except Exception as e:
            logger.error(f"LLM Error during response generation: {e}")
            return "I apologize, but I'm having trouble processing your request right now."


# Lazy initialization to avoid import-time API calls
_llm_client: Optional[LLMClient] = None


def get_llm_client() -> LLMClient:
    """Get or create the LLM client instance."""
    global _llm_client
    if _llm_client is None:
        _llm_client = LLMClient()
    return _llm_client


class _LLMClientProxy:
    """Proxy class for lazy initialization of LLMClient."""
    
    def __getattr__(self, name):
        return getattr(get_llm_client(), name)


# For backward compatibility - lazy initialization
llm_client = _LLMClientProxy()
