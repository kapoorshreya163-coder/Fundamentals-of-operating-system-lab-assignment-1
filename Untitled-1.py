# CPU Scheduling Algorithms: FCFS and SJF (Non-Preemptive)

class Process:
    def __init__(self, pid, at, bt):
        self.pid = pid  # Process ID
        self.at = at    # Arrival Time
        self.bt = bt    # Burst Time
        self.ct = 0     # Completion Time
        self.tat = 0    # Turnaround Time
        self.wt = 0     # Waiting Time


# Function to calculate FCFS Scheduling
def fcfs(processes):
    processes.sort(key=lambda x: x.at)  # Sort by Arrival Time
    time = 0

    print("\n--- FCFS Scheduling ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    for p in processes:
        if time < p.at:
            time = p.at  # CPU Idle condition

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        print(p.pid, "\t", p.at, "\t", p.bt, "\t", p.ct, "\t", p.tat, "\t", p.wt)

    avg_wt = sum(p.wt for p in processes) / len(processes)
    avg_tat = sum(p.tat for p in processes) / len(processes)

    print("Average Waiting Time =", avg_wt)
    print("Average Turnaround Time =", avg_tat)


# Function to calculate SJF Scheduling (Non-Preemptive)
def sjf(processes):
    processes_copy = processes[:]
    completed = []
    time = 0

    print("\n--- SJF Scheduling ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")

    while processes_copy:
        ready = [p for p in processes_copy if p.at <= time]

        if not ready:
            time += 1
            continue

        ready.sort(key=lambda x: x.bt)
        p = ready[0]
        processes_copy.remove(p)

        time += p.bt
        p.ct = time
        p.tat = p.ct - p.at
        p.wt = p.tat - p.bt

        completed.append(p)

        print(p.pid, "\t", p.at, "\t", p.bt, "\t", p.ct, "\t", p.tat, "\t", p.wt)

    avg_wt = sum(p.wt for p in completed) / len(completed)
    avg_tat = sum(p.tat for p in completed) / len(completed)

    print("Average Waiting Time =", avg_wt)
    print("Average Turnaround Time =", avg_tat)


# Main Program
processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    pid = input("Enter Process ID: ")
    at = int(input("Enter Arrival Time: "))
    bt = int(input("Enter Burst Time: "))
    processes.append(Process(pid, at, bt))

# Display Input
print("\nEntered Processes:")
print("PID\tAT\tBT")
for p in processes:
    print(p.pid, "\t", p.at, "\t", p.bt)

# Call FCFS and SJF
fcfs(processes)
sjf(processes)