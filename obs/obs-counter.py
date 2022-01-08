import time 
from datetime import datetime


def countdown(t): 
    while True:
        if t >= 0:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
        else:
            mins, secs = divmod(-t, 60)
            timer = '- {:02d}:{:02d}'.format(mins, secs)

        now = datetime.now()
        current_time = now.strftime("%H:%M")

        f = open("a.txt", "w")
        f.write("{}\n  -\n{}".format(current_time, timer))
        f.close()

        time.sleep(1) 
        t -= 1

countdown(1800)
