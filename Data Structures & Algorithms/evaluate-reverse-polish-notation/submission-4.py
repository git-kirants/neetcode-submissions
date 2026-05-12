class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = ["+", "-", "*", "/"]
        stack = []
        for ele in tokens:
            if ele not in ops:
                stack.append(int(ele))
        

            else:
                a = stack.pop()
                b = stack.pop()
            

                if ele == "+":
                    stack.append(b+a)
                elif ele == "-":
                    stack.append(b-a)
                elif ele == "*":
                    stack.append(b*a)
                else:
                    stack.append(int(b/a))

        
        return int(stack[-1])
                
                    

