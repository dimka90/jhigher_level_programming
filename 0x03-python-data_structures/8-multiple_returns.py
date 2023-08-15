#!/usr/bin/python3
def multiple_returns(sentence):
    tupple = ()
    if len(sentence) == 0:
        tupple = 0, "None"
    else:
        tupple = len(sentence), sentence[0]
    return tupple
