from typing import List, Dict
from pydantic import BaseModel
import json
from .llm_client import LLMClient

class BusinessIntent(BaseModel):
    action: str  # e.g., "monitor", "optimize", "predict"
    domain: str  # e.g., "supply_chain", "sales", "finance"
    target_entities: List[str]
    requested_metrics: List[str]
    time_horizon: str  # "real_time", "historical", "forecast"

class IntentExtractor:
    """
    Parses natural language utterances into structured Business Intents using LLM.
    """
    
    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client
        
    async def extract_intent(self, user_utterance: str, context: List[str] = []) -> BusinessIntent:
        system_prompt = """
        You are a Business Analyst AI. Extract the structured business intent from the user's request.
        Identify the Action, Domain (Sales, Supply Chain, etc.), Entities, Metrics, and Time Horizon.
        Return JSON.
        """
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context: {context}\nRequest: {user_utterance}"}
        ]
        
        response_str = await self.llm.get_completion(messages, json_mode=True)
        
        try:
            data = json.loads(response_str)
            return BusinessIntent(**data)
        except Exception as e:
            print(f"Parsing Error: {e}")
            # Fallback
            return BusinessIntent(
                action="analyze", 
                domain="general", 
                target_entities=[], 
                requested_metrics=[], 
                time_horizon="historical"
            )
