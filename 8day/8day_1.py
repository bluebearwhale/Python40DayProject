import threading
from datetime import datetime
def sum(name,value):
    for i in range(0,value):
        print(datetime.now())
        print(f'{name} : {i}')

t1=threading.Thread(target=sum,args=('thread number 1',10))
t2=threading.Thread(target=sum,args=('thread number 2',10))

t1.start()
t2.start()

print("main Thread operation")