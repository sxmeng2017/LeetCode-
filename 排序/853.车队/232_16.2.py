class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        load = sorted(zip(position, speed))
        count = 0
        times = [float(target - p)/s for (p, s) in load]
        while len(times) > 1:
            first = times.pop()
            if times[-1] > first:
                count += 1
            else:
                times[-1] = first
        return count + bool(times)