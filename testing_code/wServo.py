import sys
import RPi.GPIO as GPIO
import time
grayScale = False
flipped = False
specialFx = False
GPIO.setmode(GPIO.BCM)
nasa =  sys.argv
duty = 0
#nasa = str(nasa)
nasa = "A1"
print(nasa)
GPIO.setup(23,GPIO.OUT)
servo1 = GPIO.PWM(23,50)
servo1.start(0)
servo1.ChangeDutyCycle(duty)
def A1():
    duty += 4
    servo1.ChangeDutyCycle(duty)
    print('ran A1')
def B2():
    duty -= 4
    servo1.ChangeDutyCycle(duty)
    print("ran B2")
def C3():
    print("ran C3")
def D4():
    grayScale = True
    print("ran D4")
def E5():
    grayScale = False
    print("ran E5")
def F6():
    flipped = True
    print("ran F6")
def G7():
    specialFx = True
    print("ran G7")
def H8():
    flipped = False
    grayScale = False
    specialFx = False
    print("ran H8")
FAIL = -1
def parser(string, keywords):
    transitions = {}
    outputs = {}
    fails = {}

    new_state = 0

    for keyword in keywords:
        state = 0

        for j, char in enumerate(keyword):
            res = transitions.get((state, char), FAIL)
            if res == FAIL:
                break
            state = res

        for char in keyword[j:]:
            new_state += 1
            transitions[(state, char)] = new_state
            state = new_state

        outputs[state] = [keyword]

    queue = []
    for (from_state, char), to_state in transitions.items():
        if from_state == 0 and to_state != 0:
            queue.append(to_state)
            fails[to_state] = 0

    while queue:
        r = queue.pop(0)
        for (from_state, char), to_state in transitions.items():
            if from_state == r:
                queue.append(to_state)
                state = fails[from_state]

                while True:
                    res = transitions.get((state, char), state and FAIL)
                    if res != FAIL:
                        break
                    state = fails[state]

                failure = transitions.get((state, char), state and FAIL)
                fails[to_state] = failure
                outputs.setdefault(to_state, []).extend(
                    outputs.get(failure, []))

    state = 0
    results = []
    for i, char in enumerate(string):
        while True:
            res = transitions.get((state, char), state and FAIL)
            if res != FAIL:
                state = res
                break
            state = fails[state]

        for match in outputs.get(state, ()):
            results.append(match)

    return results
matches = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8",]
parsed = parser(nasa, matches)

for x in parsed:
    if (x == "A1"):
        A1()
    elif (x == "B2"):
        B2()
    elif (x == "C3"):
        C3()
    elif (x == "D4"):
        D4()
    elif (x == "E5"):
        E5()
    elif (x == "F6"):
        F6()
    elif (x == "G7"):
        G7()
    elif (x == "H8"):
        H8()