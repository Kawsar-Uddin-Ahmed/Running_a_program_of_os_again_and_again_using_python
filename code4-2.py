import os
import schedule
import time
import threading
def starting():
        m = open("ap4-2.bat","w")
        n = m.write("calc")
        m.close()
        os.system("ap4-2.bat")
        threading.Timer(10,starting).start() #It will recall from inside the function means it is recursion

#starting()
#OR
if __name__ == '__main__':
        starting()