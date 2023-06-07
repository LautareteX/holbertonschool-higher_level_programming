#!/usr/bin/python3
def multiple_returns(sentence):
    j = None

    for i in range(len(sentence)):
        j = i

    if j is None:
        return (0, None)

    return (j, sentence[0])
