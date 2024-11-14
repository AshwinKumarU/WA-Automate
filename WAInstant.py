import pywhatkit
import time

pywhatkit.sendwhatmsg_instantly('+919884319892','Sample message 1', wait_time=15, tab_close=True, close_time=3)
time.sleep(30)
pywhatkit.sendwhatmsg_instantly('+918778000401','Send sample message 2', wait_time=15, tab_close=True)
time.sleep(30)
pywhatkit.sendwhatmsg_instantly('+918148725764','Testing sample 1', wait_time=15, tab_close=True)
time.sleep(30)