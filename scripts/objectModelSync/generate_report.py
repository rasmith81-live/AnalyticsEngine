"""
Generate synchronization report.
Creates HTML and Markdown reports of sync results.
"""

import json
import shutil
from pathlib import Path
from datetime import datetime

def archive_old_sync_reports(output_dir):
    """Archive existing sync reports before creating new ones."""
    output_dir = Path(output_dir)
    archive_dir = output_dir / "archive"
    archive_dir.mkdir(exist_ok=True)
    
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Files to archive
    files_to_archive = [
        output_dir / "sync_report.md",
        output_dir / "sync_report.html"
    ]
    
    archived_count = 0
    for file_path in files_to_archive:
        if file_path.exists():
            archive_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
            archive_path = archive_dir / archive_name
            shutil.move(str(file_path), str(archive_path))
            print(f"📦 Archived: {file_path.name} → archive/{archive_name}")
            archived_count += 1
    
    if archived_count > 0:
        print(f"✓ Archived {archived_count} old sync report(s)\n")
    
    return archived_count

def generate_sync_report(config, sync_results):
    """Generate comprehensive sync report."""
    print("Generating sync report...")
    
    output_dir = Path(config['paths']['output_dir'])
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Archive old reports first
    archive_old_sync_reports(output_dir)
    
    # Generate Markdown report
    md_report = generate_markdown_report(sync_results)
    md_file = output_dir / 'sync_report.md'
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_report)
    
    print(f"  Markdown report: {md_file}")
    
    # Generate HTML report if configured
    if config['reporting']['generate_html']:
        html_report = generate_html_report(sync_results)
        html_file = output_dir / 'sync_report.html'
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_report)
        
        print(f"  HTML report: {html_file}")
    
    return {
        'markdown': str(md_file),
        'html': str(html_file) if config['reporting']['generate_html'] else None
    }

def generate_markdown_report(results):
    """Generate Markdown report."""
    report = []
    
    report.append("# Object Model Synchronization Report")
    report.append(f"\n**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Duration**: {results.get('total_duration', 0):.2f} seconds")
    report.append("\n---\n")
    
    # Summary
    report.append("## Summary")
    successful = sum(1 for step in results['steps'] if step['success'])
    total = len(results['steps'])
    
    report.append(f"\n- **Total Steps**: {total}")
    report.append(f"- **Successful**: {successful}")
    report.append(f"- **Failed**: {total - successful}")
    report.append(f"- **Errors**: {len(results['errors'])}")
    report.append(f"- **Warnings**: {len(results['warnings'])}")
    
    if results.get('backup_path'):
        report.append(f"- **Backup**: {results['backup_path']}")
    
    # Steps
    report.append("\n## Steps Executed\n")
    for i, step in enumerate(results['steps'], 1):
        status = "✅" if step['success'] else "❌"
        report.append(f"### {i}. {status} {step['name']}")
        report.append(f"- **Duration**: {step.get('duration', 0):.2f}s")
        
        if step['success'] and step.get('data'):
            data = step['data']
            if isinstance(data, dict):
                for key, value in data.items():
                    report.append(f"- **{key}**: {value}")
        
        if step.get('error'):
            report.append(f"- **Error**: {step['error']}")
        
        report.append("")
    
    # Errors
    if results['errors']:
        report.append("\n## Errors\n")
        for error in results['errors']:
            report.append(f"- {error}")
    
    # Warnings
    if results['warnings']:
        report.append("\n## Warnings\n")
        for warning in results['warnings']:
            report.append(f"- {warning}")
    
    report.append("\n---\n")
    report.append(f"\n**Status**: {'✅ SUCCESS' if successful == total else '⚠️ COMPLETED WITH ERRORS'}")
    
    return '\n'.join(report)

def generate_html_report(results):
    """Generate HTML report."""
    successful = sum(1 for step in results['steps'] if step['success'])
    total = len(results['steps'])
    success_rate = (successful / total * 100) if total > 0 else 0
    
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Object Model Sync Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; border-bottom: 3px solid #4CAF50; padding-bottom: 10px; }}
        h2 {{ color: #555; margin-top: 30px; }}
        .summary {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }}
        .stat-card {{ background: #f9f9f9; padding: 20px; border-radius: 6px; border-left: 4px solid #4CAF50; }}
        .stat-card h3 {{ margin: 0 0 10px 0; color: #666; font-size: 14px; }}
        .stat-card .value {{ font-size: 32px; font-weight: bold; color: #333; }}
        .step {{ background: #f9f9f9; padding: 15px; margin: 10px 0; border-radius: 6px; }}
        .step.success {{ border-left: 4px solid #4CAF50; }}
        .step.failed {{ border-left: 4px solid #f44336; }}
        .error {{ background: #ffebee; padding: 10px; margin: 5px 0; border-radius: 4px; color: #c62828; }}
        .warning {{ background: #fff3e0; padding: 10px; margin: 5px 0; border-radius: 4px; color: #ef6c00; }}
        .success-badge {{ background: #4CAF50; color: white; padding: 5px 15px; border-radius: 20px; display: inline-block; }}
        .error-badge {{ background: #f44336; color: white; padding: 5px 15px; border-radius: 20px; display: inline-block; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔄 Object Model Synchronization Report</h1>
        <p><strong>Date:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p><strong>Duration:</strong> {results.get('total_duration', 0):.2f} seconds</p>
        
        <div class="summary">
            <div class="stat-card">
                <h3>Total Steps</h3>
                <div class="value">{total}</div>
            </div>
            <div class="stat-card">
                <h3>Success Rate</h3>
                <div class="value">{success_rate:.0f}%</div>
            </div>
            <div class="stat-card">
                <h3>Errors</h3>
                <div class="value">{len(results['errors'])}</div>
            </div>
            <div class="stat-card">
                <h3>Warnings</h3>
                <div class="value">{len(results['warnings'])}</div>
            </div>
        </div>
        
        <h2>Steps Executed</h2>
"""
    
    for i, step in enumerate(results['steps'], 1):
        status_class = "success" if step['success'] else "failed"
        status_icon = "✅" if step['success'] else "❌"
        
        html += f"""
        <div class="step {status_class}">
            <h3>{status_icon} {step['name']}</h3>
            <p><strong>Duration:</strong> {step.get('duration', 0):.2f}s</p>
"""
        
        if step['success'] and step.get('data'):
            data = step['data']
            if isinstance(data, dict):
                html += "<ul>"
                for key, value in data.items():
                    html += f"<li><strong>{key}:</strong> {value}</li>"
                html += "</ul>"
        
        if step.get('error'):
            html += f'<div class="error"><strong>Error:</strong> {step["error"]}</div>'
        
        html += "</div>"
    
    if results['errors']:
        html += "<h2>Errors</h2>"
        for error in results['errors']:
            html += f'<div class="error">{error}</div>'
    
    if results['warnings']:
        html += "<h2>Warnings</h2>"
        for warning in results['warnings']:
            html += f'<div class="warning">{warning}</div>'
    
    status_badge = "success-badge" if successful == total else "error-badge"
    status_text = "✅ SUCCESS" if successful == total else "⚠️ COMPLETED WITH ERRORS"
    
    html += f"""
        <h2>Final Status</h2>
        <p><span class="{status_badge}">{status_text}</span></p>
    </div>
</body>
</html>
"""
    
    return html

if __name__ == '__main__':
    import json
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    # Load sample results
    sample_results = {
        'start_time': datetime.now(),
        'end_time': datetime.now(),
        'total_duration': 45.5,
        'steps': [],
        'errors': [],
        'warnings': []
    }
    
    generate_sync_report(config, sample_results)
