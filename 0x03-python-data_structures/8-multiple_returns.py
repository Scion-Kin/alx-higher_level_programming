#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        count = len(sentence)
    else:
        count = 0
    return (count, sentence if not sentence else sentence[:1])
