import threading,time
import random

number1 = random.randint(1,30)
def light():
    if not event.isSet(): #If no Event
        event.set() #the wait state not blocking Green #
    count = 0
    while True: 
        if count < 10:
            print("\033[42;1m--green light on--\033[0m")
        elif count <13:
            print("\033[43;1m--yellow light on --\033[0m")
        elif count <20:
            if event.isSet():
                event.clear()
            print("\033[41;1m--red light on--\033[0m")
        elif count < number1:
            print("\033[42;1m--EMERGENCY--\033[0m")
            print("\033[42;1m--EMERGENCY VEHICLE PASSING--\033[0m")
            print("\033[42;1m--ALL CARS STOP--\033[0m")
        else:
            count = 0
            event.set() #playing the green light to
        time.sleep(1)
        count +=1
'''
def emergency_vehicle(n): #flawed thread
        while 1:
            if not event.isSet() and count < number1:
                print("emergency vehicle [%s] is passing" %n)
                print("car [%s] is waiting for the red light.." %n)
                event.wait()
'''


def car(n):    #no bug version
    while 1:
        time.sleep(1) #let the car slowly if event.isSet(): #Green 
        if event.isSet(): #Green 
            print("car [%s] is running.." %n) 
        else:
            print("car [%s] is waiting for the red light.." %n)
            event.wait() #constantly checks flag has not been set, if not set waiting, the waiting time is an input event, can be accurate to a millisecond 

if __name__ == "__main__":
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        #te = threading.Thread(target=emergency_vehicle,args=(i,))
        
        t.start()
       # te.start()
        

    