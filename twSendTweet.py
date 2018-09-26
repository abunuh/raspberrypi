#!/usr/bin/python3

from twython import Twython

exec(open("/home/pi/scripts/TwKeys.py").read()) 

api = Twython(CK, CS, AT, AS)

api.update_status(status="BOT Test 4 of 3 for Ian G. Harris Coursera IOT course")

