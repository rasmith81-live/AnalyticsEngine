"""
SCOR Metrics Web Scraper

Scrapes metric definitions from ASCM SCOR Digital Standard website.
Extracts: ID, Name, Definition, Calculation, Data Collection, Discussion, etc.

Usage:
    python scrape_scor_metrics.py --output scor_metrics_complete.json
"""

import json
import time
import re
from typing import Dict, List, Any
from pathlib import Path

# List of all SCOR metrics to scrape
# Organized by Performance Attribute and Level

SCOR_METRICS = {
    "reliability": {
        "level_1": ["RL.1.1"],
        "level_2": ["RL.2.1", "RL.2.2", "RL.2.3", "RL.2.4"],
        "level_3": [
            "RL.3.1", "RL.3.2", "RL.3.3", "RL.3.4", "RL.3.5", 
            "RL.3.6", "RL.3.7", "RL.3.8", "RL.3.9", "RL.3.10",
            "RL.3.11", "RL.3.12", "RL.3.13", "RL.3.14", "RL.3.15"
        ]
    },
    "responsiveness": {
        "level_1": ["RS.1.1"],
        "level_2": ["RS.2.1", "RS.2.2", "RS.2.3"],
        "level_3": [
            "RS.3.1", "RS.3.2", "RS.3.3", "RS.3.4", "RS.3.5",
            "RS.3.6", "RS.3.7", "RS.3.8", "RS.3.9", "RS.3.10",
            "RS.3.11", "RS.3.12", "RS.3.13", "RS.3.14", "RS.3.15",
            "RS.3.16", "RS.3.17", "RS.3.18", "RS.3.19", "RS.3.20"
        ]
    },
    "agility": {
        "level_1": ["AG.1.1", "AG.1.2", "AG.1.3", "AG.1.4"],
        "level_2": [
            "AG.2.1", "AG.2.2", "AG.2.3", "AG.2.4",
            "AG.2.5", "AG.2.6", "AG.2.7", "AG.2.8"
        ],
        "level_3": [
            "AG.3.1", "AG.3.2", "AG.3.3", "AG.3.4", "AG.3.5",
            "AG.3.6", "AG.3.7", "AG.3.8", "AG.3.9", "AG.3.10"
        ]
    },
    "costs": {
        "level_1": ["CO.1.1", "CO.1.2"],
        "level_2": [
            "CO.2.1", "CO.2.2", "CO.2.3", "CO.2.4", "CO.2.5",
            "CO.2.6", "CO.2.7", "CO.2.8", "CO.2.9", "CO.2.10"
        ],
        "level_3": [
            "CO.3.1", "CO.3.2", "CO.3.3", "CO.3.4", "CO.3.5",
            "CO.3.6", "CO.3.7", "CO.3.8", "CO.3.9", "CO.3.10",
            "CO.3.11", "CO.3.12", "CO.3.13", "CO.3.14", "CO.3.15",
            "CO.3.16", "CO.3.17", "CO.3.18", "CO.3.19", "CO.3.20",
            "CO.3.21", "CO.3.22", "CO.3.23", "CO.3.24", "CO.3.25"
        ]
    },
    "assets": {
        "level_1": ["AM.1.1", "AM.1.2", "AM.1.3"],
        "level_2": [
            "AM.2.1", "AM.2.2", "AM.2.3", "AM.2.4",
            "AM.2.5", "AM.2.6", "AM.2.7", "AM.2.8"
        ],
        "level_3": [
            "AM.3.1", "AM.3.2", "AM.3.3", "AM.3.4", "AM.3.5",
            "AM.3.6", "AM.3.7", "AM.3.8", "AM.3.9", "AM.3.10"
        ]
    }
}

# Example metric data structure based on RL.1.1
EXAMPLE_METRIC = {
    "id": "RL.1.1",
    "name": "Perfect Customer Order Fulfillment",
    "attribute": "reliability",
    "level": "level_1",
    "definition": """The percentage of orders meeting delivery performance expectations, including complete and accurate documentation and no delivery damage. According to the APICS Dictionary, a perfect order satisfies the seven R's: the right product and/or service, the right quantity, the right condition, the right place, the right time (which should be measured by the customer's definition of on time), the right customer and the right cost.""",
    "calculation": "(Total perfect orders / Total number of orders) x 100%",
    "calculation_notes": [
        "An order is perfect if the individual line items making up that order are all perfect.",
        "For an order line to be perfect, all of the individual components must be perfect"
    ],
    "components": [
        {
            "metric": "RL.2.1",
            "name": "Percentage of Orders Delivered in Full to the Customer",
            "description": "Right product and/or service and right quantity"
        },
        {
            "metric": "RL.2.2",
            "name": "Delivery Performance to Original Customer Commit Date",
            "description": "Right time, right location and right customer"
        },
        {
            "metric": "RL.2.3",
            "name": "Customer Order Documentation Accuracy",
            "description": "Proper documentation"
        },
        {
            "metric": "RL.2.4",
            "name": "Customer Order Perfect Condition",
            "description": "Right condition"
        }
    ],
    "data_collection": {
        "primary_source": "Order",
        "description": "Data for the components that are used to drive the calculation of supply chain performance are primarily taken from Order."
    },
    "discussion": [
        "The performance of the supply chain is considered perfect if the original commitment made to a customer is met through the supply chain.",
        "An order is defined as a collection of one or more order lines representing a request to deliver specified quantities of goods or to render specific services.",
        "Orders canceled by the customer are excluded from this metric.",
        "Order changes initiated by the customer and agreed to by the supplier supersede initial commitments and form a new comparative basis for the metric."
    ],
    "unit": "Percentage",
    "dimension": "Quality",
    "related_processes": ["deliver"],
    "url": "https://scor.ascm.org/performance/reliability/RL.1.1"
}


def parse_metric_content(content: str, metric_id: str, attribute: str, level: str) -> Dict[str, Any]:
    """
    Parse the scraped content from a SCOR metric page.
    
    Args:
        content: Raw text content from the page
        metric_id: Metric ID (e.g., "RL.1.1")
        attribute: Performance attribute (reliability, responsiveness, etc.)
        level: Metric level (level_1, level_2, level_3)
    
    Returns:
        Structured metric data dictionary
    """
    metric = {
        "id": metric_id,
        "attribute": attribute,
        "level": level,
        "url": f"https://scor.ascm.org/performance/{attribute}/{metric_id}"
    }
    
    # Extract metric name (first line after ID)
    name_match = re.search(rf"{metric_id}\s+(.+?)(?:\n|Definition)", content, re.IGNORECASE)
    if name_match:
        metric["name"] = name_match.group(1).strip()
    
    # Extract definition
    def_match = re.search(r"Definition\s*\n(.+?)(?:\n\n|Calculation)", content, re.DOTALL | re.IGNORECASE)
    if def_match:
        metric["definition"] = def_match.group(1).strip()
    
    # Extract calculation
    calc_match = re.search(r"Calculation\s*\n(.+?)(?:\n\n|Data collection|Discussion)", content, re.DOTALL | re.IGNORECASE)
    if calc_match:
        calc_text = calc_match.group(1).strip()
        # Split into main formula and notes
        lines = calc_text.split('\n')
        metric["calculation"] = lines[0].strip()
        if len(lines) > 1:
            metric["calculation_notes"] = [line.strip() for line in lines[1:] if line.strip()]
    
    # Extract data collection
    data_match = re.search(r"Data collection\s*\n(.+?)(?:\n\n|Discussion)", content, re.DOTALL | re.IGNORECASE)
    if data_match:
        metric["data_collection"] = data_match.group(1).strip()
    
    # Extract discussion
    disc_match = re.search(r"Discussion\s*\n(.+?)$", content, re.DOTALL | re.IGNORECASE)
    if disc_match:
        discussion_text = disc_match.group(1).strip()
        # Split into paragraphs
        metric["discussion"] = [p.strip() for p in discussion_text.split('\n\n') if p.strip()]
    
    # Extract component metrics (Level 2 references in Level 1 metrics)
    component_pattern = r"((?:RL|RS|AG|CO|AM|EV|SC)\.\d\.\d+)"
    components = re.findall(component_pattern, content)
    if components and level == "level_1":
        metric["component_metrics"] = list(set(components))
    
    return metric


def generate_all_metric_ids() -> List[Dict[str, str]]:
    """
    Generate a flat list of all metric IDs with their attributes and levels.
    
    Returns:
        List of dicts with id, attribute, and level
    """
    all_metrics = []
    
    for attribute, levels in SCOR_METRICS.items():
        for level, metric_ids in levels.items():
            for metric_id in metric_ids:
                all_metrics.append({
                    "id": metric_id,
                    "attribute": attribute,
                    "level": level
                })
    
    return all_metrics


def save_metrics_to_json(metrics: List[Dict[str, Any]], output_file: str):
    """Save scraped metrics to JSON file."""
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Saved {len(metrics)} metrics to {output_path}")


def main():
    """
    Main scraper function.
    
    NOTE: This script provides the structure but cannot actually scrape
    the ASCM SCOR website due to authentication requirements.
    
    To use this:
    1. Manually copy metric content from SCOR pages
    2. Save to text files named {metric_id}.txt
    3. Run this script to parse and structure the data
    """
    print("🔍 SCOR Metrics Scraper")
    print("=" * 60)
    
    all_metrics = generate_all_metric_ids()
    print(f"📊 Total metrics to scrape: {len(all_metrics)}")
    
    # Count by level
    level_counts = {}
    for metric in all_metrics:
        level = metric["level"]
        level_counts[level] = level_counts.get(level, 0) + 1
    
    print(f"   Level 1 (Strategic): {level_counts.get('level_1', 0)}")
    print(f"   Level 2 (Diagnostic): {level_counts.get('level_2', 0)}")
    print(f"   Level 3 (Operational): {level_counts.get('level_3', 0)}")
    print()
    
    # Print example for manual scraping
    print("📝 Example: To manually scrape RL.1.1:")
    print("   1. Go to: https://scor.ascm.org/performance/reliability/RL.1.1")
    print("   2. Copy all text content")
    print("   3. Save to: data/scor_raw/RL.1.1.txt")
    print()
    
    print("🔧 To process saved text files:")
    print("   python scrape_scor_metrics.py --process data/scor_raw/")
    print()
    
    # Generate metric list file
    output_file = "data/scor_metrics_list.json"
    save_metrics_to_json(all_metrics, output_file)
    
    print("✅ Generated metric list with IDs and URLs")
    print(f"   Next: Manually scrape content from each URL")


if __name__ == "__main__":
    main()
