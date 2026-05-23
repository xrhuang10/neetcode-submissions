class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(second) + int(first))
            elif token == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) - int(second))
            elif token == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(second) * int(first))
            elif token == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) / int(second))
            else:
                stack.append(token)

        return int(stack[-1])