import numpy as np;
import matplotlib.pyplot as plt
import argparse;

def positive_integer(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

def obtain_args():
    parser = argparse.ArgumentParser(description="Capacitor simulation parameters")
    parser.add_argument("-n", "--ite", type=positive_integer, required=True, help="Number of iterations")
    parser.add_argument("-s", "--gs", type=positive_integer, required=True, help="Grid size (number of elements on a side)")
    parser.add_argument("-t", "--thi", type=positive_integer, required=True, help="Capacitor plate thickness")
    parser.add_argument("-w", "--wid", type=positive_integer, required=True, help="Capacitor plate width")
    parser.add_argument("-g", "--gap", type=positive_integer, required=True, help="Capacitor gap")
    parser.add_argument("-v", "--v", type=float, required=True, help="Potential V")
    args = parser.parse_args()
    return args

args = obtain_args();
ite = args.ite;
gs = args.gs;
thi = args.thi;
wid = args.wid;
gap = args.gap;
v = args.v;

bound = np.zeros((1,1)); ###this is to specify the boundary condition;
current = np.zeros((1,1)); ###this is the potential for current after however many iteration

def show_image(array):
    f, ax = plt.subplots();
    im = ax.imshow(array, interpolation='none', cmap='jet');
    ax.set_title('2D Array as an Image');
    ax.set_xlabel('X-axis');
    ax.set_ylabel('Y-axis');
    f.colorbar(im, ax = ax);
    f.savefig("/home/zky/zhou_5993043_homework/zhou_5993043_hw6/p7_hw6.eps", format = "eps");

###set the boundary, which if any point is 1 it doesnt change
def set_bound():
	global gs, thi, wid, gap, v;
	global bound, current;
	bound = np.zeros((gs,gs));
	current = np.zeros((gs,gs))
	bound[0] = 1;
	bound[-1] = 1;
	bound[:,0] = 1;
	bound[:,-1] = 1;
	mid = gs//2;
	bound[mid - gap//2 - thi: mid-gap//2, mid - wid//2 : mid + wid//2] = 1;
	bound[mid + gap//2 : mid+gap//2+thi, mid - wid//2 : mid + wid//2] = 1;	
	current[mid - gap//2 - thi: mid-gap//2, mid - wid//2 : mid + wid//2] = v;
	current[mid + gap//2 : mid+gap//2+thi, mid - wid//2 : mid + wid//2] = -v;	
	
def iteration():
	global ite, gs, thi, wid, gap, v;
	global bound, current;
	temp = current;
	if ite==0:
		return;
	else:
		for i, row in enumerate(temp):
			for j, col in enumerate(row):
				if bound[i][j] != 1:
					temp[i][j] = (temp[i-1][j] + temp[i + 1][j] + temp[i][j-1] + temp[i][j+1])/4;
		current = temp;
		ite -= 1;
		return iteration();

set_bound();
iteration();
show_image(current)
