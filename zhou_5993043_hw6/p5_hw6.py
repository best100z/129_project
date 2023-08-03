import numpy as np;
from numpy import random;
import matplotlib.pyplot as plt;

"""
since the detection for the photon during each interval is 0.002, I am using random to generate a random number from 0 to 1, the boundary doesnt really matter since the probabilty only is finite when counting an interval
so I choose when the number is from 0 to 0.002, which with respect to the entire interval 1 has probability of selecting to be 0.002;
then I return the length of such result, which represents how many of the photons have we detected
"""
def in_1000():
	result = random.random(1000);
	result = result[result<0.002];
	return len(result);

###return the mean of result array
def mean():
	global result;
	return result.sum()/len(result);

###return n!; here it can only deal with discrete numbers, but idealy there are ways to generalize the factorial function
def fac(n):
	count = 1;
	for i in range(int(n),0,-1):
		count *= i;
	return count;

###calls the previous three functions and returns two array represnting the x,y of discrete points
def poi():
	global maxi, mini;
	mu = mean();
	sigma = np.sqrt(mu);
	x = np.arange(mini, maxi);
	y = np.arange(mini, maxi);
	for i, val in enumerate(x):
		y[i] = mu**val * np.exp(-mu)/fac(val);
	return x,y;

result = np.zeros(1000);
###obtain the result as well as getting the range
###############################
mini = 1001;
maxi = -1;
for i in range(1000):
	result[i] = in_1000();
	if maxi < result[i]:
		maxi = result[i]
	if mini > result[i]:
		mini = result[i]
###############################

f, ax = plt.subplots();
ax.hist(result, bins = np.arange(mini, maxi), density = True, label = "Hist Photon detection"); ###normalized plot
ax.plot(*poi(), color = "red", label = "Poission Distribution");
ax.set(title = "Photon detection simulation", xlabel = "Number of heads", ylabel = "Probability");
ax.legend(); 
f.savefig("/home/zky/zhou_5993043_homework/zhou_5993043_hw6/p5_hw6.eps", format = "eps");
