class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(stack)
            if token == "+" or token == "-" or token == "*" or token == "/":
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "+":
                    stack.append(first + second)
            
                elif token == "-":
                    stack.append(first - second)

                elif token == "*":
                    stack.append(first * second)
            
                elif token == "/" and second != 0:
                    stack.append(first / second)
                
                else:
                    return -999999
            
            else:
                stack.append(int(token))

        return int(stack[-1])