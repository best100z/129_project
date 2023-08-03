###import the necessary library
import os;
import time;

### define a function that execute ls -l directory command using execv
def ls(directory): ###input the path to certain directory
	ls_path = "/bin/ls"; ###the path to code ls, it is /bin/ls in this system, but it could very much differ from different computer
	arg = [ls_path, "-l", directory]; ###the arguments that we would like to run
	os.execv(ls_path, arg); ###execute the command

num = 1; ###start with number 1
print("Start counting:"); ###announce that we are starting to count
while num > -1: ###make the loop keep going, and -1 can be later used as a way to exit the while loop
	print(num); ###print out the number,
	if num%10 == 0: ###as the number reaches some multiple of 10
		print("It is about to fork"); ###let the user know that it is about to fork
		retval = os.fork(); ###forking here, divide into parent--while loop and child--ls
		child = (retval == 0); ###if we are  in the 
		if child:
			print("About to execute ls");
			ls("/home/zky/zhou_5993043_homework/zhou_5993043_hw6"); ###execute the ls command, I am checking the files for this week's homework
	num += 1; ###increase by 1
	time.sleep(0.5); ###wait for half a second preparing to print the number again
	
	
