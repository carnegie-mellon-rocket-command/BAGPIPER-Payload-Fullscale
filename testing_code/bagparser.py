#!/usr/bin/env python3

import sys
import time

import payload

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

def main():
    grayScale = False
    flipped = False
    special_fx = False

    nasa =  sys.argv
    matches = ["A1", "B2", "C3", "D4", "E5", "F6", "G7", "H8",]
    parsed = parser(nasa, matches)

    bagpiper = payload.Payload()

    for x in parsed:
        if (x == "A1"):
            bagpiper.rot_left()

        elif (x == "B2"):
            bagpiper.rot_right()

        elif (x == "C3"):
            bagpiper.take_pic()

        elif (x == "D4"):
            greyscale = True

        elif (x == "E5"):
            greyscale = False

        elif (x == "F6"):
            flipped = not flipped

        elif (x == "G7"):
            special_fx = True

        elif (x == "H8"):
            special_fx = False

if __name__ == '__main__':
   main()
