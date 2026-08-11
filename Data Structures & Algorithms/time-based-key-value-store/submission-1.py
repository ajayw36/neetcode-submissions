import bisect
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list) # String key --> [(int time, String value), ...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.time_map[key]
        i = bisect.bisect_right(arr, (timestamp, 'z'))
        if i == 0:
            return ''
        return arr[i-1][1]
