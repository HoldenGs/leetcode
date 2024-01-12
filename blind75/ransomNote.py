from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag_counts = Counter(magazine)
    note_counts = Counter(ransomNote)
    
    return not note_counts - mag_counts