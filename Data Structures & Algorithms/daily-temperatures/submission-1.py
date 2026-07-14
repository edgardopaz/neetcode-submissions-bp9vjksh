class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for idx, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                old_idx = stack.pop()[1]
                res[old_idx] = idx - old_idx
            stack.append([val, idx])
        
        while stack:
            res[stack.pop()[1]] = 0
        
        return res


