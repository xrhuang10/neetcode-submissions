class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(stack)
            if token == "+":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first + second)
        
            elif token == "-":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first - second)

            elif token == "*":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first * second)
        
            elif token == "/":
                second = int(stack.pop())
                first = int(stack.pop())
                stack.append(first / second)
            
            else:
                stack.append(int(token))

        return int(stack[-1])