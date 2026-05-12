class TimeMap:

    def __init__(self):
        self.time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time:
            self.time[key] = {}
        if timestamp not in self.time[key]:
            self.time[key][timestamp] = []
        self.time[key][timestamp].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time:
            return ""
        
        seen = 0

        for time in self.time[key]:
            if time <= timestamp:
                seen = max(seen, time)
        
        return "" if seen == 0 else self.time[key][seen][-1]
