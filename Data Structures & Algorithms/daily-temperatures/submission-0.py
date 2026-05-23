class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp_s = [0]

        for i in range(1, len(temperatures)):
            while temp_s and temperatures[i] > temperatures[temp_s[-1]]:
                last_t_i = temp_s.pop()
                res[last_t_i] = i - last_t_i
            temp_s.append(i)
        
        return res