import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt

duration = 5 # record for 5 sec
sample_rate = 44100

print(f"Recording for {duration} seconds")

data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
sd.wait() # wait untill the recording is finished
print("Recording finished")

data = data.flatten() # make 1d array

time_axis = np.linspace(0, duration, num=len(data))

#plot
plt.plot(time_axis, data)
plt.title("Recording signal")
plt.xlabel("Time")
plt.ylabel("Amp")
plt.show()