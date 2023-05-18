import time

print("Press Enter to begin, Press Ctrl + C to Stop")

while True:
    try:
        input()
        starttime=time.time()
        print("started")
        while True:
            print("Time Elapsed: ", round(time.time() - starttime, 0), "secs", end="\r")
            time.sleep(1)  # 1 second delay
    except KeyboardInterrupt:
        print("Stopped")
        endtime = time.time()
        print("Total Time:", round(endtime - starttime, 2), "secs")
        break
    
            



