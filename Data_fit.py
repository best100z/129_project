import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

data = np.loadtxt("/home/zky/project_129/data.txt");
x = data[:,1];
y = data[:,0];

def in_sq(x, A):
    return A/x**2;
f1, ax1 = plt.subplots();
par, cov = opt.curve_fit(in_sq, x, y);
x_line = np.linspace(15,80, 1000);
ax1.plot(x,y, "o", color = "blue", label = "data");
ax1.plot(x_line, in_sq(x_line, *par), color = "red", label = "inverse square fit");
ax1.legend();
f1.savefig("/home/zky/project_129/data_in_sq_fit.eps", format = "eps");


def expo_d(x, A, B):
    return A * np.exp(-B * x)

f2, ax2 = plt.subplots();
par, cov = opt.curve_fit(expo_d, x, y);
ax2.plot(x,y, "o", color = "blue", label = "data");
ax2.plot(x_line, expo_d(x_line, *par), color = "red", label = "decay exponential fit");
f2.savefig("/home/zky/project_129/data_dec_exp_fit.eps", format = "eps");
