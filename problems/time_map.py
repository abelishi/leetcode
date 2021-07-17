from typing import List

class TimeMap:
    def __init__(self) -> None:
        self.time_map = dict()
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_map.__contains__(key):
            self.time_map[key].append(timestamp, value)
        else:
            self.time_map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        return
            