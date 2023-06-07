#!/usr/bin/python3
def multiple_returns(sentence):
    j = None
    ts = ()

    for i in range(len(sentence)):
        j = i

    if j is None:
        return (0, None)

    ts = (j, sentence[0])
    return ts
