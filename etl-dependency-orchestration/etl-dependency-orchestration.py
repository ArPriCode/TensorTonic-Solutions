def schedule_pipeline(tasks: list, resource_budget: int) -> list:
    task_map = {t["name"]: t for t in tasks}
    completed = set()
    running = []
    unscheduled = set(task_map.keys())
    result = []
    
    current_time = 0
    used_resources = 0
    
    while len(completed) < len(tasks):
        still_running = []
        for task in running:
            if task["end_time"] == current_time:
                completed.add(task["name"])
                used_resources -= task["resources"]
            else:
                still_running.append(task)
        running = still_running
        
        ready_tasks = []
        for name in unscheduled:
            deps = task_map[name]["depends_on"]
            if all(dep in completed for dep in deps):
                ready_tasks.append(task_map[name])
                
        ready_tasks.sort(key=lambda t: t["name"])
        
        for task in ready_tasks:
            if used_resources + task["resources"] <= resource_budget:
                unscheduled.remove(task["name"])
                used_resources += task["resources"]
                end_time = current_time + task["duration"]
                
                running.append({
                    "name": task["name"],
                    "end_time": end_time,
                    "resources": task["resources"]
                })
                
                result.append({
                    "task_name": task["name"],
                    "start_time": current_time
                })
                
        if running:
            current_time = min(t["end_time"] for t in running)

    result.sort(key=lambda x: (x["start_time"], x["task_name"]))
    return result