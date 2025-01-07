import sys
from naoqi import ALProxy

if len(sys.argv) != 4:
    print("Usage: python say_text.py <IP> <PORT> <TEXT>")
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])
text = sys.argv[3]

tts = ALProxy("ALTextToSpeech", ip, port)
tts.say(text)
