import sys
from naoqi import ALProxy

if len(sys.argv) != 6:
    print("Usage: python record_audio.py <IP> <PORT> <PATH> <FILE_TYPE> <FREQUENCY>")
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])
path = sys.argv[3]
file_type = sys.argv[4]
frequency = int(sys.argv[5])

audio_recorder = ALProxy("ALAudioRecorder", ip, port)
audio_recorder.startMicrophonesRecording(path, file_type, frequency)
