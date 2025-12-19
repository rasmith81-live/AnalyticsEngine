
"""
Resource Scheduling Engine
"""
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta

class Scheduler:
    """Assigns resources to implementation tasks."""
    
    def generate_schedule(
        self,
        tasks: List[Dict[str, Any]],
        resources: List[Dict[str, Any]],
        start_date: Optional[datetime] = None
    ) -> Dict[str, Any]:
        """
        Generate a schedule assigning resources to tasks.
        
        Args:
            tasks: List of task dicts {id, effort_hours, dependencies}
            resources: List of resource dicts {id, availability_hours_per_week}
            start_date: Project start date (defaults to now)
            
        Returns:
            Schedule dictionary
        """
        if not start_date:
            start_date = datetime.utcnow()
            
        # Simplified scheduling algorithm (Critical Path-ish)
        # 1. Topological sort tasks (assumed sorted for this mock)
        # 2. Assign first available resource
        
        assignments = []
        current_date = start_date
        
        # Calculate total effort
        total_effort = sum(t.get("effort_hours", 0) for t in tasks)
        
        # Calculate total capacity per week
        total_capacity = sum(r.get("availability_hours_per_week", 40) for r in resources)
        
        if total_capacity == 0:
            raise ValueError("No resource capacity available")
            
        # Estimate duration in weeks
        weeks_needed = total_effort / total_capacity
        end_date = start_date + timedelta(weeks=weeks_needed)
        
        # Create mock assignments
        for task in tasks:
            assignments.append({
                "task_id": task["id"],
                "resource_id": resources[0]["id"] if resources else "unassigned",
                "start": current_date.isoformat(),
                "end": (current_date + timedelta(hours=task.get("effort_hours", 0))).isoformat()
            })
            
        return {
            "start_date": start_date,
            "end_date": end_date,
            "assignments": assignments,
            "total_weeks": weeks_needed
        }

class TimelineGenerator:
    """Generates Gantt chart data."""
    
    def generate_gantt_data(self, schedule: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Transform schedule into Gantt data format.
        
        Args:
            schedule: Schedule dictionary containing assignments
            
        Returns:
            List of Gantt chart items
        """
        gantt_data = []
        assignments = schedule.get("assignments", [])
        
        for assignment in assignments:
            gantt_item = {
                "id": assignment.get("task_id"),
                "name": f"Task {assignment.get('task_id')}", # In a real scenario, lookup task name
                "start": assignment.get("start"),
                "end": assignment.get("end"),
                "resource": assignment.get("resource_id"),
                "type": "task",
                "progress": 0, # Default progress
                "dependencies": [] # assignment doesn't strictly carry dependencies in this mock
            }
            gantt_data.append(gantt_item)
            
        # Add project summary if needed
        if schedule.get("start_date") and schedule.get("end_date"):
            gantt_data.insert(0, {
                "id": "project_summary",
                "name": "Project Timeline",
                "start": schedule.get("start_date").isoformat() if isinstance(schedule.get("start_date"), datetime) else schedule.get("start_date"),
                "end": schedule.get("end_date").isoformat() if isinstance(schedule.get("end_date"), datetime) else schedule.get("end_date"),
                "type": "project",
                "progress": 0,
                "hideChildren": False
            })
            
        return gantt_data
