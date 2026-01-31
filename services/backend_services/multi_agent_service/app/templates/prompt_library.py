# =============================================================================
# Prompt Library - Centralized Prompt Template Management
# Phase 19: Prompt Library Integration
# Reference: https://www.shawnewallace.com/2025-11-19-building-a-personal-prompt-library/
# =============================================================================
"""
Prompt library for managing agent system prompts organized by scenario.

Provides:
- Scenario-based prompt organization
- Template versioning and metadata
- Prompt composition from fragments
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Set
import hashlib
import logging

logger = logging.getLogger(__name__)


class PromptCategory(str, Enum):
    """Categories for organizing prompts."""
    SCENARIO = "scenario"
    SHARED = "shared"
    TEMPLATE = "template"
    FRAGMENT = "fragment"


@dataclass
class PromptTemplate:
    """
    A versioned prompt template.
    
    Attributes:
        name: Unique identifier for the template
        content: The prompt text content
        category: Category (scenario, shared, template, fragment)
        scenario: Optional scenario name (e.g., 'supply_chain')
        version: Semantic version string
        description: Human-readable description
        tags: Keywords for discovery
        fragments: List of fragment names to compose
        metadata: Additional metadata
    """
    name: str
    content: str
    category: PromptCategory = PromptCategory.TEMPLATE
    scenario: Optional[str] = None
    version: str = "1.0.0"
    description: str = ""
    tags: List[str] = field(default_factory=list)
    fragments: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    
    @property
    def content_hash(self) -> str:
        """Generate hash of content for change detection."""
        return hashlib.sha256(self.content.encode()).hexdigest()[:16]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "name": self.name,
            "content": self.content,
            "category": self.category.value,
            "scenario": self.scenario,
            "version": self.version,
            "description": self.description,
            "tags": self.tags,
            "fragments": self.fragments,
            "metadata": self.metadata,
            "content_hash": self.content_hash,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


@dataclass
class PromptScenario:
    """
    A collection of prompts for a specific development scenario.
    
    Attributes:
        name: Scenario identifier (e.g., 'supply_chain')
        description: Human-readable description
        prompts: Dictionary of prompt templates in this scenario
        shared_fragments: List of shared fragment names to include
    """
    name: str
    description: str = ""
    prompts: Dict[str, PromptTemplate] = field(default_factory=dict)
    shared_fragments: List[str] = field(default_factory=list)
    
    def add_prompt(self, prompt: PromptTemplate) -> None:
        """Add a prompt to this scenario."""
        prompt.scenario = self.name
        prompt.category = PromptCategory.SCENARIO
        self.prompts[prompt.name] = prompt
    
    def get_prompt(self, name: str) -> Optional[PromptTemplate]:
        """Get a prompt by name."""
        return self.prompts.get(name)
    
    def list_prompts(self) -> List[str]:
        """List all prompt names in this scenario."""
        return list(self.prompts.keys())


class PromptLibrary:
    """
    Centralized library for managing prompt templates.
    
    Organizes prompts by:
    - Scenarios (domain-specific collections)
    - Shared resources (cross-scenario reusable prompts)
    - Templates (base templates for scaffolding)
    - Fragments (composable prompt pieces)
    """
    
    def __init__(self):
        self._scenarios: Dict[str, PromptScenario] = {}
        self._shared: Dict[str, PromptTemplate] = {}
        self._templates: Dict[str, PromptTemplate] = {}
        self._fragments: Dict[str, PromptTemplate] = {}
        self._tag_index: Dict[str, Set[str]] = {}
        
        self._initialize_default_content()
    
    def _initialize_default_content(self) -> None:
        """Initialize library with default scenarios and templates."""
        self._init_scenarios()
        self._init_shared_prompts()
        self._init_base_templates()
    
    def _init_scenarios(self) -> None:
        """Initialize default scenarios."""
        scenarios = [
            PromptScenario(
                name="supply_chain",
                description="Supply chain analytics and operations",
                shared_fragments=["collaboration", "contract_rules"]
            ),
            PromptScenario(
                name="retail_analytics",
                description="Retail sales and inventory analytics",
                shared_fragments=["collaboration", "contract_rules"]
            ),
            PromptScenario(
                name="financial_services",
                description="Financial analysis and accounting",
                shared_fragments=["collaboration", "contract_rules"]
            ),
            PromptScenario(
                name="software_development",
                description="Software development and architecture",
                shared_fragments=["collaboration", "contract_rules", "code_review"]
            ),
        ]
        
        for scenario in scenarios:
            self._scenarios[scenario.name] = scenario
    
    def _init_shared_prompts(self) -> None:
        """Initialize shared prompts available across scenarios."""
        shared = [
            PromptTemplate(
                name="code_review",
                content="""When reviewing code:
- Check for correctness, readability, and maintainability
- Identify potential bugs or security issues
- Suggest improvements following best practices
- Consider performance implications
- Verify proper error handling""",
                category=PromptCategory.SHARED,
                description="Code review guidelines",
                tags=["review", "quality", "development"]
            ),
            PromptTemplate(
                name="debugging",
                content="""When debugging issues:
- Reproduce the problem consistently
- Isolate the root cause, not symptoms
- Add logging to trace execution flow
- Check recent changes that may have introduced the bug
- Write a test case that fails before the fix""",
                category=PromptCategory.SHARED,
                description="Debugging best practices",
                tags=["debug", "troubleshooting", "development"]
            ),
            PromptTemplate(
                name="documentation",
                content="""When writing documentation:
- Start with a clear summary of purpose
- Include usage examples
- Document parameters and return values
- Note any prerequisites or dependencies
- Keep documentation close to the code""",
                category=PromptCategory.SHARED,
                description="Documentation guidelines",
                tags=["docs", "documentation", "writing"]
            ),
        ]
        
        for prompt in shared:
            self._shared[prompt.name] = prompt
            self._index_tags(prompt)
    
    def _init_base_templates(self) -> None:
        """Initialize base agent templates for scaffolding."""
        templates = [
            PromptTemplate(
                name="base_agent",
                content="""You are a specialized AI agent with the role of {agent_role}.

Your primary responsibilities:
{responsibilities}

When working on tasks:
- Focus on your area of expertise
- Collaborate with peer agents when needed
- Follow contract enforcement rules
- Signal struggles early rather than making assumptions

{additional_context}""",
                category=PromptCategory.TEMPLATE,
                description="Base template for all agents",
                tags=["base", "template", "agent"],
                metadata={"variables": ["agent_role", "responsibilities", "additional_context"]}
            ),
            PromptTemplate(
                name="specialist_agent",
                content="""You are {agent_role}, a domain specialist agent.

## Expertise
{domain_expertise}

## Tools Available
{tools_description}

## Collaboration Guidelines
- Consult peers via the blackboard for cross-domain questions
- Submit artifacts for peer review before finalizing
- Use contract adapter to track state transitions

## Domain Keywords
{domain_keywords}

{additional_instructions}""",
                category=PromptCategory.TEMPLATE,
                description="Template for specialist domain agents",
                tags=["specialist", "template", "domain"],
                metadata={"variables": ["agent_role", "domain_expertise", "tools_description", 
                                       "domain_keywords", "additional_instructions"]}
            ),
            PromptTemplate(
                name="coordinator_agent",
                content="""You are {agent_role}, a coordination agent responsible for orchestrating work.

## Coordination Responsibilities
- Delegate tasks to appropriate specialist agents
- Monitor task progress and handle blockers
- Aggregate results from multiple agents
- Ensure contract compliance across delegations

## Available Agents
{available_agents}

## Delegation Strategy
{delegation_strategy}

## Escalation Rules
- Escalate to human if agents struggle repeatedly
- Hard stop on contract violations
- Request approval for high-impact decisions

{additional_instructions}""",
                category=PromptCategory.TEMPLATE,
                description="Template for coordinator agents",
                tags=["coordinator", "template", "orchestration"],
                metadata={"variables": ["agent_role", "available_agents", "delegation_strategy",
                                       "additional_instructions"]}
            ),
        ]
        
        for template in templates:
            self._templates[template.name] = template
            self._index_tags(template)
    
    def _index_tags(self, prompt: PromptTemplate) -> None:
        """Index prompt by its tags for discovery."""
        for tag in prompt.tags:
            if tag not in self._tag_index:
                self._tag_index[tag] = set()
            self._tag_index[tag].add(prompt.name)
    
    def add_scenario(self, scenario: PromptScenario) -> None:
        """Add a new scenario to the library."""
        self._scenarios[scenario.name] = scenario
        logger.info(f"Added scenario: {scenario.name}")
    
    def get_scenario(self, name: str) -> Optional[PromptScenario]:
        """Get a scenario by name."""
        return self._scenarios.get(name)
    
    def list_scenarios(self) -> List[str]:
        """List all available scenarios."""
        return list(self._scenarios.keys())
    
    def add_shared_prompt(self, prompt: PromptTemplate) -> None:
        """Add a shared prompt to the library."""
        prompt.category = PromptCategory.SHARED
        self._shared[prompt.name] = prompt
        self._index_tags(prompt)
        logger.info(f"Added shared prompt: {prompt.name}")
    
    def get_shared_prompt(self, name: str) -> Optional[PromptTemplate]:
        """Get a shared prompt by name."""
        return self._shared.get(name)
    
    def list_shared_prompts(self) -> List[str]:
        """List all shared prompts."""
        return list(self._shared.keys())
    
    def add_template(self, template: PromptTemplate) -> None:
        """Add a base template to the library."""
        template.category = PromptCategory.TEMPLATE
        self._templates[template.name] = template
        self._index_tags(template)
        logger.info(f"Added template: {template.name}")
    
    def get_template(self, name: str) -> Optional[PromptTemplate]:
        """Get a template by name."""
        return self._templates.get(name)
    
    def list_templates(self) -> List[str]:
        """List all available templates."""
        return list(self._templates.keys())
    
    def add_fragment(self, fragment: PromptTemplate) -> None:
        """Add a prompt fragment to the library."""
        fragment.category = PromptCategory.FRAGMENT
        self._fragments[fragment.name] = fragment
        self._index_tags(fragment)
        logger.info(f"Added fragment: {fragment.name}")
    
    def get_fragment(self, name: str) -> Optional[PromptTemplate]:
        """Get a fragment by name."""
        return self._fragments.get(name)
    
    def list_fragments(self) -> List[str]:
        """List all available fragments."""
        return list(self._fragments.keys())
    
    def search_by_tag(self, tag: str) -> List[str]:
        """Find prompts by tag."""
        return list(self._tag_index.get(tag.lower(), set()))
    
    def search_by_tags(self, tags: List[str]) -> List[str]:
        """Find prompts matching all specified tags."""
        if not tags:
            return []
        
        result_sets = [self._tag_index.get(tag.lower(), set()) for tag in tags]
        intersection = set.intersection(*result_sets) if result_sets else set()
        return list(intersection)
    
    def get_all_prompts(self) -> Dict[str, List[Dict[str, Any]]]:
        """Get all prompts organized by category."""
        return {
            "scenarios": [
                {
                    "name": s.name,
                    "description": s.description,
                    "prompts": [p.to_dict() for p in s.prompts.values()]
                }
                for s in self._scenarios.values()
            ],
            "shared": [p.to_dict() for p in self._shared.values()],
            "templates": [p.to_dict() for p in self._templates.values()],
            "fragments": [p.to_dict() for p in self._fragments.values()],
        }
    
    def compose_prompt(
        self,
        template_name: str,
        variables: Dict[str, str],
        include_fragments: Optional[List[str]] = None
    ) -> str:
        """
        Compose a prompt from a template with variable substitution.
        
        Args:
            template_name: Name of the template to use
            variables: Dictionary of variable names to values
            include_fragments: Optional list of fragment names to append
            
        Returns:
            Composed prompt string
        """
        template = self.get_template(template_name)
        if not template:
            raise ValueError(f"Template not found: {template_name}")
        
        composed = template.content
        for var_name, var_value in variables.items():
            placeholder = "{" + var_name + "}"
            composed = composed.replace(placeholder, var_value)
        
        if include_fragments:
            fragment_content = []
            for frag_name in include_fragments:
                fragment = self.get_fragment(frag_name)
                if fragment:
                    fragment_content.append(f"\n## {fragment.name.replace('_', ' ').title()}\n{fragment.content}")
            
            if fragment_content:
                composed += "\n" + "\n".join(fragment_content)
        
        return composed


_library_instance: Optional[PromptLibrary] = None


def get_prompt_library() -> PromptLibrary:
    """Get the singleton prompt library instance."""
    global _library_instance
    if _library_instance is None:
        _library_instance = PromptLibrary()
    return _library_instance
