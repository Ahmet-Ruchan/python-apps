# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write

# Sampling frequency
# Now, before starting the recorder, we have to declare a few variables.
# The first one is the sampling frequency of the audio
# (in most cases this will be 44100 or 48000 frames per second) and the second is recording duration.
freq = 44100

# Recording duration
duration = 5

# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
				samplerate=freq, channels=1)

# Record audio for the given number of seconds
sd.wait()

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)
