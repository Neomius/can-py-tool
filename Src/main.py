
import time
import can

bustype = 'socketcan_native'
channel = 'vcan0'

def producer(frameid):
    """:param id: Spam the bus with messages including the data id."""
    bus = can.interface.Bus(channel=channel, bustype=bustype)
    #for i in range(10):
    while True:
        msg = can.Message(arbitration_id=0xc0ffee, data=[frameid, 0, 0, 1, 3, 1, 4, 1], extended_id=False)
        bus.send(msg)
        time.sleep(0.01)
    # Issue #3: Need to keep running to ensure the writing threads stay alive. ?
    time.sleep(1)

producer(10)
