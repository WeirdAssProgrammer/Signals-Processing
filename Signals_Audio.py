#Main goal: Read Sound files(wav) and plot it

#Required liberaries:
import wave
import matplotlib.pyplot as plt
import numpy as np

with wave.open("C:\\Users\\RedBloodHunter\\Downloads\\gettysburg.wav",'r') as wavF:
    num_channels = wavF.getnchannels() # channels
    sample_width = wavF.getsampwidth() # sample width
    frame_rate = wavF.getframerate() # samples per sec
    num_frames = wavF.getnframes() # frames number
    frames = wavF.readframes(wavF.getnframes())

    #convert to nump arrays
    if sample_width == 2: # 16 bit 
        data = np.frombuffer(frames, dtype=np.int16)
    elif sample_width == 1: # 8 bit
        data = np.frombuffer(frames, dtype=np.uint8)
    else:
        raise ValueError("Sample width not supported")

    #if stereo use 1 channel
    if num_channels == 2:
        data = data[::2]

# x axis: time => frames / framerate
time = np.linspace(0, num_frames / frame_rate, num=num_frames)

#plot data
plt.plot(time, data)

plt.title("Audio Signal")
plt.xlabel("Time")
plt.ylabel("Amp")
plt.show()