import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

data = np.loadtxt("/home/zky/project_129/data.txt");
x = data[:,1];
y = data[:,0];
"""
def in_sq(x, A):
    return A/x**2;
f1, ax1 = plt.subplots();
par, cov = opt.curve_fit(in_sq, x, y);
x_line = np.linspace(15,80, 1000);
ax1.plot(x,y, "o", color = "blue", label = "data");
ax1.plot(x_line, in_sq(x_line, *par), color = "red", label = "inverse square fit");
plt.show();


# Define the model function
def exponential_decay(x, A, B):
    return A * np.exp(-B * x)

# Example data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([5.0, 3.3, 1.9, 1.1, 0.6, 0.2])

# Perform the curve fitting
params, cov_matrix = opt.curve_fit(exponential_decay, x_data, y_data)

# Evaluate the fit at some x values
x_values_for_evaluation = np.linspace(0, 10, 100)
y_fit = exponential_decay(x_values_for_evaluation, *params)

# Print the fitted parameters
print("Fitted parameters:")
print("A =", params[0])
print("B =", params[1])

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_values_for_evaluation, y_fit, label='Fitted Curve', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.title('Exponential Decay Fit')
plt.show()
"""