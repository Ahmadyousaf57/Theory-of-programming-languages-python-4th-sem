# FCFS with Arrival Time

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

# Combine all data into one list for sorting
combined = list(zip(process, arrival_time, burst_time))
# Sort by arrival time
combined.sort(key=lambda x: x[1])

# Initialize lists
completion_time = [0] * n
turnaround_time = [0] * n
waiting_time = [0] * n

# First process
completion_time[0] = combined[0][1] + combined[0][2]  # AT + BT
turnaround_time[0] = completion_time[0] - combined[0][1]
waiting_time[0] = turnaround_time[0] - combined[0][2]

# Loop for other processes
for i in range(1, n):
    # CPU idle check
    if completion_time[i-1] < combined[i][1]:
        completion_time[i] = combined[i][1] + combined[i][2]
    else:
        completion_time[i] = completion_time[i-1] + combined[i][2]
    
    turnaround_time[i] = completion_time[i] - combined[i][1]
    waiting_time[i] = turnaround_time[i] - combined[i][2]

# Print Table
print("\nProcess\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    p, at, bt = combined[i]
    print(f"P{p}\t{at}\t{bt}\t{completion_time[i]}\t{turnaround_time[i]}\t{waiting_time[i]}")

# Averages
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n
print(f"\nAverage Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")
