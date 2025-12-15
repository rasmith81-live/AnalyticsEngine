import sys
import os
import unittest
from typing import Dict, Any, List

# Add the directory ABOVE business_metadata to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import models as package
from business_metadata.ontology_models import (
    InterviewSessionDefinition,
    UtteranceDefinition,
    BusinessIntentDefinition,
    CompanyValueChainModelDefinition
)

class TestConversationModeling(unittest.TestCase):
    def test_conversation_models(self):
        """Test Conversation Modeling models."""
        print("\nTesting Conversation Modeling Models...")
        
        # 1. Interview Session
        session = InterviewSessionDefinition(
            kind="interview_session_definition",
            id="sess_123",
            name="Session 123",
            company_id="comp_acme",
            participants=["user_bob", "bot_cascade"],
            started_at="2025-01-01T10:00:00Z"
        )
        self.assertEqual(session.id, "sess_123")
        print("✅ InterviewSessionDefinition created")
        
        # 2. Utterance
        utterance = UtteranceDefinition(
            kind="utterance_definition",
            id="utt_1",
            name="Utterance 1",
            session_id="sess_123",
            speaker="user_bob",
            raw_text="I want to optimize my supply chain.",
            nlp_annotations={"intent": "optimize_supply_chain"}
        )
        self.assertEqual(utterance.raw_text, "I want to optimize my supply chain.")
        print("✅ UtteranceDefinition created")
        
        # 3. Business Intent
        intent = BusinessIntentDefinition(
            kind="business_intent_definition",
            id="intent_1",
            name="Optimize Supply Chain",
            session_id="sess_123",
            intent_type="goal_definition",
            target_concepts=["supply_chain"]
        )
        self.assertEqual(intent.name, "Optimize Supply Chain")
        print("✅ BusinessIntentDefinition created")
        
        # 4. Derived Value Chain Model
        model = CompanyValueChainModelDefinition(
            kind="company_value_chain_model_definition",
            id="model_v1",
            name="Acme Supply Chain Model",
            company_id="comp_acme",
            session_id="sess_123",
            derived_from="conversation",
            included_nodes=["node_supplier", "node_warehouse"],
            applied_patterns=["pat_supply_chain_optimization"]
        )
        self.assertEqual(model.derived_from, "conversation")
        print("✅ CompanyValueChainModelDefinition created")

if __name__ == "__main__":
    unittest.main()
