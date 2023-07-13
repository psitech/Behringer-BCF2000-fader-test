# https://mido.readthedocs.io/en/latest/index.html
# https://www.w3schools.com/python/default.asp

import mido
import time

midi_out = mido.open_output('BCF2000 1')

while True:
    for C in range(0x51, 0x59):
        midi_out.send(mido.Message('control_change', channel = 0, control = C, value = 0x7F))        
        time.sleep(0.03)
    for C in range(0x51, 0x59):
        midi_out.send(mido.Message('control_change', channel = 0, control = C, value = 0x00))     
        time.sleep(0.03)

midi_out.close()
