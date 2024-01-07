def firstBadVersion(n: int) -> int:
    return binary_search(0, n)

def binary_search(self, low, high):
    if high == low:
        return high

    mid = (low + high) // 2

    if not isBadVersion(mid):
        return self.binary_search(mid + 1, high)
    else:
        return self.binary_search(low, mid)