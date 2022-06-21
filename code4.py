import os
import schedule
import time
import threading
def starting():
        m = open("ap4.bat","w")
        n = m.write("calc")
        m.close()
        os.system("ap4.bat")

#a = schedule.every().day.at("23:10").do(starting)
schedule.every().day.at("22:43").do(starting) #This will execute first at the mentioned time and then the while(1) loop
while(1):
    schedule.run_pending()  # Run all jobs that are scheduled to run
    time.sleep(1)
    threading.Timer(7200,starting).start() #It will run the program every after 2 hours