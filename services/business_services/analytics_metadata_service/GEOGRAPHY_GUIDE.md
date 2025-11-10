# Geography & NAICS Industry Classification Guide

## Overview

The geography models provide hierarchical geographic classification for clients, while NAICS (North American Industry Classification System) provides standardized industry classification. Together, they enable precise client segmentation and benchmarking.

---

## Geography Models

### 1. Country

**Purpose**: Represents a country with ISO codes and basic information.

**Key Fields**:
- `name` - Country name (e.g., "United States")
- `code` - Country code (e.g., "US")
- `iso_alpha2` - ISO 3166-1 alpha-2 code (e.g., "US")
- `iso_alpha3` - ISO 3166-1 alpha-3 code (e.g., "USA")
- `iso_numeric` - ISO 3166-1 numeric code (e.g., "840")
- `capital` - Capital city
- `currency_code` - ISO 4217 currency code (e.g., "USD")
- `currency_name` - Currency name (e.g., "US Dollar")
- `phone_code` - International dialing code (e.g., "+1")

**Relationships**:
- One-to-many with `Region`
- One-to-many with `Client`

### 2. Region

**Purpose**: Represents a state, province, or administrative region within a country.

**Key Fields**:
- `country_id` - Foreign key to Country
- `name` - Region name (e.g., "California", "Ontario")
- `code` - Region code (e.g., "CA", "ON")
- `region_type` - Type: state, province, territory, county, etc.
- `capital` - Capital city
- `abbreviation` - Common abbreviation

**Relationships**:
- Many-to-one with `Country`
- One-to-many with `MetropolitanStatisticalArea`
- One-to-many with `Client`

### 3. MetropolitanStatisticalArea (MSA)

**Purpose**: Represents a metropolitan statistical area as defined by the U.S. Office of Management and Budget or equivalent international designations.

**Key Fields**:
- `region_id` - Foreign key to Region
- `name` - MSA name (e.g., "New York-Newark-Jersey City, NY-NJ-PA")
- `code` - MSA code
- `cbsa_code` - Core Based Statistical Area (CBSA) code
- `msa_type` - Type: metropolitan, micropolitan
- `population` - Population estimate
- `population_year` - Year of population estimate
- `central_city` - Primary central city
- `counties` - Array of counties in the MSA (JSON)

**Relationships**:
- Many-to-one with `Region`
- One-to-many with `Client`

---

## NAICS Industry Classification

### What is NAICS?

The **North American Industry Classification System (NAICS)** is the standard used by Federal statistical agencies in classifying business establishments for the purpose of collecting, analyzing, and publishing statistical data related to the U.S. business economy.

### NAICS Hierarchy

1. **Sector** (2-digit) - 20 broad sectors
2. **Subsector** (3-digit) - More specific industry groups
3. **Industry Group** (4-digit) - Detailed industry groups
4. **NAICS Industry** (5-digit) - Specific industries
5. **National Industry** (6-digit) - Most detailed level

### Client NAICS Fields

- `naics_code` - Full NAICS code (up to 6 digits)
- `naics_title` - Industry title/description
- `naics_sector` - Sector name (2-digit level)
- `naics_subsector` - Subsector name (3-digit level)

---

## Usage Examples

### Example 1: Create Geographic Hierarchy

```python
from analytics_models import Country, Region, MetropolitanStatisticalArea

# Create United States
usa = Country(
    name="United States",
    code="US",
    iso_alpha2="US",
    iso_alpha3="USA",
    iso_numeric="840",
    capital="Washington, D.C.",
    currency_code="USD",
    currency_name="US Dollar",
    phone_code="+1"
)

# Create California
california = Region(
    country_id=usa.id,
    name="California",
    code="CA",
    region_type="state",
    capital="Sacramento",
    abbreviation="CA"
)

# Create Los Angeles MSA
la_msa = MetropolitanStatisticalArea(
    region_id=california.id,
    name="Los Angeles-Long Beach-Anaheim, CA",
    code="31080",
    cbsa_code="31080",
    msa_type="metropolitan",
    population=13200998,
    population_year=2020,
    central_city="Los Angeles",
    counties={
        "counties": [
            "Los Angeles County",
            "Orange County"
        ]
    }
)

# Create San Francisco MSA
sf_msa = MetropolitanStatisticalArea(
    region_id=california.id,
    name="San Francisco-Oakland-Berkeley, CA",
    code="41860",
    cbsa_code="41860",
    msa_type="metropolitan",
    population=4731803,
    population_year=2020,
    central_city="San Francisco",
    counties={
        "counties": [
            "San Francisco County",
            "Alameda County",
            "Contra Costa County",
            "Marin County",
            "San Mateo County"
        ]
    }
)
```

### Example 2: Create Client with Geography and NAICS

```python
from analytics_models import Client

# Technology company in San Francisco
tech_client = Client(
    name="Acme Software Inc",
    code="ACME_SOFT",
    description="Enterprise SaaS company",
    
    # NAICS Classification - Software Publishers
    naics_code="511210",
    naics_title="Software Publishers",
    naics_sector="51 - Information",
    naics_subsector="511 - Publishing Industries",
    
    # Geography
    country_id=usa.id,
    region_id=california.id,
    metropolitan_area_id=sf_msa.id,
    
    contact_email="admin@acmesoftware.com",
    contact_phone="+1-415-555-0100"
)

# Manufacturing company in Los Angeles
mfg_client = Client(
    name="Pacific Manufacturing Corp",
    code="PAC_MFG",
    description="Electronics manufacturing",
    
    # NAICS Classification - Computer and Electronic Product Manufacturing
    naics_code="334",
    naics_title="Computer and Electronic Product Manufacturing",
    naics_sector="31-33 - Manufacturing",
    naics_subsector="334 - Computer and Electronic Product Manufacturing",
    
    # Geography
    country_id=usa.id,
    region_id=california.id,
    metropolitan_area_id=la_msa.id,
    
    contact_email="admin@pacmfg.com",
    contact_phone="+1-310-555-0200"
)

# Retail company in New York
retail_client = Client(
    name="Metro Retail Group",
    code="METRO_RETAIL",
    description="Multi-location retail chain",
    
    # NAICS Classification - Department Stores
    naics_code="452210",
    naics_title="Department Stores",
    naics_sector="44-45 - Retail Trade",
    naics_subsector="452 - General Merchandise Stores",
    
    # Geography
    country_id=usa.id,
    region_id=new_york.id,
    metropolitan_area_id=nyc_msa.id,
    
    contact_email="admin@metroretail.com",
    contact_phone="+1-212-555-0300"
)
```

### Example 3: International Clients

```python
# Create Canada
canada = Country(
    name="Canada",
    code="CA",
    iso_alpha2="CA",
    iso_alpha3="CAN",
    iso_numeric="124",
    capital="Ottawa",
    currency_code="CAD",
    currency_name="Canadian Dollar",
    phone_code="+1"
)

# Create Ontario
ontario = Region(
    country_id=canada.id,
    name="Ontario",
    code="ON",
    region_type="province",
    capital="Toronto",
    abbreviation="ON"
)

# Create Toronto CMA (Census Metropolitan Area)
toronto_cma = MetropolitanStatisticalArea(
    region_id=ontario.id,
    name="Toronto, ON",
    code="535",
    cbsa_code="535",
    msa_type="metropolitan",
    population=6202225,
    population_year=2021,
    central_city="Toronto"
)

# Canadian client
canadian_client = Client(
    name="Maple Tech Solutions",
    code="MAPLE_TECH",
    description="Canadian technology services",
    
    # NAICS Classification
    naics_code="541512",
    naics_title="Computer Systems Design Services",
    naics_sector="54 - Professional, Scientific, and Technical Services",
    naics_subsector="5415 - Computer Systems Design and Related Services",
    
    # Geography
    country_id=canada.id,
    region_id=ontario.id,
    metropolitan_area_id=toronto_cma.id,
    
    contact_email="admin@mapletech.ca",
    contact_phone="+1-416-555-0400"
)
```

---

## Common NAICS Codes

### Technology Sector

| Code | Title |
|------|-------|
| 511210 | Software Publishers |
| 518210 | Data Processing, Hosting, and Related Services |
| 541511 | Custom Computer Programming Services |
| 541512 | Computer Systems Design Services |
| 541513 | Computer Facilities Management Services |
| 541519 | Other Computer Related Services |

### Manufacturing

| Code | Title |
|------|-------|
| 334 | Computer and Electronic Product Manufacturing |
| 335 | Electrical Equipment, Appliance, and Component Manufacturing |
| 336 | Transportation Equipment Manufacturing |

### Retail Trade

| Code | Title |
|------|-------|
| 441 | Motor Vehicle and Parts Dealers |
| 445 | Food and Beverage Stores |
| 452 | General Merchandise Stores |
| 454 | Nonstore Retailers |

### Finance and Insurance

| Code | Title |
|------|-------|
| 522110 | Commercial Banking |
| 522210 | Credit Card Issuing |
| 523110 | Investment Banking and Securities Dealing |
| 524113 | Direct Life Insurance Carriers |

### Healthcare

| Code | Title |
|------|-------|
| 621111 | Offices of Physicians (except Mental Health Specialists) |
| 622110 | General Medical and Surgical Hospitals |
| 623110 | Nursing Care Facilities (Skilled Nursing Facilities) |

---

## Query Examples

### Get Clients by Geography

```python
# Get all clients in California
ca_clients = session.query(Client).filter(
    Client.region_id == california.id,
    Client.is_active == True
).all()

# Get all clients in San Francisco MSA
sf_clients = session.query(Client).filter(
    Client.metropolitan_area_id == sf_msa.id,
    Client.is_active == True
).all()

# Get all US clients
us_clients = session.query(Client).filter(
    Client.country_id == usa.id,
    Client.is_active == True
).all()
```

### Get Clients by NAICS

```python
# Get all software publishers
software_clients = session.query(Client).filter(
    Client.naics_code == "511210",
    Client.is_active == True
).all()

# Get all clients in Information sector (51)
info_sector_clients = session.query(Client).filter(
    Client.naics_sector.like("51%"),
    Client.is_active == True
).all()

# Get all manufacturing clients (31-33)
mfg_clients = session.query(Client).filter(
    Client.naics_sector.like("31-33%"),
    Client.is_active == True
).all()
```

### Combined Geography and NAICS Queries

```python
# Get all software companies in California
ca_software = session.query(Client).filter(
    Client.region_id == california.id,
    Client.naics_code == "511210",
    Client.is_active == True
).all()

# Get all tech companies in San Francisco MSA
sf_tech = session.query(Client).filter(
    Client.metropolitan_area_id == sf_msa.id,
    Client.naics_sector.like("51%"),
    Client.is_active == True
).all()
```

---

## Benefits

### For Benchmarking
✅ **Geographic Segmentation** - Compare performance by region/MSA  
✅ **Industry Segmentation** - Compare against industry peers  
✅ **Combined Analysis** - Industry performance by geography  

### For Reporting
✅ **Regional Reports** - Performance by country/region/MSA  
✅ **Industry Reports** - Performance by NAICS sector  
✅ **Market Analysis** - Industry trends by geography  

### For Client Management
✅ **Client Segmentation** - Group clients by location and industry  
✅ **Territory Management** - Assign clients by geography  
✅ **Industry Specialization** - Focus on specific NAICS codes  

---

## Best Practices

### 1. **Use Standard Codes**
- Always use official ISO country codes
- Use official NAICS codes from census.gov
- Use official CBSA codes for MSAs

### 2. **Maintain Hierarchy**
- Ensure Region belongs to correct Country
- Ensure MSA belongs to correct Region
- Ensure Client geography is consistent

### 3. **Keep Data Current**
- Update population estimates annually
- Review NAICS codes every 5 years (when updated)
- Verify MSA definitions periodically

### 4. **Document Sources**
- Track data sources in metadata
- Note when data was last updated
- Document any custom classifications

---

## Data Sources

### Geography
- **ISO Codes**: https://www.iso.org/iso-3166-country-codes.html
- **US MSAs**: https://www.census.gov/programs-surveys/metro-micro.html
- **Canadian CMAs**: https://www.statcan.gc.ca/

### NAICS
- **US NAICS**: https://www.census.gov/naics/
- **NAICS Manual**: https://www.census.gov/naics/reference_files_tools/
- **NAICS Search**: https://www.census.gov/naics/search/

---

## API Endpoints (Suggested)

### Geography Endpoints
```
GET    /countries                  - List countries
POST   /countries                  - Create country
GET    /countries/{id}             - Get country
PUT    /countries/{id}             - Update country
GET    /countries/{id}/regions     - Get regions in country

GET    /regions                    - List regions
POST   /regions                    - Create region
GET    /regions/{id}               - Get region
PUT    /regions/{id}               - Update region
GET    /regions/{id}/msas          - Get MSAs in region

GET    /msas                       - List MSAs
POST   /msas                       - Create MSA
GET    /msas/{id}                  - Get MSA
PUT    /msas/{id}                  - Update MSA
```

### Client Geography Endpoints
```
GET    /clients?country_id={id}    - Filter by country
GET    /clients?region_id={id}     - Filter by region
GET    /clients?msa_id={id}        - Filter by MSA
GET    /clients?naics_code={code}  - Filter by NAICS
```

---

## Conclusion

The geography and NAICS models provide comprehensive client classification enabling precise segmentation, benchmarking, and analysis by location and industry.
