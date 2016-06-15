import DataCollector
import math
import numpy as np
import matplotlib.pyplot as plt

#Setup the DAta Collector
DC = DataCollector.DataCollector()
DC.addParams(['time','freq','sin','cos'])

#Run the simulation
for i in range(0,5000):
    time = i/100;
    freq = i/1000;
    sin = 20*math.sin(freq*time);
    cos = 18*math.cos(time);
    DC.slurp();
    
#Plot the Data
plt.figure
plt.subplot(2,1,1)
plt.plot(DC.get('time'),DC.get('sin'));
plt.hold;
plt.plot(DC.get('time'),DC.get('freq'));
plt.subplot(2,1,2)
plt.plot(DC.get('time'),DC.get('cos'));


