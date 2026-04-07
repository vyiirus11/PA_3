import time
import matplotlib.pyplot as plt
from main import common_subsequence, parse_input

# Load your input file
A, B, weights = parse_input("inputs/example2.in")

sizes = []
times = []

# Test increasing input sizes
for multiplier in range(1, 11):  # 10 test cases
    test_a = A * multiplier
    test_b = B * multiplier

    start = time.time()
    common_subsequence(test_a, test_b, weights)
    end = time.time()

    sizes.append(len(test_a))
    times.append(end - start)

# Plot
plt.plot(sizes, times, marker='o')
plt.title("HVLCS Runtime")
plt.xlabel("Input Size (string length)")
plt.ylabel("Time (seconds)")
plt.grid(True)

# Save graph
plt.savefig("images/runtime_graph.png")

# Show graph
plt.show()