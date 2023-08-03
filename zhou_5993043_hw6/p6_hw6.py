import numpy as np;
import matplotlib.pyplot as plt;
from scipy import random;

###actual result: sqrt(pi)
act = np.sqrt(np.pi);
###(a)
###since the function is symmetric, I am going to find the fractional error for only the positive side;

a_act = act/2;

def gau(x):
	return np.exp(-x**2);

###since this is gaussian with standard deviation of 1, so it makes the most sense to only care about within 3 standard deviaion, which covers over 99 percent of the entire value
def inte(n): ###n is how many parts are we going to divide the interval from 0 to 2;
	points = np.linspace(0,3,n + 1)[1:] ###making the rectangle from the right point
	val = gau(points).sum() * 3/n;
	return val;

def a_x_y():
	global n;
	global a_act;
	x = np.arange(1,n+1);
	y = np.zeros(n);
	for i in x:
		y[i-1] = inte(i);
	y = abs(a_act - y)/a_act
	return x,y;

n = 100;	
f,ax = plt.subplots();
ax.set(title = "(a)Integral using rectangle", xlabel = "num of rectangles", ylabel = "fractional dif");
ax.plot(*a_x_y());
f.savefig("/home/zky/zhou_5993043_homework/zhou_5993043_hw6/p6_hw6_a.eps", format = "eps");

"""
The following is using the Monte Carlo method, for the same reason as above, I am going to select only the positive side from 0 to 3
"""
def inteM(n):
	x_span = 3; ###select x from 0 to 3
	points = random.uniform(0,x_span,n);
	val = gau(points).sum()/n * 3;
	return val;

n =1000
def b_x_y():
	global n;
	global a_act;
	x = np.arange(1,n+1);
	y = np.zeros(n);
	for i in x:
		y[i-1] = inteM(i);
	y = abs(a_act - y)/a_act
	return x,y;
f1,ax1 = plt.subplots();
ax1.set(title = "(a)Integral using Monte Carlo", xlabel = "num of random points", ylabel = "fractional dif");
ax1.plot(*b_x_y());
f1.savefig("/home/zky/zhou_5993043_homework/zhou_5993043_hw6/p6_hw6_b.eps", format = "eps");
