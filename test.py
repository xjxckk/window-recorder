
from DXcam import Recording
from time import sleep

recording = Recording('Startpage - Google Chrome')
print('Starting')
recording.start(filename='test')
sleep(3)
print('Stopping')
recording.stop()
# sleep(3)