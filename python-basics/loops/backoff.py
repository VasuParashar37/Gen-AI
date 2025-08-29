import time
attempts = 1
max_attempts = 5
wait_time = 1

while attempts<=max_attempts:
    print("Attempts:",attempts,"\t","Wait time:",wait_time,"Seconds")
    attempts+=1
    time.sleep(wait_time)
    wait_time*=2
