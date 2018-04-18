#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return
    else:
        first = sentence[0]
    return len(sentence), first
