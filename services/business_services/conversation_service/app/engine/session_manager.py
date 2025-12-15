from typing import Dict, List, Any
import uuid
from datetime import datetime

class SessionManager:
    """Manages conversational sessions."""
    
    def __init__(self):
        self.sessions: Dict[str, Dict[str, Any]] = {}

    def create_session(self, user_id: str) -> str:
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            "user_id": user_id,
            "created_at": datetime.utcnow(),
            "history": [],
            "context": {}
        }
        return session_id

    def add_utterance(self, session_id: str, role: str, content: str):
        if session_id in self.sessions:
            self.sessions[session_id]["history"].append({
                "role": role,
                "content": content,
                "timestamp": datetime.utcnow()
            })

    def get_history(self, session_id: str) -> List[Dict[str, Any]]:
        return self.sessions.get(session_id, {}).get("history", [])
