import naoqi
import time
from naoqi import ALProxy
AR = ALProxy("ALAudioRecorder", "155.245.22.39", 9559)
AR.stopMicrophonesRecording()
AR.startMicrophonesRecording("/data/home/nao/recordings/microphones/vishuu3.wav","wav",16000,[0,0,1,0])
time.sleep(5)
AR.stopMicrophonesRecording()
