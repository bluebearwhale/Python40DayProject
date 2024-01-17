import threading
import time

def thread_1():
    while True:
        print("thread 1 operation")
        time.sleep(1.0)

t1=threading.Thread(target=thread_1)
#메인 코드가 동작할때만 동작하게 함
t1.daemon=True
t1.start()

while True:
    print("main operation")
    time.sleep(2.0)