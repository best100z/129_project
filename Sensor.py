import time
import numpy as np; 
import board;
import busio;
import adafruit_ads1x15.ads1015 as ADS;
from adafruit_ads1x15.analog_in import AnalogIn;
###
ACQTIME = 0.1;
SPS = 920;
VGAIN = 1
nsamples = int(ACQTIME*SPS)
sinterval = 1.0/SPS
i2c = busio.I2C(board.SCL, board.SDA);
ads = ADS.ADS1015(i2c)
channel = AnalogIn(ads, ADS.P0);
ads.gain = VGAIN;
ads.data_rate = SPS
ads.mode = ADS.Mode.CONTINUOUS
indata = np.zeros(nsamples,'float')
vin = AnalogIn(ads, 0)
for i in range(nsamples):
	st = time.perf_counter()
	indata[i] = vin.voltage
	while (time.perf_counter() - st) <= sinterval:
		pass
with open("/home/kaiyanzhou/project_129/data.txt","w") as fil:
	for i,val in enumerate(indata):
		if val >=0.46:
			indata[i] = np.log((val-0.46)/3.67)/(-0.068)    
	print(indata, file = fil);
