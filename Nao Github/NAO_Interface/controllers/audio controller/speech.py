
# speech.py
import naoqi, paramiko, time
from naoqi import ALProxy
from core.config import CONFIGS
# Variables:
IP = CONFIGS['IP']
soundRecordPath = CONFIGS["soundRecordPath"] # Recording path stored in Nao
localPath = CONFIGS['localPath'] # Our target path on our device
MODEL_TTS = CONFIGS['MODEL_TTS']
PORT = CONFIGS['PORT']
MODEL_RECORDER = CONFIGS["MODEL_RECORDER"]
USER = CONFIGS['USER']
PASS = CONFIGS['PASS']
AUDIO_FILE_TYPE = CONFIGS["AUDIO_FILE_TYPE"]
SPEAKER = CONFIGS["SPEAKER"]
SAMPLING_FREQUENCY = CONFIGS["SAMPLING_FREQUENCY"]
DELAY = CONFIGS["DELAY"]
DrivePORT = CONFIGS["DrivePORT"]

tts = ALProxy(MODEL_TTS, IP, PORT)
tts.say("what can I do for you Ahmed?")

audio_recorder = ALProxy(MODEL_RECORDER, IP, PORT)
audio_recorder.startMicrophonesRecording(soundRecordPath, AUDIO_FILE_TYPE,SAMPLING_FREQUENCY , SPEAKER )
time.sleep(DELAY)
audio_recorder.stopMicrophonesRecording()

ssh_client =paramiko.SSHClient() # SSH
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=IP,port=DrivePORT,username=USER,password=PASS)
ftp_client =ssh_client.open_sftp() # Secure File Transfer Protocl
ftp_client.get(soundRecordPath, localPath)

ftp_client.close()

ssh_client.close()
