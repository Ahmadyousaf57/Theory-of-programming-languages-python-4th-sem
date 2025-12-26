# FCFS Scheduling Algorithm

# Taking number of processes
n = int(input("Enter number of processes: "))
process = []
burst_time = []

for i in range(n):
    process.append(i + 1)
    bt = int(input(f"Enter Burst Time for Process {i + 1}: "))
    burst_time.append(bt)

waiting_time = [0] * n
turnaround_time = [0] * n

# Calculating waiting time
for i in range(1, n):
    waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

# Calculating turnaround time
for i in range(n):
    turnaround_time[i] = burst_time[i] + waiting_time[i]

# Output
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"{process[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Average Times
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n
print(f"\nAverage Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")
