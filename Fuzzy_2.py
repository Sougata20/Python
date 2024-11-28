import numpy as np
import matplotlib.pyplot as plt

# Triangular membership function
def triangular(x, a, b, c):
    """Triangle MF: a, b, c are the parameters for the triangle (a = left, b = peak, c = right)"""
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

# Trapezoidal membership function
def trapezoidal(x, a, b, c, d):
    """Trapezoid MF: a, b, c, d are the parameters for the trapezoid (a, b = left side, c, d = right side)"""
    return np.maximum(np.minimum((x - a) / (b - a), 1, (d - x) / (d - c)), 0)

# Gaussian membership function
def gaussian(x, mean, sigma):
    """Gaussian MF: mean and sigma are the parameters for the Gaussian distribution"""
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

# Create a range of x values
x = np.linspace(-10, 10, 500)

# Triangular membership function parameters
a, b, c = -5, 0, 5

# Trapezoidal membership function parameters
a_t, b_t, c_t, d_t = -7, -3, 3, 7

# Gaussian membership function parameters
mean, sigma = 0, 2

# Plotting the membership functions
plt.figure(figsize=(10, 6))

# Triangular Membership Function
plt.subplot(3, 1, 1)
plt.plot(x, triangular(x, a, b, c), label="Triangular MF", color="b")
plt.title("Triangular Membership Function")
plt.xlabel("x")
plt.ylabel("Membership")
plt.grid(True)
plt.legend()

# Trapezoidal Membership Function
plt.subplot(3, 1, 2)
plt.plot(x, trapezoidal(x, a_t, b_t, c_t, d_t), label="Trapezoidal MF", color="g")
plt.title("Trapezoidal Membership Function")
plt.xlabel("x")
plt.ylabel("Membership")
plt.grid(True)
plt.legend()

# Gaussian Membership Function
plt.subplot(3, 1, 3)
plt.plot(x, gaussian(x, mean, sigma), label="Gaussian MF", color="r")
plt.title("Gaussian Membership Function")
plt.xlabel("x")
plt.ylabel("Membership")
plt.grid(True)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
