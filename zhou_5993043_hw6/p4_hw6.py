import numpy as np;
from numpy import random;
import matplotlib.pyplot as plt;

results = np.zeros(1000);

def head_100():
	result = random.randint(0,2,100).sum();
	return result;

def mu():
	global results;
	return results.sum()/len(results);

def sigma():
	global results;
	mean = mu();
	sq_dif = (results-mean)**2;
	var = sq_dif.sum()/len(results);
	return var**(0.5);

def gaus():
	mean = mu();
	si = sigma();
	x = np.linspace(0,100,1000);
	val = 1/si/(2*np.pi)**(0.5)*np.exp(-(x-mean)**2/2/si**2);
	return x, val;

f, ax = plt.subplots();
for i in range(1000):
	results[i] = head_100();

ax.hist(results, bins = np.arange(0, 102), density = True, label = "Coin Toss Hist");
ax.plot(*gaus(), color = "red", label = "Gaussian distribution");
ax.set(title = "Coin toss simulation", xlabel = "Number of heads", ylabel = "Probability");
ax.legend();
f.savefig("/home/zky/zhou_5993043_homework/zhou_5993043_hw6/p4_hw6.eps", format = "eps");
plt.show()	
