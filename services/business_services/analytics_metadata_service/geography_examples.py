"""
Geography and NAICS Examples

Demonstrates how to create geographic hierarchies and assign NAICS industry
classifications to clients.
"""

from analytics_models import Country, Region, MetropolitanStatisticalArea, Client


# ============================================================================
# Example 1: United States Geography
# ============================================================================

def create_us_geography():
    """Create US geography hierarchy."""
    
    # United States
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
    
    # California
    california = Region(
        country_id=usa.id,
        name="California",
        code="CA",
        region_type="state",
        capital="Sacramento",
        abbreviation="CA"
    )
    
    # New York
    new_york = Region(
        country_id=usa.id,
        name="New York",
        code="NY",
        region_type="state",
        capital="Albany",
        abbreviation="NY"
    )
    
    # Texas
    texas = Region(
        country_id=usa.id,
        name="Texas",
        code="TX",
        region_type="state",
        capital="Austin",
        abbreviation="TX"
    )
    
    # Los Angeles MSA
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
    
    # San Francisco MSA
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
    
    # New York MSA
    nyc_msa = MetropolitanStatisticalArea(
        region_id=new_york.id,
        name="New York-Newark-Jersey City, NY-NJ-PA",
        code="35620",
        cbsa_code="35620",
        msa_type="metropolitan",
        population=19216182,
        population_year=2020,
        central_city="New York",
        counties={
            "counties": [
                "Bronx County, NY",
                "Kings County, NY",
                "New York County, NY",
                "Queens County, NY",
                "Richmond County, NY",
                "Bergen County, NJ",
                "Hudson County, NJ",
                "Passaic County, NJ"
            ]
        }
    )
    
    # Austin MSA
    austin_msa = MetropolitanStatisticalArea(
        region_id=texas.id,
        name="Austin-Round Rock-Georgetown, TX",
        code="12420",
        cbsa_code="12420",
        msa_type="metropolitan",
        population=2283371,
        population_year=2020,
        central_city="Austin",
        counties={
            "counties": [
                "Travis County",
                "Williamson County",
                "Hays County",
                "Bastrop County",
                "Caldwell County"
            ]
        }
    )
    
    return {
        "country": usa,
        "regions": [california, new_york, texas],
        "msas": [la_msa, sf_msa, nyc_msa, austin_msa]
    }


# ============================================================================
# Example 2: Canada Geography
# ============================================================================

def create_canada_geography():
    """Create Canada geography hierarchy."""
    
    # Canada
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
    
    # Ontario
    ontario = Region(
        country_id=canada.id,
        name="Ontario",
        code="ON",
        region_type="province",
        capital="Toronto",
        abbreviation="ON"
    )
    
    # British Columbia
    bc = Region(
        country_id=canada.id,
        name="British Columbia",
        code="BC",
        region_type="province",
        capital="Victoria",
        abbreviation="BC"
    )
    
    # Toronto CMA
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
    
    # Vancouver CMA
    vancouver_cma = MetropolitanStatisticalArea(
        region_id=bc.id,
        name="Vancouver, BC",
        code="933",
        cbsa_code="933",
        msa_type="metropolitan",
        population=2642825,
        population_year=2021,
        central_city="Vancouver"
    )
    
    return {
        "country": canada,
        "regions": [ontario, bc],
        "msas": [toronto_cma, vancouver_cma]
    }


# ============================================================================
# Example 3: Technology Clients with NAICS
# ============================================================================

def create_technology_clients(usa, california, sf_msa):
    """Create technology clients with NAICS classification."""
    
    # Software Publisher
    saas_client = Client(
        name="CloudTech Solutions",
        code="CLOUDTECH",
        description="Enterprise SaaS platform provider",
        
        # NAICS - Software Publishers
        naics_code="511210",
        naics_title="Software Publishers",
        naics_sector="51 - Information",
        naics_subsector="511 - Publishing Industries (except Internet)",
        
        # Geography
        country_id=usa.id,
        region_id=california.id,
        metropolitan_area_id=sf_msa.id,
        
        contact_email="admin@cloudtech.com",
        contact_phone="+1-415-555-0100",
        
        config={
            "company_size": "mid_market",
            "employees": 250,
            "founded_year": 2015
        }
    )
    
    # Computer Systems Design
    consulting_client = Client(
        name="Digital Consulting Group",
        code="DCG",
        description="IT consulting and systems integration",
        
        # NAICS - Computer Systems Design Services
        naics_code="541512",
        naics_title="Computer Systems Design Services",
        naics_sector="54 - Professional, Scientific, and Technical Services",
        naics_subsector="5415 - Computer Systems Design and Related Services",
        
        # Geography
        country_id=usa.id,
        region_id=california.id,
        metropolitan_area_id=sf_msa.id,
        
        contact_email="admin@dcg.com",
        contact_phone="+1-415-555-0200",
        
        config={
            "company_size": "enterprise",
            "employees": 1500,
            "founded_year": 2005
        }
    )
    
    # Data Processing and Hosting
    hosting_client = Client(
        name="DataCenter Pro",
        code="DATACENTER",
        description="Cloud hosting and data center services",
        
        # NAICS - Data Processing, Hosting, and Related Services
        naics_code="518210",
        naics_title="Data Processing, Hosting, and Related Services",
        naics_sector="51 - Information",
        naics_subsector="5182 - Data Processing, Hosting, and Related Services",
        
        # Geography
        country_id=usa.id,
        region_id=california.id,
        metropolitan_area_id=sf_msa.id,
        
        contact_email="admin@datacenterpro.com",
        contact_phone="+1-415-555-0300"
    )
    
    return [saas_client, consulting_client, hosting_client]


# ============================================================================
# Example 4: Manufacturing Clients with NAICS
# ============================================================================

def create_manufacturing_clients(usa, california, la_msa):
    """Create manufacturing clients with NAICS classification."""
    
    # Electronics Manufacturing
    electronics_client = Client(
        name="Pacific Electronics Manufacturing",
        code="PAC_ELEC",
        description="Electronic components and assemblies",
        
        # NAICS - Computer and Electronic Product Manufacturing
        naics_code="334",
        naics_title="Computer and Electronic Product Manufacturing",
        naics_sector="31-33 - Manufacturing",
        naics_subsector="334 - Computer and Electronic Product Manufacturing",
        
        # Geography
        country_id=usa.id,
        region_id=california.id,
        metropolitan_area_id=la_msa.id,
        
        contact_email="admin@pacelec.com",
        contact_phone="+1-310-555-0100",
        
        config={
            "company_size": "large",
            "employees": 5000,
            "facilities": ["Los Angeles", "San Diego", "Phoenix"]
        }
    )
    
    # Semiconductor Manufacturing
    semiconductor_client = Client(
        name="Silicon Valley Semiconductors",
        code="SVS",
        description="Semiconductor and integrated circuit manufacturing",
        
        # NAICS - Semiconductor and Other Electronic Component Manufacturing
        naics_code="3344",
        naics_title="Semiconductor and Other Electronic Component Manufacturing",
        naics_sector="31-33 - Manufacturing",
        naics_subsector="334 - Computer and Electronic Product Manufacturing",
        
        # Geography
        country_id=usa.id,
        region_id=california.id,
        metropolitan_area_id=la_msa.id,
        
        contact_email="admin@svs.com",
        contact_phone="+1-310-555-0200"
    )
    
    return [electronics_client, semiconductor_client]


# ============================================================================
# Example 5: Retail Clients with NAICS
# ============================================================================

def create_retail_clients(usa, new_york, nyc_msa):
    """Create retail clients with NAICS classification."""
    
    # Department Store
    department_store = Client(
        name="Metro Department Stores",
        code="METRO_DEPT",
        description="Multi-location department store chain",
        
        # NAICS - Department Stores
        naics_code="452210",
        naics_title="Department Stores",
        naics_sector="44-45 - Retail Trade",
        naics_subsector="452 - General Merchandise Stores",
        
        # Geography
        country_id=usa.id,
        region_id=new_york.id,
        metropolitan_area_id=nyc_msa.id,
        
        contact_email="admin@metrodept.com",
        contact_phone="+1-212-555-0100",
        
        config={
            "company_size": "large",
            "store_count": 150,
            "regions": ["Northeast", "Mid-Atlantic"]
        }
    )
    
    # E-commerce Retailer
    ecommerce_client = Client(
        name="Digital Retail Group",
        code="DRG",
        description="Online retail marketplace",
        
        # NAICS - Electronic Shopping
        naics_code="454110",
        naics_title="Electronic Shopping",
        naics_sector="44-45 - Retail Trade",
        naics_subsector="454 - Nonstore Retailers",
        
        # Geography
        country_id=usa.id,
        region_id=new_york.id,
        metropolitan_area_id=nyc_msa.id,
        
        contact_email="admin@drg.com",
        contact_phone="+1-212-555-0200"
    )
    
    return [department_store, ecommerce_client]


# ============================================================================
# Example 6: Financial Services Clients with NAICS
# ============================================================================

def create_financial_clients(usa, new_york, nyc_msa):
    """Create financial services clients with NAICS classification."""
    
    # Commercial Bank
    bank_client = Client(
        name="Metropolitan Bank",
        code="METRO_BANK",
        description="Regional commercial bank",
        
        # NAICS - Commercial Banking
        naics_code="522110",
        naics_title="Commercial Banking",
        naics_sector="52 - Finance and Insurance",
        naics_subsector="5221 - Depository Credit Intermediation",
        
        # Geography
        country_id=usa.id,
        region_id=new_york.id,
        metropolitan_area_id=nyc_msa.id,
        
        contact_email="admin@metrobank.com",
        contact_phone="+1-212-555-0300",
        
        config={
            "company_size": "large",
            "branch_count": 200,
            "assets_usd": 50000000000
        }
    )
    
    # Investment Banking
    investment_bank = Client(
        name="Capital Investment Partners",
        code="CIP",
        description="Investment banking and securities",
        
        # NAICS - Investment Banking and Securities Dealing
        naics_code="523110",
        naics_title="Investment Banking and Securities Dealing",
        naics_sector="52 - Finance and Insurance",
        naics_subsector="5231 - Securities and Commodity Contracts Intermediation and Brokerage",
        
        # Geography
        country_id=usa.id,
        region_id=new_york.id,
        metropolitan_area_id=nyc_msa.id,
        
        contact_email="admin@cip.com",
        contact_phone="+1-212-555-0400"
    )
    
    return [bank_client, investment_bank]


# ============================================================================
# Usage Example
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Geography and NAICS Examples")
    print("=" * 80)
    
    # Create US geography
    print("\n1. Creating US Geography...")
    us_geo = create_us_geography()
    print(f"   ✓ Created country: {us_geo['country'].name}")
    print(f"   ✓ Created {len(us_geo['regions'])} regions")
    print(f"   ✓ Created {len(us_geo['msas'])} MSAs")
    
    # Create Canada geography
    print("\n2. Creating Canada Geography...")
    ca_geo = create_canada_geography()
    print(f"   ✓ Created country: {ca_geo['country'].name}")
    print(f"   ✓ Created {len(ca_geo['regions'])} provinces")
    print(f"   ✓ Created {len(ca_geo['msas'])} CMAs")
    
    # Create technology clients
    print("\n3. Creating Technology Clients...")
    tech_clients = create_technology_clients(
        us_geo['country'],
        us_geo['regions'][0],  # California
        us_geo['msas'][1]  # San Francisco MSA
    )
    print(f"   ✓ Created {len(tech_clients)} technology clients")
    for client in tech_clients:
        print(f"      - {client.name} (NAICS: {client.naics_code})")
    
    # Create manufacturing clients
    print("\n4. Creating Manufacturing Clients...")
    mfg_clients = create_manufacturing_clients(
        us_geo['country'],
        us_geo['regions'][0],  # California
        us_geo['msas'][0]  # Los Angeles MSA
    )
    print(f"   ✓ Created {len(mfg_clients)} manufacturing clients")
    for client in mfg_clients:
        print(f"      - {client.name} (NAICS: {client.naics_code})")
    
    # Create retail clients
    print("\n5. Creating Retail Clients...")
    retail_clients = create_retail_clients(
        us_geo['country'],
        us_geo['regions'][1],  # New York
        us_geo['msas'][2]  # NYC MSA
    )
    print(f"   ✓ Created {len(retail_clients)} retail clients")
    for client in retail_clients:
        print(f"      - {client.name} (NAICS: {client.naics_code})")
    
    # Create financial clients
    print("\n6. Creating Financial Services Clients...")
    fin_clients = create_financial_clients(
        us_geo['country'],
        us_geo['regions'][1],  # New York
        us_geo['msas'][2]  # NYC MSA
    )
    print(f"   ✓ Created {len(fin_clients)} financial services clients")
    for client in fin_clients:
        print(f"      - {client.name} (NAICS: {client.naics_code})")
    
    total_clients = (len(tech_clients) + len(mfg_clients) + 
                     len(retail_clients) + len(fin_clients))
    
    print(f"\n{'=' * 80}")
    print(f"Total: {total_clients} clients created with geography and NAICS classification")
    print("=" * 80)
