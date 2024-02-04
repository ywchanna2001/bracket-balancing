import math

# Constants
g = 9.8
pi = 3.14

# Input
theta = float(input())
v = float(input())
alpha = float(input())

# Convert angles to radians
theta_rad = math.radians(theta)
alpha_rad = math.radians(alpha)

# Calculate time of flight (t)
t = (2 * v * math.sin(theta_rad)) / (g * math.cos(alpha_rad))

# Calculate horizontal distance (d)
d = v * math.cos(theta_rad) * t

# Print the results with two decimal places
print(f"{t:.2f} {d:.2f}")
