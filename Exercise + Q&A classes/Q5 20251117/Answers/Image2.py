import numpy as np
import matplotlib.pyplot as plt

# Define the potential energy function
def potential_energy(x, A, B):
    """
    Calculate potential energy V(x) = A/x^3 - B/x
    """
    return A / (x**3) - B / x

# Parameters
A = 2.0  # Can adjust A value as needed
B = 1.0  # Can adjust B value as needed

# Define x range with integer endpoints to minimize empty space
x_start = 1
x_end = 15
x = np.linspace(x_start, x_end, 5000)  # High resolution for smooth curve

# Calculate corresponding potential energy values
V = potential_energy(x, A, B)

# Find extremum points of potential energy
def derivative_V(x, A, B):
    """Calculate the derivative of V(x): V'(x) = -3A/x^4 + B/x^2"""
    return -3*A/(x**4) + B/(x**2)

# Solve V'(x) = 0, i.e., -3A/x^4 + B/x^2 = 0
# Rearranging: B/x^2 = 3A/x^4, which gives B*x^2 = 3A, so x^2 = 3A/B
x_critical = np.sqrt(3*A/B)
V_critical = potential_energy(x_critical, A, B)

# Calculate second derivative to determine nature of extremum
def second_derivative_V(x, A, B):
    """Calculate the second derivative of V(x): V''(x) = 12A/x^5 - 2B/x^3"""
    return 12*A/(x**5) - 2*B/(x**3)

second_deriv_at_critical = second_derivative_V(x_critical, A, B)

# Create the plot with maximum utilization of space
plt.figure(figsize=(12, 8))
plt.plot(x, V, label=f'$V(x) = \\frac{{{A}}}{{x^3}} - \\frac{{{B}}}{{x}}$', linewidth=2, color='blue')

# Mark the critical point
plt.plot(x_critical, V_critical, 'ro', markersize=8, label=f'Critical point: ({x_critical:.2f}, {V_critical:.2f})')

# Add asymptotic behavior indicators
plt.axhline(0, color='gray', linestyle='--', alpha=0.5, label='y=0')

# Mark some significant points
x_points = [1, 2, 3, 5, 8, 12]
for x_pt in x_points:
    if x_pt <= x_end:
        v_pt = potential_energy(x_pt, A, B)
        plt.plot(x_pt, v_pt, 'go', markersize=5, alpha=0.7)

# Annotate some points
plt.annotate(f'x=1\nV={potential_energy(1, A, B):.2f}', 
             xy=(1, potential_energy(1, A, B)), xytext=(1.5, potential_energy(1, A, B)+0.3),
             arrowprops=dict(arrowstyle='->', color='green', alpha=0.7),
             fontsize=10, ha='center')

plt.annotate(f'x=3\nV={potential_energy(3, A, B):.2f}', 
             xy=(3, potential_energy(3, A, B)), xytext=(3.5, potential_energy(3, A, B)-0.3),
             arrowprops=dict(arrowstyle='->', color='green', alpha=0.7),
             fontsize=10, ha='center')

# Set axis limits to use space efficiently
plt.xlim(x_start, x_end)
plt.ylim(min(V)*1.1, max(V)*1.1 if max(V) > 0 else max(V)*0.9)

plt.xlabel('$x$', fontsize=14)
plt.ylabel('$V(x)$', fontsize=14)
plt.title('Potential Energy Curve $V(x) = A/x^3 - B/x$ with Key Features', fontsize=16)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=12)

# Add text box with key characteristics
textstr = f'Parameters: A={A}, B={B}\n'
textstr += f'Critical point: x = √(3A/B) = {x_critical:.3f}\n'
textstr += f'Potential at critical point: V = {V_critical:.3f}\n'
if second_deriv_at_critical > 0:
    textstr += 'Nature: Local minimum (stable equilibrium)\n'
else:
    textstr += 'Nature: Local maximum (unstable equilibrium)\n'
textstr += 'Behavior: V(x) → +∞ as x → 0⁺\n'
textstr += 'Behavior: V(x) → 0 as x → ∞'

props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
plt.text(0.02, 0.98, textstr, transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=props)

plt.tight_layout()
plt.show()

# Print analysis results
print("Potential Energy Function Analysis:")
print(f"V(x) = {A}/x^3 - {B}/x")
print("\nAs x approaches 0+:")
print("  - A/x^3 term approaches positive infinity")
print("  - B/x term approaches positive infinity")
print("  - But since A/x^3 grows faster than B/x, the overall value approaches positive infinity")

print("\nAs x approaches infinity:")
print("  - A/x^3 term approaches 0")
print("  - B/x term approaches 0")
print("  - Overall value approaches 0")

print(f"\nExtremum Point Analysis:")
print(f"  Extremum position: x = √(3A/B) = √({3*A}/{B}) = {x_critical:.3f}")
print(f"  Potential energy at extremum: V = {V_critical:.3f}")
if second_deriv_at_critical > 0:
    print(f"  Second derivative: {second_deriv_at_critical:.3f} > 0, indicating a local minimum (stable equilibrium)")
else:
    print(f"  Second derivative: {second_deriv_at_critical:.3f} < 0, indicating a local maximum (unstable equilibrium)")

print(f"\nFunction values at integer points:")
for i in range(1, 8):
    print(f"  x={i}: V({i}) = {potential_energy(i, A, B):.3f}")



