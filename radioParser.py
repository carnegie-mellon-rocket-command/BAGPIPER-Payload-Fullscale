import sys
import time

class RadioParser():
    received = False
    cmd_lst = []
    commands = []
    
    
    def __init__(self):
        print("radio parser initiated")
        
    def receive(self):
        '''
        Received the commands by listening to radio
        Once commands received and verified will set received to true and update commands list
        '''
        self.cmd_lst = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8"]
        
    def parser(self, debug=False):
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
        if matches and matches not in self.commands:
            self.commands.append(matches)
            
        return self.commands
    
    def read_command(self, debug=False):
        path = "../logs/multimon.txt"
        if debug:
            path = "testing_code/multimon.txt"
        f = open(path,'r')
        command_raw = f.read()
        f.close()
        return command_raw
        
    
    
r = RadioParser()
print(r.parser(True))
