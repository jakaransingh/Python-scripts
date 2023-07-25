import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def get_cpu_percent():
    return psutil.cpu_percent(percpu=True)

def update_graph(frame):
    plt.clf()
    plt.title("CPU Usage (%)")
    plt.xlabel("CPU Core")
    plt.ylabel("Usage")
    cpu_percent = get_cpu_percent()
    plt.bar(range(len(cpu_percent)), cpu_percent, color='skyblue')
    plt.xticks(range(len(cpu_percent)), [f"Core {i}" for i in range(len(cpu_percent))])
    plt.ylim(0, 100)

if __name__ == "__main__":
    fig = plt.figure()
    ani = FuncAnimation(fig, update_graph, interval=1000)  # Update graph every 1 second (1000 ms)
    plt.show()
