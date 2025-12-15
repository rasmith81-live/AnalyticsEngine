
import logging
from typing import Any, Dict, List, Optional
import re
from datetime import datetime

from ..models import DataQualityRule, RuleType, ValidationResult

logger = logging.getLogger(__name__)

class RulesEngine:
    """
    Engine for evaluating data quality rules against datasets or single records.
    """

    def validate_record(self, record: Dict[str, Any], rules: List[DataQualityRule]) -> List[ValidationResult]:
        """
        Validate a single record against a list of rules.
        """
        results = []
        for rule in rules:
            if not rule.is_active:
                continue
            
            try:
                result = self._evaluate_rule(record, rule)
                results.append(result)
            except Exception as e:
                logger.error(f"Error evaluating rule {rule.id} on record: {e}")
                results.append(ValidationResult(
                    rule_id=rule.id,
                    is_valid=False,
                    error_message=f"System error during validation: {str(e)}",
                    metadata={"error_type": "system_error"}
                ))
        return results

    def _evaluate_rule(self, record: Dict[str, Any], rule: DataQualityRule) -> ValidationResult:
        is_valid = True
        error_message = None
        
        # 1. Attribute Check
        value = None
        if rule.target_attribute:
            if rule.target_attribute not in record:
                # Decide if missing attribute is a failure. For quality rules, usually yes.
                return ValidationResult(
                    rule_id=rule.id,
                    is_valid=False,
                    error_message=f"Attribute '{rule.target_attribute}' missing from record",
                    metadata={"missing_attribute": True}
                )
            value = record[rule.target_attribute]

        # 2. Rule Evaluation
        if rule.rule_type == RuleType.NON_NULL:
            if value is None or (isinstance(value, str) and value.strip() == ""):
                is_valid = False
                error_message = f"Attribute '{rule.target_attribute}' cannot be null or empty"

        elif rule.rule_type == RuleType.RANGE:
            min_val = rule.parameters.get("min")
            max_val = rule.parameters.get("max")
            
            if value is not None:
                # Handle types (e.g. string numbers) if necessary, or assume typed input
                try:
                    if min_val is not None and float(value) < float(min_val):
                        is_valid = False
                        error_message = f"Value {value} is less than minimum {min_val}"
                    elif max_val is not None and float(value) > float(max_val):
                        is_valid = False
                        error_message = f"Value {value} is greater than maximum {max_val}"
                except (ValueError, TypeError):
                    is_valid = False
                    error_message = f"Value {value} could not be compared numerically"

        elif rule.rule_type == RuleType.FORMAT:
            regex_pattern = rule.parameters.get("regex")
            if regex_pattern and value is not None:
                if not re.match(regex_pattern, str(value)):
                    is_valid = False
                    error_message = f"Value '{value}' does not match format '{regex_pattern}'"

        elif rule.rule_type == RuleType.UNIQUENESS:
            # Cannot check uniqueness on single record isolation without external context
            # Pass true or mark as skipped
            pass 

        elif rule.rule_type == RuleType.CUSTOM:
            # Placeholder for custom logic injection
            pass

        return ValidationResult(
            rule_id=rule.id,
            entity_id=str(record.get("id")) if "id" in record else None,
            is_valid=is_valid,
            error_message=error_message
        )

    def validate_dataset(self, dataset: List[Dict[str, Any]], rules: List[DataQualityRule]) -> List[ValidationResult]:
        """
        Validate a full dataset.
        Includes row-level checks and set-level checks (uniqueness).
        """
        all_results = []
        
        # 1. Row-level checks
        for record in dataset:
            all_results.extend(self.validate_record(record, rules))
            
        # 2. Set-level checks (Uniqueness)
        for rule in rules:
            if not rule.is_active or rule.rule_type != RuleType.UNIQUENESS or not rule.target_attribute:
                continue
                
            # Check uniqueness
            seen = {}
            for i, record in enumerate(dataset):
                val = record.get(rule.target_attribute)
                if val is None:
                    continue # handled by NON_NULL if set
                
                # Simple string representation for hashability if needed
                val_key = str(val)
                
                if val_key in seen:
                    # Found duplicate
                    all_results.append(ValidationResult(
                        rule_id=rule.id,
                        entity_id=str(record.get("id", f"index_{i}")),
                        is_valid=False,
                        error_message=f"Duplicate value '{val}' found for {rule.target_attribute}",
                        metadata={"duplicate_of_index": seen[val_key]}
                    ))
                else:
                    seen[val_key] = i

        return all_results
