#!/usr/bin/python3

from twython import TwythonStreamer
import sys

exec(open("/home/pi/scripts/TwKeys.py").read()) 

class MyStreamer(TwythonStreamer):
    msg_cnt = 0
    def on_success(self, data):
        
        if 'text' in data:
            self.msg_cnt = self.msg_cnt + 1
            print("Message Count = {}".format(self.msg_cnt))
        if self.msg_cnt == 3:
            print("Ian G. Harris is popular!")
            sys.exit()

 

stream = MyStreamer(CK, CS, AT, AS)
stream.statuses.filter(track='Ian G. Harris')

