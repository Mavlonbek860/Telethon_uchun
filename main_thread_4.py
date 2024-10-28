from threading import Thread
from time import sleep

def my_func_1():
    print("Worker-1 started!")
    sleep(1)
    print("Worker-1 finished!")

def my_func_2(main_thread):
    print("Worker-2 waiting worker-1 to finish!")
    main_thread.join()
    print("Worker-2 started!")
    sleep(1)
    print("Worker-2 done!")

worker1 = Thread(target=my_func_1)
worker2 = Thread(target=my_func_2, args=(worker1,))

worker1.start()
worker2.start()

for num in range(6):
    print("Main thread still working on task", num)
    sleep(0.60)

worker1.join()
print("Main thread completed!")