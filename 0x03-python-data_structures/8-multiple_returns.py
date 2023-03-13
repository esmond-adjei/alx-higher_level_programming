#!/usr/bin/python3
def multiple_returns(sentence):
    sent_len = len(sentence)
    first_char = sentence[0] if sent_len else None
    return len(sentence), first_char
