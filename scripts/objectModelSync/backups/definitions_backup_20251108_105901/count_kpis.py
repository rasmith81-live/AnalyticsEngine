import csv

csv_path = r"C:\Users\Arthu\Downloads\kpidepot.com-channel-sales.csv"

with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    
print(f"Total KPIs: {len(rows)}")
print("\nFirst 5 KPIs:")
for i, row in enumerate(rows[:5]):
    print(f"{i+1}. {row['KPI']}")
