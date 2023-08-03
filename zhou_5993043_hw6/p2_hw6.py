###import the necessary library
import time;
import threading;
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.lines import Line2D

###define the global variables
inp = 0;
add = -1;
count = 0

def num(): ###gracefully asking the user to provide a number input return the value
	n = input("Please input a number:\n");
	try:
		n = float(n);
		return n
	except:
		print("Sorry, this isn't a number\n");
		return num();

class Scope(object): ###creating the class
    def __init__(self, ax, maxt=2, dt=0.02): ###set initiate the class
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = np.array([])
        self.ydata = np.array([])
        ###this is to initiate the graph
        self.line, = self.ax.plot([],[], lw = 1, marker = "o", color = "blue") ###for this, I will plot it as points as dots and use a thin line to connect them
        self.ax.set(xlabel = "nth input", ylabel = "input val", title = "input stream") ###make the labels
        self.ax.set_ylim(-10, 10); 
        self.ax.set_xlim(0, self.maxt)

    def update(self, data):
        ###here is to use the global variables
        global count;
        global inp;
        global add;
        ###not to alter the value
        t = count; 
        y = inp;
        ###add is used as a signal to determine if we need to obtain new data for the animation
        add = -1;
        ###standard way of updating the graph
        self.tdata = np.append(self.tdata, t)
        self.ydata = np.append(self.ydata, y)
        self.ydata = self.ydata[self.tdata > (t-self.maxt)]
        self.tdata = self.tdata[self.tdata > (t-self.maxt)]
        self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
        ###for y lim, I am makig the upper limit as 5 greater than the maximum poits on the plot, and lower limit as 5 smaller than the minimum points on the plot
        maxy = np.amax(self.ydata);
        miny = np.amin(self.ydata);
        if abs(maxy - miny) > 1: ###only update the ylim if we are not squishing the graph
            self.ax.set_ylim(miny - 5, maxy + 5);
        self.ax.figure.canvas.draw()
        self.line.set_data(self.tdata, self.ydata)
        return self.line,

def thethread(): ###define the thread function
    ###declare that we are going to use the global variables
	global count;
	global inp;
	global add;
	add = -1; ###when initiating, we want to be able to take inputs
	count = 0;
	while True: ###keep running
		if add==-1: ###if we are in a state ready for receiving data
			inp = num();
			count += 1;
			add = 1; ###stop receiving data until allowed to receive again
		
if __name__ == '__main__':
    dt = 0.001
    fig, ax = plt.subplots()
    scope = Scope(ax, maxt=10, dt=dt); ###creat the scope object
    thr = threading.Thread(target = thethread) ###creating a new thread: same pid as main but it can run seperate code as the main process
    thr.start(); ###start the receiving process
    ani = animation.FuncAnimation(fig, scope.update, frames = 10, interval=dt*1000., blit=False) ###creat the animation

    plt.show()
