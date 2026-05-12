class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        stack = []

        for i, temp in enumerate(temperatures):
            
            while stack and temp > stack[-1][1]:
                index , temperature = stack.pop()
                output.append([i-index, index])

            stack.append((i, temp))

        
        while stack:
            index, temp = stack.pop()
            output.append([0, index])
            
        output.sort(key=lambda x: x[1])
        
        return [x[0] for x in output]