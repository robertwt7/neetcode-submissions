class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_s = []

        for i, t in enumerate(temperatures):
            while temp_s and t > temperatures[temp_s[-1]]:
                last_i = temp_s.pop()
                res[last_i] = i - last_i
            temp_s.append(i)

        return res