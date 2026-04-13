class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # method stores the key, value, and timestamp into our key store
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp] )
    def get(self, key: str, timestamp: int) -> str:
        # method grabs the most recent value of the key and the most recent timestamp (if the key is less than or equal to the given timestamp)
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res