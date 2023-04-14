'''
author: Josh Huang
for testing, use this command: 
    python -c 'import radioParser; radioParser.test()'
'''
import sys
import time
import RPi.GPIO as GPIO
from buzzer import Buzzer

class RadioParser():
    
    def __init__(self):
        # self.commands = []
        self.buzzer = Buzzer()
        self.old = []
        print("radio parser initiated")
        self.prev_length = 0
        
    def parser(self, debug=False):
        try:
            self.buzzer.beep()
            self.buzzer.beep()
                        
            string = self.read_command(debug)
            
            starts = ["XX4XXX", "KC1RWU", "KQ4CTL-6"]
            if not [ele for ele in starts if(ele in string)]:
                print("callsign does not match")
                return []
            
            matches = []
            
            check = {'A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8'}
            for i in range(len(string)):
                if i+1 > len(string):
                    return matches
                elif str(string[i:i+2]) in check:
                    matches.append(string[i:i+2])
            
            # print(f"matches: {matches}")
            m = []
            if matches:
                m = [x for idx, x in enumerate(matches) if idx >= self.prev_length]
                # print(f"m: {m}")
                if m and m not in self.old:
                    self.old.append(m)
                    # print(f"old: {self.old}")
                    return m

            # print("matches: " + str(matches))
            self.prev_length = len(matches)
            return []
        
        except Exception as e:
            print(e)
            raise(e) # log the error with the established format
    
    def read_command(self, debug=False):
        path = "/home/pi/Desktop/logs/multimon.txt"
        if debug:
            path = "/home/pi/Desktop/BAGPIPER-FS-Payload/testing_code/multimon.txt"
        f = open(path,'r')
        command_raw = f.read()
        f.close()
        return command_raw
        
def test():
    # python -c 'import radioParser; radioParser.test()'
    r = RadioParser()
    while True:
        commands = r.parser(False)
        if commands:
            print(f"out: {commands}\n")
        time.sleep(5)


    
