class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][1]:
                index , temperature = stack.pop()
                output.append([i-index, index])
                res[index] = i-index

            stack.append((i, temp))

        return res