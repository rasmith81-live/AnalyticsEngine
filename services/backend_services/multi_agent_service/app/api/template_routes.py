# =============================================================================
# Template API Routes
# Phase 19: Prompt Library Integration
# Reference: https://www.shawnewallace.com/2026-01-12-introducing-prompt-library-cli/
# =============================================================================
"""
API routes for prompt library and agent template management.

Provides:
- Template listing and retrieval
- Agent scaffolding from templates
- Prompt fragment management
- Fuzzy agent discovery
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
import logging

from ..templates import (
    PromptLibrary,
    PromptTemplate,
    AgentScaffolder,
    AgentTemplateConfig,
    PromptFragments,
    FragmentComposer,
)
from ..templates.prompt_library import get_prompt_library
from ..templates.agent_scaffolder import get_agent_scaffolder

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/templates", tags=["templates"])


class ScaffoldRequest(BaseModel):
    """Request to scaffold a new agent from a template."""
    template_name: str = Field(..., description="Name of the template to use")
    agent_role: str = Field(..., description="Role identifier for the new agent")
    display_name: Optional[str] = Field(None, description="Human-readable name")
    description: Optional[str] = Field(None, description="Agent description")
    domain_keywords: List[str] = Field(default_factory=list, description="Keywords for discovery")
    tools: List[str] = Field(default_factory=list, description="Tool names the agent can use")
    capabilities: List[str] = Field(default_factory=list, description="Capability descriptions")
    scenario: Optional[str] = Field(None, description="Scenario this agent belongs to")
    fragments: List[str] = Field(default_factory=list, description="Fragment names to include")
    custom_variables: Dict[str, str] = Field(default_factory=dict, description="Additional variables")
    dry_run: bool = Field(False, description="Preview without creating")


class ScaffoldResponse(BaseModel):
    """Response from scaffolding an agent."""
    success: bool
    agent_role: Optional[str] = None
    display_name: Optional[str] = None
    system_prompt: Optional[str] = None
    template_version: Optional[str] = None
    content_hash: Optional[str] = None
    preview: Optional[Dict[str, Any]] = None
    error: Optional[str] = None


class ComposeRequest(BaseModel):
    """Request to compose a prompt from template and fragments."""
    template_name: str = Field(..., description="Template to compose from")
    variables: Dict[str, str] = Field(default_factory=dict, description="Variable substitutions")
    fragments: List[str] = Field(default_factory=list, description="Fragments to include")


class ComposeResponse(BaseModel):
    """Response from composing a prompt."""
    success: bool
    composed_prompt: Optional[str] = None
    template_version: Optional[str] = None
    fragments_included: List[str] = []
    error: Optional[str] = None


@router.get("/scenarios")
async def list_scenarios() -> Dict[str, Any]:
    """List all available scenarios."""
    library = get_prompt_library()
    scenarios = library.list_scenarios()
    
    return {
        "scenarios": [
            {
                "name": name,
                "description": library.get_scenario(name).description if library.get_scenario(name) else ""
            }
            for name in scenarios
        ],
        "count": len(scenarios)
    }


@router.get("/scenarios/{scenario_name}")
async def get_scenario(scenario_name: str) -> Dict[str, Any]:
    """Get details of a specific scenario."""
    library = get_prompt_library()
    scenario = library.get_scenario(scenario_name)
    
    if not scenario:
        raise HTTPException(status_code=404, detail=f"Scenario not found: {scenario_name}")
    
    return {
        "name": scenario.name,
        "description": scenario.description,
        "prompts": scenario.list_prompts(),
        "shared_fragments": scenario.shared_fragments
    }


@router.get("/list")
async def list_templates() -> Dict[str, Any]:
    """List all available templates."""
    library = get_prompt_library()
    
    return {
        "templates": [
            {
                "name": name,
                "description": library.get_template(name).description if library.get_template(name) else "",
                "version": library.get_template(name).version if library.get_template(name) else "1.0.0"
            }
            for name in library.list_templates()
        ],
        "count": len(library.list_templates())
    }


@router.get("/template/{template_name}")
async def get_template(template_name: str) -> Dict[str, Any]:
    """Get details of a specific template."""
    library = get_prompt_library()
    template = library.get_template(template_name)
    
    if not template:
        raise HTTPException(status_code=404, detail=f"Template not found: {template_name}")
    
    return template.to_dict()


@router.get("/fragments")
async def list_fragments() -> Dict[str, Any]:
    """List all available prompt fragments."""
    fragments = PromptFragments.get_all()
    
    return {
        "fragments": [
            {
                "name": f.name,
                "description": f.description,
                "tags": f.tags,
                "content_length": len(f.content)
            }
            for f in fragments.values()
        ],
        "count": len(fragments)
    }


@router.get("/fragments/{fragment_name}")
async def get_fragment(fragment_name: str) -> Dict[str, Any]:
    """Get a specific fragment."""
    fragment = PromptFragments.get(fragment_name)
    
    if not fragment:
        raise HTTPException(status_code=404, detail=f"Fragment not found: {fragment_name}")
    
    return {
        "name": fragment.name,
        "description": fragment.description,
        "content": fragment.content,
        "tags": fragment.tags
    }


@router.get("/fragments/search/{tag}")
async def search_fragments_by_tag(tag: str) -> Dict[str, Any]:
    """Search fragments by tag."""
    fragments = PromptFragments.search_by_tag(tag)
    
    return {
        "tag": tag,
        "fragments": [
            {
                "name": f.name,
                "description": f.description,
                "tags": f.tags
            }
            for f in fragments
        ],
        "count": len(fragments)
    }


@router.get("/shared")
async def list_shared_prompts() -> Dict[str, Any]:
    """List all shared prompts."""
    library = get_prompt_library()
    
    return {
        "shared_prompts": [
            {
                "name": name,
                "description": library.get_shared_prompt(name).description if library.get_shared_prompt(name) else "",
                "tags": library.get_shared_prompt(name).tags if library.get_shared_prompt(name) else []
            }
            for name in library.list_shared_prompts()
        ],
        "count": len(library.list_shared_prompts())
    }


@router.get("/shared/{prompt_name}")
async def get_shared_prompt(prompt_name: str) -> Dict[str, Any]:
    """Get a specific shared prompt."""
    library = get_prompt_library()
    prompt = library.get_shared_prompt(prompt_name)
    
    if not prompt:
        raise HTTPException(status_code=404, detail=f"Shared prompt not found: {prompt_name}")
    
    return prompt.to_dict()


@router.post("/scaffold", response_model=ScaffoldResponse)
async def scaffold_agent(request: ScaffoldRequest) -> ScaffoldResponse:
    """
    Scaffold a new agent from a template.
    
    Use dry_run=true to preview without creating.
    """
    scaffolder = get_agent_scaffolder()
    
    config = AgentTemplateConfig(
        template_name=request.template_name,
        agent_role=request.agent_role,
        display_name=request.display_name or "",
        description=request.description or "",
        domain_keywords=request.domain_keywords,
        tools=request.tools,
        capabilities=request.capabilities,
        scenario=request.scenario,
        fragments=request.fragments,
        custom_variables=request.custom_variables
    )
    
    try:
        if request.dry_run:
            preview = scaffolder.preview_scaffold(config)
            return ScaffoldResponse(
                success=preview.get("success", False),
                preview=preview,
                error=preview.get("error")
            )
        
        scaffolded = scaffolder.scaffold(config)
        
        logger.info(f"Scaffolded agent: {scaffolded.config.agent_role}")
        
        return ScaffoldResponse(
            success=True,
            agent_role=scaffolded.config.agent_role,
            display_name=scaffolded.config.display_name,
            system_prompt=scaffolded.system_prompt,
            template_version=scaffolded.template_version,
            content_hash=scaffolded.content_hash
        )
        
    except ValueError as e:
        logger.warning(f"Scaffold error: {e}")
        return ScaffoldResponse(success=False, error=str(e))
    except Exception as e:
        logger.error(f"Unexpected scaffold error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/compose", response_model=ComposeResponse)
async def compose_prompt(request: ComposeRequest) -> ComposeResponse:
    """Compose a prompt from a template with variable substitution."""
    library = get_prompt_library()
    
    try:
        composed = library.compose_prompt(
            template_name=request.template_name,
            variables=request.variables,
            include_fragments=request.fragments
        )
        
        template = library.get_template(request.template_name)
        
        return ComposeResponse(
            success=True,
            composed_prompt=composed,
            template_version=template.version if template else "1.0.0",
            fragments_included=request.fragments
        )
        
    except ValueError as e:
        return ComposeResponse(success=False, error=str(e))
    except Exception as e:
        logger.error(f"Compose error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/search")
async def search_prompts(
    query: str = Query(..., description="Search query"),
    category: Optional[str] = Query(None, description="Filter by category")
) -> Dict[str, Any]:
    """Search prompts by tag or keyword."""
    library = get_prompt_library()
    
    results = library.search_by_tag(query)
    
    all_prompts = library.get_all_prompts()
    keyword_matches = []
    
    query_lower = query.lower()
    for template in all_prompts.get("templates", []):
        if query_lower in template.get("name", "").lower():
            keyword_matches.append({"type": "template", "name": template["name"]})
        elif query_lower in template.get("description", "").lower():
            keyword_matches.append({"type": "template", "name": template["name"]})
    
    for shared in all_prompts.get("shared", []):
        if query_lower in shared.get("name", "").lower():
            keyword_matches.append({"type": "shared", "name": shared["name"]})
    
    return {
        "query": query,
        "tag_matches": results,
        "keyword_matches": keyword_matches,
        "total_results": len(results) + len(keyword_matches)
    }


@router.get("/scaffolded")
async def list_scaffolded_agents() -> Dict[str, Any]:
    """List all agents that have been scaffolded."""
    scaffolder = get_agent_scaffolder()
    
    scaffolded = []
    for role in scaffolder.list_scaffolded():
        agent = scaffolder.get_scaffolded(role)
        if agent:
            scaffolded.append({
                "agent_role": role,
                "display_name": agent.config.display_name,
                "template_name": agent.config.template_name,
                "created_at": agent.created_at.isoformat(),
                "content_hash": agent.content_hash
            })
    
    return {
        "scaffolded_agents": scaffolded,
        "count": len(scaffolded)
    }


@router.get("/scaffolded/{agent_role}")
async def get_scaffolded_agent(agent_role: str) -> Dict[str, Any]:
    """Get details of a scaffolded agent."""
    scaffolder = get_agent_scaffolder()
    agent = scaffolder.get_scaffolded(agent_role)
    
    if not agent:
        raise HTTPException(status_code=404, detail=f"Scaffolded agent not found: {agent_role}")
    
    return agent.to_dict()
