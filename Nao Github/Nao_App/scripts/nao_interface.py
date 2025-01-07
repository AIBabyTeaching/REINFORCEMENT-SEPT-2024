# scripts/nao_interface.py placeholder file
# Python 2.7 script for NAO interaction
import sys
from naoqi import ALProxy

def close_hand(ip, port, hand_name):
    motion_service = ALProxy("ALMotion", ip, port)
    motion_service.closeHand(hand_name)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python nao_interface.py <IP> <PORT> <HAND_NAME>")
        sys.exit(1)
    
    ip = sys.argv[1]
    port = int(sys.argv[2])
    hand_name = sys.argv[3]
    close_hand(ip, port, hand_name)
