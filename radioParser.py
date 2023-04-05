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
        self.commands = []
        self.buzzer = Buzzer()
        print("radio parser initiated")
        
    def parser(self, debug=False):
        try:
            self.buzzer.beep()
            self.buzzer.beep()
            
            string = self.read_command(debug)
            
            starts = ["XX4XXX", "KC1RWU"]
            if not [ele for ele in starts if(ele in string)]:
                return self.commands
            
            matches = []
            check = {'A1', 'B2', 'C3', 'D4', 'E5', 'F6', 'G7', 'H8'}
            for i in range(len(string)):
                if i+1 > len(string):
                    return matches
                elif str(string[i:i+2]) in check:
                    matches.append(string[i:i+2])
            
            print("matches: " + str(matches))
            
            more_matches = True
            # old_cmds = [cmd for command_lst in self.commands for command in cmd_lst]
            old_cmds = []
            for sublist in self.commands:
                for item in sublist:
                    old_cmds.append(item)
            for i in range(len(old_cmds)):
                if i < len(matches):
                    if old_cmds[:i] != matches[:i]:
                        self.commands.append(matches[i:])
                        more_matches = False
            
            new_match_cnt = len(matches) - len(old_cmds)
            if new_match_cnt > 0 and more_matches:
                print("more matches")
                self.commands.append(matches[len(old_cmds):])
            
            return self.commands
        
        except Exception as e:
            raise(e) # log the error with the established format
    
    def read_command(self, debug=False):
        path = "/home/pi/Desktop/logs/multimon.txt"
        if debug:
            path = "testing_code/multimon.txt"
        f = open(path,'r')
        command_raw = f.read()
        f.close()
        return command_raw
        
def test():
    r = RadioParser()
    while True:
        commands = r.parser(True)
        print(f"out: {commands}")
        time.sleep(5)


    