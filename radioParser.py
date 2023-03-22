import sys
import time
import RPi.GPIO as GPIO

class RadioParser():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    
    def __init__(self):
        self.commands = []
        print("radio parser initiated")
        
    def parser(self, debug=False):
        try:
            self.beep()
            self.beep()
            
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
            
            # if matches and matches not in self.commands:
            #     self.commands.append(matches)
            tmp = []
            commands_copy = self.commands
            for matched_cmd in matches:
                tmp.append(matched_cmd)
                for lst in self.commands:
                    # print(lst)
                    if lst == tmp:
                        tmp = []                        
               
            if tmp and tmp not in self.commands:         
                self.commands.append(tmp)
            
            return self.commands
        
        except Exception as e:
            with open("aaaaaaa.txt", 'w') as loggg:
                loggg.write(str(e))
            print(str(e))
            self.beep()
    
    def read_command(self, debug=False):
        path = "/home/pi/Desktop/logs/multimon.txt"
        if debug:
            path = "testing_code/multimon.txt"
        f = open(path,'r')
        command_raw = f.read()
        f.close()
        return command_raw
    
    def beep(self):
        GPIO.output(21, GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(21, GPIO.LOW)
        time.sleep(.2)
        
    
def test():
    r = RadioParser()
    while True:
        commands = r.parser()
        print(f"out: {commands}")
        time.sleep(5)

    