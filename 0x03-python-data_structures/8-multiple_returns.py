#!/usr/bin/python3
def multiple_returns(sentence):
    len_ = len(sentence)
    if len_ == 0 or sentence is None:
        return 0, None
    else:
        return len_, sentence[0]
