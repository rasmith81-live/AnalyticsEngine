# =============================================================================
# Prompt Fragments - Reusable Prompt Components
# Phase 19: Prompt Library Integration
# Reference: https://www.shawnewallace.com/2025-11-19-building-a-personal-prompt-library/
# =============================================================================
"""
Shared prompt fragments for composition into agent prompts.

Provides:
- Predefined reusable prompt sections
- Fragment composition utilities
- DRY principle for prompt engineering
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


@dataclass
class Fragment:
    """A reusable prompt fragment."""
    name: str
    content: str
    description: str = ""
    tags: List[str] = field(default_factory=list)


class PromptFragments:
    """
    Collection of reusable prompt fragments.
    
    These fragments can be composed together to build
    complete agent system prompts while following DRY principles.
    """
    
    COLLABORATION = Fragment(
        name="collaboration",
        content="""## Collaboration Guidelines
When collaborating with peers:
- Use the blackboard for task coordination and artifact sharing
- Signal readiness via contract adapter when completing subtasks
- Request peer review for critical decisions before finalizing
- Consult domain experts for questions outside your expertise
- Share intermediate results to enable parallel work""",
        description="Guidelines for inter-agent collaboration",
        tags=["collaboration", "teamwork", "blackboard"]
    )
    
    CONTRACT_RULES = Fragment(
        name="contract_rules",
        content="""## Contract Enforcement Rules
You must follow these behavioral contracts:
- Maximum 3 assumptions before requesting clarification
- Maximum 5 failed attempts before signaling struggle
- Always validate state transitions through the contract adapter
- Submit artifacts for peer review when confidence < 80%
- Hard stop on contract violations - do not proceed
- Escalate to human when stuck or facing ambiguity""",
        description="Behavioral contract rules for agents",
        tags=["contract", "rules", "enforcement"]
    )
    
    CODE_REVIEW = Fragment(
        name="code_review",
        content="""## Code Review Standards
When reviewing or generating code:
- Check for correctness, readability, and maintainability
- Identify potential bugs, security issues, or performance problems
- Suggest improvements following established best practices
- Verify proper error handling and edge cases
- Ensure code follows project conventions and style guides
- Consider testability and add test cases where appropriate""",
        description="Standards for code review tasks",
        tags=["code", "review", "quality"]
    )
    
    DEBUGGING = Fragment(
        name="debugging",
        content="""## Debugging Approach
When debugging issues:
- Reproduce the problem consistently before attempting fixes
- Isolate the root cause, not just symptoms
- Add descriptive logging to trace execution flow
- Check recent changes that may have introduced the bug
- Write a failing test case before implementing the fix
- Verify the fix doesn't introduce new issues""",
        description="Best practices for debugging",
        tags=["debugging", "troubleshooting", "fixes"]
    )
    
    DOCUMENTATION = Fragment(
        name="documentation",
        content="""## Documentation Standards
When writing documentation:
- Start with a clear summary of purpose and scope
- Include practical usage examples
- Document all parameters, return values, and exceptions
- Note prerequisites, dependencies, and limitations
- Keep documentation close to and in sync with code
- Use consistent formatting and terminology""",
        description="Standards for documentation",
        tags=["documentation", "writing", "standards"]
    )
    
    TASK_EXECUTION = Fragment(
        name="task_execution",
        content="""## Task Execution Protocol
When executing tasks:
1. Parse and validate the task requirements
2. Check for dependencies and prerequisites
3. Plan the approach before starting execution
4. Execute in small, verifiable steps
5. Validate results at each checkpoint
6. Signal completion with artifact submission
7. Request peer review if needed""",
        description="Protocol for task execution",
        tags=["task", "execution", "protocol"]
    )
    
    ERROR_HANDLING = Fragment(
        name="error_handling",
        content="""## Error Handling
When encountering errors:
- Log the error with full context and stack trace
- Classify the error type (transient, permanent, user error)
- Attempt recovery for transient errors with backoff
- Signal struggle for persistent failures
- Provide clear error messages for user-facing issues
- Never silently swallow exceptions""",
        description="Error handling guidelines",
        tags=["error", "handling", "recovery"]
    )
    
    DATA_QUALITY = Fragment(
        name="data_quality",
        content="""## Data Quality Standards
When working with data:
- Validate data types and formats before processing
- Check for null values, duplicates, and anomalies
- Apply appropriate data transformations consistently
- Document data lineage and transformations
- Flag data quality issues for upstream review
- Use appropriate statistical methods for analysis""",
        description="Data quality standards",
        tags=["data", "quality", "validation"]
    )
    
    SECURITY = Fragment(
        name="security",
        content="""## Security Considerations
When handling sensitive operations:
- Never log or expose sensitive data (PII, credentials)
- Validate and sanitize all user inputs
- Use parameterized queries to prevent injection
- Follow principle of least privilege
- Encrypt sensitive data at rest and in transit
- Report security concerns immediately""",
        description="Security guidelines",
        tags=["security", "privacy", "safety"]
    )
    
    PERFORMANCE = Fragment(
        name="performance",
        content="""## Performance Considerations
When optimizing for performance:
- Profile before optimizing - measure, don't guess
- Focus on algorithmic improvements first
- Use appropriate data structures for the use case
- Consider caching for expensive operations
- Batch operations where possible
- Monitor resource usage (memory, CPU, I/O)""",
        description="Performance optimization guidelines",
        tags=["performance", "optimization", "efficiency"]
    )
    
    @classmethod
    def get_all(cls) -> Dict[str, Fragment]:
        """Get all available fragments."""
        return {
            "collaboration": cls.COLLABORATION,
            "contract_rules": cls.CONTRACT_RULES,
            "code_review": cls.CODE_REVIEW,
            "debugging": cls.DEBUGGING,
            "documentation": cls.DOCUMENTATION,
            "task_execution": cls.TASK_EXECUTION,
            "error_handling": cls.ERROR_HANDLING,
            "data_quality": cls.DATA_QUALITY,
            "security": cls.SECURITY,
            "performance": cls.PERFORMANCE,
        }
    
    @classmethod
    def get(cls, name: str) -> Optional[Fragment]:
        """Get a fragment by name."""
        return cls.get_all().get(name)
    
    @classmethod
    def list_names(cls) -> List[str]:
        """List all fragment names."""
        return list(cls.get_all().keys())
    
    @classmethod
    def search_by_tag(cls, tag: str) -> List[Fragment]:
        """Find fragments by tag."""
        results = []
        for fragment in cls.get_all().values():
            if tag.lower() in [t.lower() for t in fragment.tags]:
                results.append(fragment)
        return results


class FragmentComposer:
    """
    Utility for composing prompts from fragments.
    
    Usage:
        composer = FragmentComposer()
        prompt = composer.compose(
            base_content="You are a data analyst.",
            fragments=["collaboration", "data_quality", "contract_rules"]
        )
    """
    
    def __init__(self):
        self._custom_fragments: Dict[str, Fragment] = {}
    
    def add_custom_fragment(self, fragment: Fragment) -> None:
        """Add a custom fragment."""
        self._custom_fragments[fragment.name] = fragment
        logger.info(f"Added custom fragment: {fragment.name}")
    
    def get_fragment(self, name: str) -> Optional[Fragment]:
        """Get a fragment by name (custom or built-in)."""
        if name in self._custom_fragments:
            return self._custom_fragments[name]
        return PromptFragments.get(name)
    
    def compose(
        self,
        base_content: str,
        fragments: List[str],
        separator: str = "\n\n"
    ) -> str:
        """
        Compose a prompt from base content and fragments.
        
        Args:
            base_content: The base prompt content
            fragments: List of fragment names to include
            separator: Separator between sections
            
        Returns:
            Composed prompt string
        """
        parts = [base_content]
        
        for frag_name in fragments:
            fragment = self.get_fragment(frag_name)
            if fragment:
                parts.append(fragment.content)
            else:
                logger.warning(f"Fragment not found: {frag_name}")
        
        return separator.join(parts)
    
    def compose_with_context(
        self,
        base_content: str,
        fragments: List[str],
        context: Dict[str, str],
        separator: str = "\n\n"
    ) -> str:
        """
        Compose a prompt with variable substitution.
        
        Args:
            base_content: The base prompt content (may contain {variables})
            fragments: List of fragment names to include
            context: Dictionary of variable names to values
            separator: Separator between sections
            
        Returns:
            Composed prompt string with variables substituted
        """
        composed = self.compose(base_content, fragments, separator)
        
        for var_name, var_value in context.items():
            placeholder = "{" + var_name + "}"
            composed = composed.replace(placeholder, var_value)
        
        return composed
    
    def preview(
        self,
        base_content: str,
        fragments: List[str]
    ) -> Dict[str, Any]:
        """
        Preview composition without executing.
        
        Returns metadata about what would be composed.
        """
        found_fragments = []
        missing_fragments = []
        
        for frag_name in fragments:
            fragment = self.get_fragment(frag_name)
            if fragment:
                found_fragments.append({
                    "name": fragment.name,
                    "description": fragment.description,
                    "tags": fragment.tags,
                    "content_length": len(fragment.content)
                })
            else:
                missing_fragments.append(frag_name)
        
        total_length = len(base_content) + sum(
            len(self.get_fragment(f).content) 
            for f in fragments 
            if self.get_fragment(f)
        )
        
        return {
            "base_content_length": len(base_content),
            "fragments_found": found_fragments,
            "fragments_missing": missing_fragments,
            "total_estimated_length": total_length,
            "success": len(missing_fragments) == 0
        }


_composer_instance: Optional[FragmentComposer] = None


def get_fragment_composer() -> FragmentComposer:
    """Get the singleton fragment composer instance."""
    global _composer_instance
    if _composer_instance is None:
        _composer_instance = FragmentComposer()
    return _composer_instance
