def isAnagram(s: str, t: str) -> bool:
    return get_letters(s) == get_letters(t)

def get_letters(s: str):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d