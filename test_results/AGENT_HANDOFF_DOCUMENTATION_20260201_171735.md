# Agent Workflow Handoffs Documentation

This document provides a comprehensive reference of all workflow handoffs between agents
in the AnalyticsEngine multi-agent system.

## Overview

- **Total Handoff Types:** 37
- **Workflow Categories:** 10
- **Agent Types:** 26

## Handoff Matrix

| Source Agent | Target Agent | Tool Name | Category |
|-------------|--------------|-----------|----------|
| ArchitectAgent | BusinessAnalystAgent | `request_entity_validation` | Entity Design Workflow |
| ArchitectAgent | BusinessAnalystAgent | `request_kpi_requirements` | Entity Design Workflow |
| ArchitectAgent | DeveloperAgent | `request_schema_generation` | Entity Design Workflow |
| DeveloperAgent | TesterAgent | `request_test_specification` | Entity Design Workflow |
| DeveloperAgent | DocumenterAgent | `request_documentation` | Entity Design Workflow |
| TesterAgent | DocumenterAgent | `request_test_documentation` | Entity Design Workflow |
| DataScientistAgent | ArchitectAgent | `handoff_to_architect_for_model_design` | ML/Predictive Model Workflow |
| DataScientistAgent | DeveloperAgent | `handoff_to_developer_for_implementation` | ML/Predictive Model Workflow |
| DataScientistAgent | ArchitectAgent | `request_architecture_review` | ML/Predictive Model Workflow |
| ArchitectAgent | DeveloperAgent | `handoff_model_architecture_to_developer` | ML/Predictive Model Workflow |
| DeveloperAgent | TesterAgent | `handoff_ml_to_tester` | ML/Predictive Model Workflow |
| DeveloperAgent | DocumenterAgent | `handoff_ml_to_documenter` | ML/Predictive Model Workflow |
| BusinessAnalystAgent | DataAnalystAgent | `request_kpi_calculation_design` | Analytics Workflow |
| BusinessAnalystAgent | DataScientistAgent | `request_predictive_analysis` | Analytics Workflow |
| DataStewardAgent | DataScientistAgent | `request_statistical_validation` | Analytics Workflow |
| DataStewardAgent | DataScientistAgent | `request_ml_model_design` | Analytics Workflow |
| FormulaBuilderAgent | DataAnalystAgent | `request_data_analyst_review` | Analytics Workflow |
| SalesManagerAgent | MarketingManagerAgent | `request_mql_from_marketing` | Sales Pipeline Workflow |
| SalesManagerAgent | AccountantAgent | `request_deal_pricing` | Sales Pipeline Workflow |
| SalesManagerAgent | ProjectManagerAgent | `handoff_to_project_manager` | Sales Pipeline Workflow |
| MarketingManagerAgent | SalesManagerAgent | `handoff_mql_to_sales` | Sales Pipeline Workflow |
| MarketingManagerAgent | DataScientistAgent | `request_campaign_analytics` | Sales Pipeline Workflow |
| MarketingManagerAgent | UIDesignerAgent | `request_design_assets` | Sales Pipeline Workflow |
| CustomerSuccessManagerAgent | DataScientistAgent | `request_churn_prediction_model` | Customer Success Workflow |
| CustomerSuccessManagerAgent | SalesManagerAgent | `handoff_expansion_to_sales` | Customer Success Workflow |
| OperationsManagerAgent | DataScientistAgent | `request_demand_forecast_model` | Operations Workflow |
| ProcessEngineerAgent | OperationsManagerAgent | `request_operations_review` | Operations Workflow |
| ArchitectAgent | DataGovernanceSpecialistAgent | `request_governance_review` | Governance Workflow |
| IntegrationSpecialistAgent | MappingSpecialistAgent | `request_mapping_assistance` | Integration Workflow |
| IntegrationSpecialistAgent | DeveloperAgent | `request_custom_development` | Integration Workflow |
| DataQualityAnalystAgent | DataAnalystAgent | `request_data_profiling` | Integration Workflow |
| LibrarianCuratorAgent | ArchitectAgent | `request_architect_review` | Knowledge Curation Workflow |
| LibrarianCuratorAgent | BusinessAnalystAgent | `request_business_analyst_review` | Knowledge Curation Workflow |
| BusinessStrategistAgent | CompetitiveAnalystAgent | `request_competitive_analysis` | Knowledge Curation Workflow |
| CompetitiveAnalystAgent | BusinessStrategistAgent | `request_strategist_review` | Knowledge Curation Workflow |
| DeveloperAgent | DeploymentSpecialistAgent | `request_deployment_config` | Release Management Workflow |
| ReleaseManagerAgent | DeploymentSpecialistAgent | `request_deployment_review` | Release Management Workflow |

---

## Handoffs by Workflow Category

### Entity Design Workflow

#### Architect requests entity validation

- **Tool:** `request_entity_validation`
- **Source:** ArchitectAgent
- **Target:** BusinessAnalystAgent
- **Description:** Architect requests Business Analyst to validate entity design against industry best practices
- **Required Inputs:** entity_name, entity_type, proposed_attributes
- **Expected Outputs:** validation_status, recommendations
- **Response Tool:** `share_entity_validation`

#### Architect requests KPI requirements

- **Tool:** `request_kpi_requirements`
- **Source:** ArchitectAgent
- **Target:** BusinessAnalystAgent
- **Description:** Architect requests Business Analyst to identify KPIs for designed entities
- **Required Inputs:** entity_name, business_context
- **Expected Outputs:** kpi_list, measurement_requirements

#### Architect requests schema generation

- **Tool:** `request_schema_generation`
- **Source:** ArchitectAgent
- **Target:** DeveloperAgent
- **Description:** Architect requests Developer to generate schemas from entity designs
- **Required Inputs:** entity_definitions, schema_type
- **Expected Outputs:** schema_artifacts
- **Response Tool:** `share_schema_artifacts`

#### Developer requests test specification

- **Tool:** `request_test_specification`
- **Source:** DeveloperAgent
- **Target:** TesterAgent
- **Description:** Developer requests Tester to create test specifications for generated code
- **Required Inputs:** code_artifact, test_requirements
- **Expected Outputs:** test_specification, test_cases

#### Developer requests documentation

- **Tool:** `request_documentation`
- **Source:** DeveloperAgent
- **Target:** DocumenterAgent
- **Description:** Developer requests Documenter to create documentation for generated code
- **Required Inputs:** code_artifact, doc_type
- **Expected Outputs:** documentation

#### Tester requests test documentation

- **Tool:** `request_test_documentation`
- **Source:** TesterAgent
- **Target:** DocumenterAgent
- **Description:** Tester requests Documenter to create test documentation
- **Required Inputs:** test_suite, test_cases
- **Expected Outputs:** test_documentation

### ML/Predictive Model Workflow

#### Data Scientist handoff to Architect for model design

- **Tool:** `handoff_to_architect_for_model_design`
- **Source:** DataScientistAgent
- **Target:** ArchitectAgent
- **Description:** Data Scientist hands off correlation analysis to Architect for ML model architecture design
- **Required Inputs:** correlation_analysis_id, model_type, target_variable, features
- **Expected Outputs:** model_architecture

#### Data Scientist handoff to Developer for implementation

- **Tool:** `handoff_to_developer_for_implementation`
- **Source:** DataScientistAgent
- **Target:** DeveloperAgent
- **Description:** Data Scientist hands off model specification to Developer for implementation
- **Required Inputs:** model_specification_id, architecture_id
- **Expected Outputs:** implementation_artifacts

#### Data Scientist requests architecture review

- **Tool:** `request_architecture_review`
- **Source:** DataScientistAgent
- **Target:** ArchitectAgent
- **Description:** Data Scientist requests Architect to review proposed model architecture
- **Required Inputs:** model_specification, architecture_proposal
- **Expected Outputs:** review_feedback, approval_status

#### Architect handoff ML architecture to Developer

- **Tool:** `handoff_model_architecture_to_developer`
- **Source:** ArchitectAgent
- **Target:** DeveloperAgent
- **Description:** Architect hands off ML model architecture to Developer for implementation
- **Required Inputs:** architecture_id, model_specification_id
- **Expected Outputs:** implementation_plan

#### Developer handoff ML to Tester

- **Tool:** `handoff_ml_to_tester`
- **Source:** DeveloperAgent
- **Target:** TesterAgent
- **Description:** Developer hands off ML model implementation to Tester for testing
- **Required Inputs:** model_specification_id, implementation_id, model_type
- **Expected Outputs:** test_plan, test_results

#### Developer handoff ML to Documenter

- **Tool:** `handoff_ml_to_documenter`
- **Source:** DeveloperAgent
- **Target:** DocumenterAgent
- **Description:** Developer hands off ML model to Documenter for documentation
- **Required Inputs:** model_specification_id, model_name, model_purpose
- **Expected Outputs:** model_documentation, api_documentation, user_guide

### Analytics Workflow

#### Business Analyst requests KPI calculation design

- **Tool:** `request_kpi_calculation_design`
- **Source:** BusinessAnalystAgent
- **Target:** DataAnalystAgent
- **Description:** Business Analyst requests Data Analyst to design calculation logic for KPIs
- **Required Inputs:** kpi_list, calculation_requirements
- **Expected Outputs:** calculation_definitions

#### Business Analyst requests predictive analysis

- **Tool:** `request_predictive_analysis`
- **Source:** BusinessAnalystAgent
- **Target:** DataScientistAgent
- **Description:** Business Analyst requests Data Scientist to analyze KPIs for predictive opportunities
- **Required Inputs:** kpi_ids
- **Expected Outputs:** predictive_opportunities, correlation_analysis

#### Data Steward requests statistical validation

- **Tool:** `request_statistical_validation`
- **Source:** DataStewardAgent
- **Target:** DataScientistAgent
- **Description:** Data Steward requests Data Scientist to validate KPI correlations statistically
- **Required Inputs:** kpi_pairs, suspected_correlations
- **Expected Outputs:** statistical_validation, p_values

#### Data Steward requests ML model design

- **Tool:** `request_ml_model_design`
- **Source:** DataStewardAgent
- **Target:** DataScientistAgent
- **Description:** Data Steward collaborates with Data Scientist on predictive ML models
- **Required Inputs:** target_kpi, feature_kpis
- **Expected Outputs:** model_design, feature_importance

#### Formula Builder requests Data Analyst review

- **Tool:** `request_data_analyst_review`
- **Source:** FormulaBuilderAgent
- **Target:** DataAnalystAgent
- **Description:** Formula Builder requests Data Analyst to review calculation logic
- **Required Inputs:** formula_definition, calculation_steps
- **Expected Outputs:** review_feedback, optimization_suggestions

### Sales Pipeline Workflow

#### Sales Manager requests MQL from Marketing

- **Tool:** `request_mql_from_marketing`
- **Source:** SalesManagerAgent
- **Target:** MarketingManagerAgent
- **Description:** Sales Manager requests Marketing Qualified Leads from Marketing
- **Required Inputs:** lead_criteria, quantity_needed
- **Expected Outputs:** mql_list

#### Sales Manager requests deal pricing

- **Tool:** `request_deal_pricing`
- **Source:** SalesManagerAgent
- **Target:** AccountantAgent
- **Description:** Sales Manager requests deal pricing from Accountant
- **Required Inputs:** deal_id, pricing_requirements
- **Expected Outputs:** pricing_proposal, financial_terms

#### Sales Manager handoff to Project Manager

- **Tool:** `handoff_to_project_manager`
- **Source:** SalesManagerAgent
- **Target:** ProjectManagerAgent
- **Description:** Sales Manager hands off won deal to Project Manager for onboarding
- **Required Inputs:** deal_id, client_info, contract_terms
- **Expected Outputs:** onboarding_plan

#### Marketing Manager handoff MQL to Sales

- **Tool:** `handoff_mql_to_sales`
- **Source:** MarketingManagerAgent
- **Target:** SalesManagerAgent
- **Description:** Marketing Manager hands off qualified leads to Sales Manager
- **Required Inputs:** lead_list, qualification_criteria
- **Expected Outputs:** acceptance_status

#### Marketing Manager requests campaign analytics

- **Tool:** `request_campaign_analytics`
- **Source:** MarketingManagerAgent
- **Target:** DataScientistAgent
- **Description:** Marketing Manager requests campaign performance analysis
- **Required Inputs:** campaign_id
- **Expected Outputs:** performance_analysis, recommendations

#### Marketing Manager requests design assets

- **Tool:** `request_design_assets`
- **Source:** MarketingManagerAgent
- **Target:** UIDesignerAgent
- **Description:** Marketing Manager requests design assets for campaigns
- **Required Inputs:** campaign_brief, asset_requirements
- **Expected Outputs:** design_assets

### Customer Success Workflow

#### Customer Success requests churn prediction model

- **Tool:** `request_churn_prediction_model`
- **Source:** CustomerSuccessManagerAgent
- **Target:** DataScientistAgent
- **Description:** Customer Success requests churn prediction model from Data Scientist
- **Required Inputs:** customer_segment, prediction_requirements
- **Expected Outputs:** churn_model, risk_scores

#### Customer Success handoff expansion to Sales

- **Tool:** `handoff_expansion_to_sales`
- **Source:** CustomerSuccessManagerAgent
- **Target:** SalesManagerAgent
- **Description:** Customer Success hands off expansion opportunity to Sales
- **Required Inputs:** customer_id, expansion_opportunity
- **Expected Outputs:** sales_engagement_plan

### Operations Workflow

#### Operations Manager requests demand forecast model

- **Tool:** `request_demand_forecast_model`
- **Source:** OperationsManagerAgent
- **Target:** DataScientistAgent
- **Description:** Operations Manager requests demand forecasting model
- **Required Inputs:** forecast_horizon, product_categories
- **Expected Outputs:** forecast_model, predictions

#### Process Engineer requests operations review

- **Tool:** `request_operations_review`
- **Source:** ProcessEngineerAgent
- **Target:** OperationsManagerAgent
- **Description:** Process Engineer requests Operations Manager to review simulation results
- **Required Inputs:** simulation_id, process_changes
- **Expected Outputs:** review_feedback, approval_status

### Governance Workflow

#### Architect requests governance review

- **Tool:** `request_governance_review`
- **Source:** ArchitectAgent
- **Target:** DataGovernanceSpecialistAgent
- **Description:** Architect requests Data Governance Specialist to review entity design for compliance
- **Required Inputs:** entity_definition, compliance_requirements
- **Expected Outputs:** compliance_status, recommendations

### Integration Workflow

#### Integration Specialist requests mapping assistance

- **Tool:** `request_mapping_assistance`
- **Source:** IntegrationSpecialistAgent
- **Target:** MappingSpecialistAgent
- **Description:** Integration Specialist requests help with field mappings
- **Required Inputs:** source_schema, target_schema
- **Expected Outputs:** field_mappings, transformation_rules

#### Integration Specialist requests custom development

- **Tool:** `request_custom_development`
- **Source:** IntegrationSpecialistAgent
- **Target:** DeveloperAgent
- **Description:** Integration Specialist requests custom integration code
- **Required Inputs:** integration_requirements, api_specifications
- **Expected Outputs:** integration_code

#### Data Quality Analyst requests data profiling

- **Tool:** `request_data_profiling`
- **Source:** DataQualityAnalystAgent
- **Target:** DataAnalystAgent
- **Description:** Data Quality Analyst requests Data Analyst to profile source data
- **Required Inputs:** data_source, profiling_requirements
- **Expected Outputs:** data_profile, quality_metrics

### Knowledge Curation Workflow

#### Librarian Curator requests Architect review

- **Tool:** `request_architect_review`
- **Source:** LibrarianCuratorAgent
- **Target:** ArchitectAgent
- **Description:** Librarian Curator requests Architect to review extracted entities for DDD design
- **Required Inputs:** extracted_entities, domain_context
- **Expected Outputs:** design_feedback, entity_refinements

#### Librarian Curator requests Business Analyst review

- **Tool:** `request_business_analyst_review`
- **Source:** LibrarianCuratorAgent
- **Target:** BusinessAnalystAgent
- **Description:** Librarian Curator requests Business Analyst to review extracted KPIs
- **Required Inputs:** extracted_kpis, business_context
- **Expected Outputs:** kpi_validation, business_alignment

#### Business Strategist requests competitive analysis

- **Tool:** `request_competitive_analysis`
- **Source:** BusinessStrategistAgent
- **Target:** CompetitiveAnalystAgent
- **Description:** Business Strategist requests competitive analysis after business model elicitation
- **Required Inputs:** business_model, market_segment
- **Expected Outputs:** competitive_landscape, peer_analysis

#### Competitive Analyst requests Strategist review

- **Tool:** `request_strategist_review`
- **Source:** CompetitiveAnalystAgent
- **Target:** BusinessStrategistAgent
- **Description:** Competitive Analyst requests Business Strategist to review findings
- **Required Inputs:** competitive_findings, market_analysis
- **Expected Outputs:** strategic_implications, recommendations

### Release Management Workflow

#### Developer requests deployment config

- **Tool:** `request_deployment_config`
- **Source:** DeveloperAgent
- **Target:** DeploymentSpecialistAgent
- **Description:** Developer requests deployment configuration from Deployment Specialist
- **Required Inputs:** artifact_id, deployment_target
- **Expected Outputs:** deployment_config, infrastructure_requirements

#### Release Manager requests deployment review

- **Tool:** `request_deployment_review`
- **Source:** ReleaseManagerAgent
- **Target:** DeploymentSpecialistAgent
- **Description:** Release Manager requests Deployment Specialist to review release plan
- **Required Inputs:** release_plan, deployment_schedule
- **Expected Outputs:** review_feedback, approval_status

---

## Agent Collaboration Summary

### Agents as Handoff Source

| Agent | Outgoing Handoffs |
|-------|------------------|
| ArchitectAgent | 5 |
| DeveloperAgent | 5 |
| DataScientistAgent | 3 |
| SalesManagerAgent | 3 |
| MarketingManagerAgent | 3 |
| BusinessAnalystAgent | 2 |
| DataStewardAgent | 2 |
| CustomerSuccessManagerAgent | 2 |
| IntegrationSpecialistAgent | 2 |
| LibrarianCuratorAgent | 2 |
| TesterAgent | 1 |
| FormulaBuilderAgent | 1 |
| OperationsManagerAgent | 1 |
| ProcessEngineerAgent | 1 |
| DataQualityAnalystAgent | 1 |
| BusinessStrategistAgent | 1 |
| CompetitiveAnalystAgent | 1 |
| ReleaseManagerAgent | 1 |

### Agents as Handoff Target

| Agent | Incoming Handoffs |
|-------|------------------|
| DataScientistAgent | 6 |
| DeveloperAgent | 4 |
| BusinessAnalystAgent | 3 |
| DocumenterAgent | 3 |
| ArchitectAgent | 3 |
| DataAnalystAgent | 3 |
| TesterAgent | 2 |
| SalesManagerAgent | 2 |
| DeploymentSpecialistAgent | 2 |
| MarketingManagerAgent | 1 |
| AccountantAgent | 1 |
| ProjectManagerAgent | 1 |
| UIDesignerAgent | 1 |
| OperationsManagerAgent | 1 |
| DataGovernanceSpecialistAgent | 1 |
| MappingSpecialistAgent | 1 |
| CompetitiveAnalystAgent | 1 |
| BusinessStrategistAgent | 1 |
