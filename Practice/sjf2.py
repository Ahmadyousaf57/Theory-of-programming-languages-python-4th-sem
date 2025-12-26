# SJF (Non-Preemptive) with Arrival Time

n = int(input("Enter number of processes: "))

process = []
arrival_time = []
burst_time = []

for i in range(n):
    process.append(i + 1)
    at = int(input(f"Enter Arrival Time for Process {i+1}: "))
    bt = int(input(f"Enter Burst Time for Process {i+1}: "))
    arrival_time.append(at)
    burst_time.append(bt)

# Store all data in a list of dictionaries for easier handling
processes = []
for i in range(n):
    processes.append({
        "pid": process[i],
        "at": arrival_time[i],
        "bt": burst_time[i],
        "ct": 0,
        "tat": 0,
        "wt": 0,
        "completed": False
    })

current_time = 0
completed_processes = 0

while completed_processes < n:
    # Get all processes that have arrived and are not completed
    ready_queue = [p for p in processes if p["at"] <= current_time and not p["completed"]]

    if ready_queue:
        # Select process with the shortest burst time
        shortest_job = min(ready_queue, key=lambda x: x["bt"])

        # Set completion time
        shortest_job["ct"] = current_time + shortest_job["bt"]
        # Set turnaround time = CT - AT
        shortest_job["tat"] = shortest_job["ct"] - shortest_job["at"]
        # Set waiting time = TAT - BT
        shortest_job["wt"] = shortest_job["tat"] - shortest_job["bt"]
        # Mark as completed
        shortest_job["completed"] = True

        # Update current time
        current_time = shortest_job["ct"]
        completed_processes += 1
    else:
        current_time += 1  # CPU idle, so we increment time

# Print result
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for p in sorted(processes, key=lambda x: x["pid"]):
    print(f"P{p['pid']}\t{p['at']}\t{p['bt']}\t{p['ct']}\t{p['tat']}\t{p['wt']}")

# Averages
avg_tat = sum(p['tat'] for p in processes) / n
avg_wt = sum(p['wt'] for p in processes) / n
print(f"\nAverage Turnaround Time: {avg_tat}")
print(f"Average Waiting Time: {avg_wt}")
