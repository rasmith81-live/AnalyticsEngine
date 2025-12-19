import unittest
import asyncio
from unittest.mock import MagicMock, patch, AsyncMock
from fastapi.testclient import TestClient
import json
import sys
import os
from unittest.mock import MagicMock

# Mock openai module before importing app
sys.modules["openai"] = MagicMock()

# Add parent directory to path to allow importing app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main import app
from app.models import BusinessIntent, InterviewSession
from app.llm_client import LLMClient

class TestConversationService(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
        # Mock LLM Client to avoid external calls
        self.llm_patcher = patch('app.main.llm_client')
        self.mock_llm = self.llm_patcher.start()
        
        # Setup default mock responses
        self.mock_llm.extract_intents = AsyncMock(return_value=[
            BusinessIntent(name="Analyze Sales", confidence=0.9, parameters={"metric": "revenue"})
        ])
        self.mock_llm.generate_response = AsyncMock(return_value="I can help you analyze sales revenue.")
        self.mock_llm.generate_value_chain = AsyncMock(return_value=MagicMock(dict=lambda: {"name": "Test VC"}))

    def tearDown(self):
        self.llm_patcher.stop()

    def test_health_check(self):
        """Test service health check"""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "healthy")

    def test_session_management(self):
        """Test session creation and retrieval"""
        # Create Session
        response = self.client.post("/api/v1/sessions?user_id=test_user")
        self.assertEqual(response.status_code, 200)
        session_data = response.json()
        self.assertEqual(session_data["user_id"], "test_user")
        session_id = session_data["id"]

        # Get Session
        response = self.client.get(f"/api/v1/sessions/{session_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["id"], session_id)

    def test_chat_flow(self):
        """Test chat endpoint with mocked LLM"""
        # Create session first
        response = self.client.post("/api/v1/sessions?user_id=chat_user")
        session_id = response.json()["id"]

        # Send message
        payload = {
            "session_id": session_id,
            "user_id": "chat_user",
            "message": "I want to analyze my sales revenue."
        }
        response = self.client.post("/api/v1/chat", json=payload)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "I can help you analyze sales revenue.")
        self.assertEqual(len(data["intents"]), 1)
        self.assertEqual(data["intents"][0]["name"], "Analyze Sales")

    def test_pattern_matching(self):
        """Test intent matching to patterns"""
        intent = {
            "name": "Optimize Inventory",
            "confidence": 0.9,
            "parameters": {},
            "description": "User wants to optimize inventory levels",
            "domain": "supply_chain",
            "target_entities": ["inventory"],
            "requested_metrics": []
        }
        
        response = self.client.post("/api/v1/match-intent", json=intent)
        self.assertEqual(response.status_code, 200)
        matches = response.json()
        self.assertTrue(len(matches) > 0)
        self.assertEqual(matches[0]["pattern_id"], "SCOR_Model")
        
        # Test Design Suggestions
        pattern_id = matches[0]["pattern_id"]
        response = self.client.post(f"/api/v1/suggestions/{pattern_id}/apply")
        self.assertEqual(response.status_code, 200)
        suggestion = response.json()
        self.assertIn("Warehouse", suggestion["entities"])
        
    def test_strategic_recommendation(self):
        """Test Strategic Recommendation Engine"""
        payload = {
            "business_description": "We run a large hospital network focused on patient care.",
            "use_cases": ["improve clinical outcomes", "reduce wait times"]
        }
        
        response = self.client.post("/api/v1/recommend-strategy", json=payload)
        self.assertEqual(response.status_code, 200)
        recommendations = response.json()
        self.assertTrue(len(recommendations) > 0)
        self.assertEqual(recommendations[0]["value_chain_name"], "Standard Model for Healthcare")

if __name__ == '__main__':
    unittest.main()
