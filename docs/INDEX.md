# Analytics Engine - Documentation Index

**Version**: 1.0  
**Last Updated**: December 21, 2025

Welcome to the Analytics Engine documentation. This index provides a comprehensive guide to all available documentation organized by topic.

---

## 📚 Documentation Structure

```
docs/
├── INDEX.md (this file)                    ← Master documentation index
├── getting-started/                        ← Quick start and setup guides
├── architecture/                           ← System architecture and design
├── development/                            ← Development guides and standards
├── operations/                             ← Deployment and operations
├── api/                                    ← API documentation
├── database/                               ← Database and migrations
├── services/                               ← Individual service documentation
└── reference/                              ← Reference materials
```

---

## 🚀 Getting Started

**New to Analytics Engine? Start here:**

1. **[Getting Started Guide](./getting-started/README.md)** - Complete setup (includes 5-minute quick start)
2. **[Architecture Overview](./architecture/README.md)** - Understand the system
3. **[Development Guide](./development/README.md)** - Development standards and setup
4. **[API Documentation](./api/README.md)** - API reference

---

## 📖 Core Documentation

### Getting Started
| Document | Description | Audience |
|----------|-------------|----------|
| [Quick Start Guide](../QUICK_START_GUIDE.md) | 5-minute setup guide | All users |
| [Installation Guide](./getting-started/installation.md) | Detailed installation steps | Developers, Ops |
| [Configuration Guide](./getting-started/configuration.md) | Environment and service config | Developers, Ops |
| [First Steps Tutorial](./getting-started/tutorial.md) | Hands-on tutorial | Developers |

### Architecture
| Document | Description | Audience |
|----------|-------------|----------|
| [Architecture Overview](./architecture/README.md) | System architecture and design | All |
| [Microservices Architecture](./architecture/microservices.md) | Service boundaries and patterns | Architects, Developers |
| [Data Architecture](./architecture/data-architecture.md) | Database, CQRS, TimescaleDB | Architects, DBAs |
| [Event-Driven Architecture](./architecture/event-driven.md) | Messaging and events | Architects, Developers |
| [Security Architecture](./architecture/security.md) | Authentication, authorization | Security, Architects |

### Development
| Document | Description | Audience |
|----------|-------------|----------|
| [Development Guide](./development/README.md) | Development standards and practices | Developers |
| [Development Setup](./development/setup.md) | Local development environment | Developers |
| [Coding Standards](./development/coding-standards.md) | Code style and conventions | Developers |
| [Testing Guide](./development/testing.md) | Unit, integration, E2E testing | Developers |
| [Contributing Guide](./development/contributing.md) | How to contribute | Contributors |

### Operations
| Document | Description | Audience |
|----------|-------------|----------|
| [Operations Guide](./operations/README.md) | Deployment and operations | DevOps, Ops |
| [Deployment Guide](./operations/deployment.md) | Docker, Kubernetes deployment | DevOps |
| [Monitoring Guide](./operations/monitoring.md) | Observability and metrics | DevOps, Ops |
| [Troubleshooting Guide](./operations/troubleshooting.md) | Common issues and solutions | All |
| [Backup and Recovery](./operations/backup-recovery.md) | Data backup strategies | Ops, DBAs |

### Database
| Document | Description | Audience |
|----------|-------------|----------|
| [Database Guide](./database/README.md) | Database architecture and usage | Developers, DBAs |
| [Migration Guide](./database/migrations.md) | Alembic migrations | Developers, DBAs |
| [TimescaleDB Guide](./database/timescaledb.md) | Time-series data management | Developers, DBAs |
| [Data Persistence](./database/data-persistence.md) | Docker volumes and persistence | Ops, DBAs |
| [Archival Guide](./archival_implementation_guide.md) | Data archival to lakehouse | Ops, DBAs |

### API Documentation
| Document | Description | Audience |
|----------|-------------|----------|
| [API Overview](./api/README.md) | API architecture and patterns | Developers |
| [API Gateway](./api/api-gateway.md) | Gateway routing and features | Developers |
| [REST API Guide](./api/rest-api.md) | REST API conventions | Developers |
| [Event API Guide](./api/event-api.md) | Event-driven APIs | Developers |
| [Authentication](./api/authentication.md) | API authentication | Developers |

---

## 🔧 Service Documentation

### Backend Services (Infrastructure)
| Service | Port | Documentation | Description |
|---------|------|---------------|-------------|
| Database Service | 8000 | [docs](./services/database_service.md) | Database operations, CQRS, migrations |
| Messaging Service | 8001 | [docs](./services/messaging_service.md) | Redis operations, pub/sub |
| Archival Service | 8005 | [docs](./services/archival_service.md) | Data archival to lakehouse |
| Observability Service | 8080 | [docs](./services/observability_service.md) | Monitoring, metrics, tracing |

### Business Services (Domain Logic)
| Service | Port | Documentation | Description |
|---------|------|---------------|-------------|
| Business Metadata | 8020 | [docs](./services/business_metadata.md) | KPI definitions, object models |
| Calculation Engine | 8021 | [docs](./services/calculation_engine_service.md) | KPI calculations |
| Demo Config Service | 8022 | [docs](./services/demo_config_service.md) | Configuration and proposals |
| Connector Service | 8023 | [docs](./services/connector_service.md) | Data source connectors |
| Ingestion Service | 8024 | [docs](./services/ingestion_service.md) | Data ingestion |
| Metadata Ingestion | 8025 | [docs](./services/metadata_ingestion_service.md) | Excel/CSV bulk import |
| Conversation Service | 8026 | [docs](./services/conversation_service.md) | Chatbot and NLP |

### Support Services
| Service | Port | Documentation | Description |
|---------|------|---------------|-------------|
| Systems Monitor | 8010 | [docs](./services/systems_monitor.md) | System health monitoring |
| Entity Resolution | 8012 | [docs](./services/entity_resolution_service.md) | Entity matching |
| Data Governance | 8013 | [docs](./services/data_governance_service.md) | Data quality |
| Machine Learning | 8014 | [docs](./services/machine_learning_service.md) | ML models |

### Frontend Services
| Service | Port | Documentation | Description |
|---------|------|---------------|-------------|
| API Gateway | 8090 | [docs](./services/api_gateway.md) | Unified API interface |
| Demo Config UI | 3000 | [docs](./services/demo_config_ui.md) | React frontend |

---

## 📋 Reference Documentation

### Scripts and Tools
| Tool | Documentation | Description |
|------|---------------|-------------|
| KPI Excel Processor | [scripts/kpiExcelProcessor/README.md](../scripts/kpiExcelProcessor/README.md) | Process KPI Excel/CSV files |
| Object Model Sync | [scripts/objectModelSync/README.md](../scripts/objectModelSync/README.md) | Governance suite |
| Migration Utilities | [scripts/MIGRATION_UTILITIES_GUIDE.md](../scripts/MIGRATION_UTILITIES_GUIDE.md) | Database migration tools |
| Quick Reference | [scripts/QUICK_REFERENCE.md](../scripts/QUICK_REFERENCE.md) | Command reference |

### Business Documentation
| Document | Description | Audience |
|----------|-------------|----------|
| [Business Plan](../BUSINESS_PLAN.md) | Business model and financials | Business, Management |
| [Features](../features.md) | Feature breakdown with estimates | Product, Development |
| [Changelog](../CHANGELOG.md) | Version history and changes | All |

### Technical Reference
| Document | Description | Audience |
|----------|-------------|----------|
| [Technology Stack](./reference/technology-stack.md) | Technologies used | Developers |
| [Design Patterns](./reference/design-patterns.md) | Patterns and practices | Architects, Developers |
| [Glossary](./reference/glossary.md) | Terms and definitions | All |
| [FAQ](./reference/faq.md) | Frequently asked questions | All |

---

## 🎯 Documentation by Role

### For Developers
1. [Getting Started Guide](./getting-started/README.md)
2. [Development Guide](./development/README.md)
3. [Architecture Overview](./architecture/README.md)
4. [Testing Guide](./development/testing.md)
5. [API Documentation](./api/README.md)
6. [Database Guide](./database/README.md)

### For DevOps/Operations
1. [Deployment Guide](./operations/deployment.md)
2. [Monitoring Guide](./operations/monitoring.md)
3. [Troubleshooting Guide](./operations/troubleshooting.md)
4. [Backup and Recovery](./operations/backup-recovery.md)
5. [Database Migrations](./database/migrations.md)
6. [Archival Guide](./archival_implementation_guide.md)

### For Architects
1. [Architecture Overview](./architecture/README.md)
2. [Microservices Architecture](./architecture/microservices.md)
3. [Data Architecture](./architecture/data-architecture.md)
4. [Event-Driven Architecture](./architecture/event-driven.md)
5. [Security Architecture](./architecture/security.md)
6. [Design Patterns](./reference/design-patterns.md)

### For Business Users
1. [Business Plan](../BUSINESS_PLAN.md)
2. [Features](../features.md)
3. [Getting Started Guide](./getting-started/README.md)
4. [API Gateway](./services/api_gateway.md)
5. [Demo Config UI](./services/demo_config_ui.md)

---

## 🔍 Documentation by Topic

### Getting Started & Setup
- [Getting Started Guide](./getting-started/README.md)
- [Installation Guide](./getting-started/installation.md)
- [Configuration Guide](./getting-started/configuration.md)
- [Development Guide](./development/README.md)

### Architecture & Design
- [Architecture Overview](./architecture/README.md)
- [Microservices Architecture](./architecture/microservices.md)
- [Data Architecture](./architecture/data-architecture.md)
- [Event-Driven Architecture](./architecture/event-driven.md)
- [CQRS Pattern](./architecture/cqrs-pattern.md)

### Database & Data
- [Database Guide](./database/README.md)
- [TimescaleDB Guide](./database/timescaledb.md)
- [Migration Guide](./database/migrations.md)
- [Data Persistence](./database/data-persistence.md)
- [Archival Guide](./archival_implementation_guide.md)

### Development & Testing
- [Development Guide](./development/README.md)
- [Coding Standards](./development/coding-standards.md)
- [Testing Guide](./development/testing.md)
- [Contributing Guide](./development/contributing.md)
- [Debugging Guide](./development/debugging.md)

### Deployment & Operations
- [Deployment Guide](./operations/deployment.md)
- [Docker Guide](./operations/docker.md)
- [Monitoring Guide](./operations/monitoring.md)
- [Troubleshooting Guide](./operations/troubleshooting.md)
- [Backup and Recovery](./operations/backup-recovery.md)

### APIs & Integration
- [API Overview](./api/README.md)
- [API Gateway](./api/api-gateway.md)
- [REST API Guide](./api/rest-api.md)
- [Event API Guide](./api/event-api.md)
- [Authentication](./api/authentication.md)

---

## 📊 Diagrams and Visualizations

### Architecture Diagrams
- [Service Endpoints Visualization](./service_endpoints_visualization.html) - Interactive service map
- [Architecture Diagrams](./architecture/diagrams/) - Lucidchart diagrams
- [Sequence Diagrams](./architecture/sequences/) - UML sequence diagrams

### Data Flow Diagrams
- [CQRS Data Flow](./architecture/diagrams/cqrs-flow.md)
- [Event Flow](./architecture/diagrams/event-flow.md)
- [Archival Flow](./architecture/timescaledb_archival.md)

---

## 🆕 Recent Updates

### December 21, 2025
- ✅ **Database Migration**: Added persistent storage tables (connector_profiles, client_configs, service_proposals)
- ✅ **Redis Fix**: Fixed Redis configuration error
- ✅ **Data Persistence**: Validated Docker volume persistence
- 📄 **New Docs**: DATABASE_MIGRATION_GUIDE.md

### December 19, 2025
- ✅ **Backend Integration**: DatabaseClient implementations for Connector and Demo Config services
- ✅ **Calculation Engine**: Refactored to use standardized clients
- 📄 **Updated**: CHANGELOG.md

See [CHANGELOG.md](../CHANGELOG.md) for complete history.

---

## 🔗 External Resources

### Technology Documentation
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [TimescaleDB Documentation](https://docs.timescale.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Docker Documentation](https://docs.docker.com/)
- [Redis Documentation](https://redis.io/documentation)

### Standards and Frameworks
- [SCOR Model](https://www.ascm.org/corporate-transformation/standards-methodology/scor/)
- [OpenTelemetry](https://opentelemetry.io/docs/)
- [Prometheus](https://prometheus.io/docs/)

---

## 📝 Documentation Standards

### Writing Guidelines
- Use clear, concise language
- Include code examples where appropriate
- Keep documentation up to date with code changes
- Use consistent formatting and structure
- Include diagrams for complex concepts

### Documentation Template
See [Documentation Template](./reference/doc-template.md) for the standard format.

---

## 🤝 Contributing to Documentation

Documentation improvements are always welcome! See [Contributing Guide](./development/contributing.md) for guidelines.

**To update documentation**:
1. Edit the relevant markdown file
2. Update this index if adding new documents
3. Update the changelog
4. Submit a pull request

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-org/analytics-engine/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-org/analytics-engine/discussions)
- **Email**: support@your-company.com

---

## 📄 License

MIT License - see [LICENSE](../LICENSE) file for details.

---

**Navigation**:
- [← Back to Main README](../README.md)
- [Getting Started →](./getting-started/README.md)
- [Architecture →](./architecture/README.md)

