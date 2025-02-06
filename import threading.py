import threading
import time

def my_callback():
    print("Timer finished! Executing callback...")
    print("Timer started. Waiting for it to finish...")

def start_timer(seconds, callback):
    def my_sleep():
        
        
        for i in range (1,9): 
        print (i, "bateau-bateau")
        time.sleep(seconds)
        callback()
    
    thread = threading.Thread(target=my_sleep)
    thread.start()


start_timer(1, my_callback)