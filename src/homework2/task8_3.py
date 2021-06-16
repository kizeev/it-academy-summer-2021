# Shortest Word
# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.


def find_short(s):
    text1 = s.split()
    min_text = s
    for i in text1:
        if len(i) < len(min_text):
            min_text = i
    len_text = len(min_text)
    return len_text
