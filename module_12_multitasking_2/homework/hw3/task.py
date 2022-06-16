import threading
import time

sem = threading.Semaphore()
run_event=threading.Event()
run_event.set()
def fun1(run_event):
    while run_event.is_set():

        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)

def fun2(run_event):
    while run_event.is_set():
        print(run_event)


        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)







t1 = threading.Thread(target = fun1,args = (run_event,))
t1.start()
t2 = threading.Thread(target = fun2,args = (run_event,))
t2.start()
try:
    time.sleep(500)
    print('ok')
except KeyboardInterrupt:
    run_event.clear()
    t1.join()
    t2.join()
    print('stop')




