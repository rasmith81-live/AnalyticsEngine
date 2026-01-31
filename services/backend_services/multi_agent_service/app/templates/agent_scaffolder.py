# =============================================================================
# Agent Scaffolder - Create Agents from Templates
# Phase 19: Prompt Library Integration
# Reference: https://www.shawnewallace.com/2026-01-12-introducing-prompt-library-cli/
# =============================================================================
"""
Agent scaffolder for creating new agents from templates.

Provides:
- Template-based agent creation
- Customization options
- Validation of required fields
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
import logging
import re

from .prompt_library import PromptLibrary, PromptTemplate, get_prompt_library

logger = logging.getLogger(__name__)


@dataclass
class AgentTemplateConfig:
    """
    Configuration for scaffolding a new agent.
    
    Attributes:
        template_name: Name of the template to use (e.g., 'specialist_agent')
        agent_role: Role identifier for the new agent
        display_name: Human-readable name
        description: Agent description
        domain_keywords: Keywords for fuzzy discovery
        tools: List of tool names the agent can use
        capabilities: List of capability descriptions
        scenario: Optional scenario this agent belongs to
        fragments: List of fragment names to include
        custom_variables: Additional template variables
    """
    template_name: str
    agent_role: str
    display_name: str = ""
    description: str = ""
    domain_keywords: List[str] = field(default_factory=list)
    tools: List[str] = field(default_factory=list)
    capabilities: List[str] = field(default_factory=list)
    scenario: Optional[str] = None
    fragments: List[str] = field(default_factory=list)
    custom_variables: Dict[str, str] = field(default_factory=dict)
    
    def __post_init__(self):
        if not self.display_name:
            self.display_name = self.agent_role.replace("_", " ").title()


@dataclass
class ScaffoldedAgent:
    """
    Result of scaffolding an agent from a template.
    
    Attributes:
        config: The configuration used to scaffold
        system_prompt: Generated system prompt
        created_at: Timestamp of creation
        template_version: Version of template used
        content_hash: Hash of generated content
    """
    config: AgentTemplateConfig
    system_prompt: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    template_version: str = "1.0.0"
    content_hash: str = ""
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "agent_role": self.config.agent_role,
            "display_name": self.config.display_name,
            "description": self.config.description,
            "domain_keywords": self.config.domain_keywords,
            "tools": self.config.tools,
            "capabilities": self.config.capabilities,
            "scenario": self.config.scenario,
            "system_prompt": self.system_prompt,
            "template_name": self.config.template_name,
            "template_version": self.template_version,
            "created_at": self.created_at.isoformat(),
            "content_hash": self.content_hash,
        }


class AgentScaffolder:
    """
    Scaffolds new agents from templates.
    
    Usage:
        scaffolder = AgentScaffolder()
        config = AgentTemplateConfig(
            template_name="specialist_agent",
            agent_role="inventory_analyst",
            domain_keywords=["inventory", "stock", "warehouse"],
            tools=["analyze_inventory", "check_stock_levels"]
        )
        agent = scaffolder.scaffold(config)
    """
    
    def __init__(self, library: Optional[PromptLibrary] = None):
        self._library = library or get_prompt_library()
        self._scaffolded_agents: Dict[str, ScaffoldedAgent] = {}
    
    def scaffold(self, config: AgentTemplateConfig) -> ScaffoldedAgent:
        """
        Scaffold a new agent from a template.
        
        Args:
            config: Agent template configuration
            
        Returns:
            ScaffoldedAgent with generated system prompt
            
        Raises:
            ValueError: If template not found or required variables missing
        """
        template = self._library.get_template(config.template_name)
        if not template:
            available = self._library.list_templates()
            raise ValueError(
                f"Template '{config.template_name}' not found. "
                f"Available templates: {available}"
            )
        
        variables = self._build_variables(config, template)
        missing = self._check_required_variables(template, variables)
        if missing:
            raise ValueError(f"Missing required variables: {missing}")
        
        system_prompt = self._compose_prompt(template, variables, config.fragments)
        
        import hashlib
        content_hash = hashlib.sha256(system_prompt.encode()).hexdigest()[:16]
        
        scaffolded = ScaffoldedAgent(
            config=config,
            system_prompt=system_prompt,
            template_version=template.version,
            content_hash=content_hash
        )
        
        self._scaffolded_agents[config.agent_role] = scaffolded
        logger.info(f"Scaffolded agent: {config.agent_role} from template: {config.template_name}")
        
        return scaffolded
    
    def _build_variables(
        self,
        config: AgentTemplateConfig,
        template: PromptTemplate
    ) -> Dict[str, str]:
        """Build variable dictionary from config."""
        variables = {
            "agent_role": config.display_name,
        }
        
        if config.description:
            variables["domain_expertise"] = config.description
            variables["responsibilities"] = config.description
        
        if config.tools:
            tools_desc = "\n".join(f"- {tool}" for tool in config.tools)
            variables["tools_description"] = tools_desc
        
        if config.domain_keywords:
            keywords = ", ".join(config.domain_keywords)
            variables["domain_keywords"] = keywords
        
        if config.capabilities:
            caps_desc = "\n".join(f"- {cap}" for cap in config.capabilities)
            variables["responsibilities"] = caps_desc
        
        variables["additional_context"] = ""
        variables["additional_instructions"] = ""
        
        variables.update(config.custom_variables)
        
        return variables
    
    def _check_required_variables(
        self,
        template: PromptTemplate,
        variables: Dict[str, str]
    ) -> List[str]:
        """Check for missing required variables."""
        pattern = r'\{(\w+)\}'
        required = set(re.findall(pattern, template.content))
        
        optional = {"additional_context", "additional_instructions"}
        required_only = required - optional
        
        provided = set(variables.keys())
        missing = required_only - provided
        
        return list(missing)
    
    def _compose_prompt(
        self,
        template: PromptTemplate,
        variables: Dict[str, str],
        fragments: List[str]
    ) -> str:
        """Compose the final system prompt."""
        prompt = template.content
        for var_name, var_value in variables.items():
            placeholder = "{" + var_name + "}"
            prompt = prompt.replace(placeholder, var_value)
        
        if fragments:
            fragment_content = []
            for frag_name in fragments:
                fragment = self._library.get_fragment(frag_name)
                if fragment:
                    title = fragment.name.replace("_", " ").title()
                    fragment_content.append(f"\n## {title}\n{fragment.content}")
                else:
                    shared = self._library.get_shared_prompt(frag_name)
                    if shared:
                        title = shared.name.replace("_", " ").title()
                        fragment_content.append(f"\n## {title}\n{shared.content}")
            
            if fragment_content:
                prompt += "\n" + "\n".join(fragment_content)
        
        return prompt
    
    def get_scaffolded(self, agent_role: str) -> Optional[ScaffoldedAgent]:
        """Get a previously scaffolded agent."""
        return self._scaffolded_agents.get(agent_role)
    
    def list_scaffolded(self) -> List[str]:
        """List all scaffolded agent roles."""
        return list(self._scaffolded_agents.keys())
    
    def preview_scaffold(self, config: AgentTemplateConfig) -> Dict[str, Any]:
        """
        Preview what scaffolding would produce without creating.
        
        This is a dry-run mode that shows the expected output.
        """
        template = self._library.get_template(config.template_name)
        if not template:
            return {
                "success": False,
                "error": f"Template '{config.template_name}' not found",
                "available_templates": self._library.list_templates()
            }
        
        variables = self._build_variables(config, template)
        missing = self._check_required_variables(template, variables)
        
        if missing:
            return {
                "success": False,
                "error": f"Missing required variables: {missing}",
                "variables_provided": list(variables.keys()),
                "variables_required": list(set(re.findall(r'\{(\w+)\}', template.content)))
            }
        
        system_prompt = self._compose_prompt(template, variables, config.fragments)
        
        return {
            "success": True,
            "preview": {
                "agent_role": config.agent_role,
                "display_name": config.display_name,
                "template_name": config.template_name,
                "template_version": template.version,
                "system_prompt_preview": system_prompt[:500] + "..." if len(system_prompt) > 500 else system_prompt,
                "system_prompt_length": len(system_prompt),
                "fragments_included": config.fragments,
                "domain_keywords": config.domain_keywords,
                "tools": config.tools,
            }
        }


_scaffolder_instance: Optional[AgentScaffolder] = None


def get_agent_scaffolder() -> AgentScaffolder:
    """Get the singleton agent scaffolder instance."""
    global _scaffolder_instance
    if _scaffolder_instance is None:
        _scaffolder_instance = AgentScaffolder()
    return _scaffolder_instance
