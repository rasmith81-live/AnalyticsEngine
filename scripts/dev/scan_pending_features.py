import re

def scan_features(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    pending_items = []
    current_section = ""
    
    for line in lines:
        line = line.strip()
        if line.startswith("## "):
            current_section = line.strip("# ").strip()
        elif line.startswith("### "):
            current_section = line.strip("# ").strip()
        
        if (line.startswith("#### Feature:") or line.startswith("#### Page:")) and "[COMPLETED]" not in line:
            item_name = line.replace("#### Feature:", "").replace("#### Page:", "").strip()
            pending_items.append(f"[{current_section}] {item_name}")

    return pending_items

if __name__ == "__main__":
    items = scan_features("c:\\Users\\Arthu\\CascadeProjects\\AnalyticsEngine\\features.md")
    if items:
        print("Found the following pending features:")
        for item in items:
            print(f"- {item}")
    else:
        print("All features appear to be marked as [COMPLETED]!")
