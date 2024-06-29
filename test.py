
from window-recorder import Recorder
from time import sleep

recorder = Recorder('Startpage - Google Chrome')
print('Starting')
recorder.start(filename='test')
sleep(3)
print('Stopping')
recorder.stop()