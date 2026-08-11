class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for ch in tokens:
            if ch in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                if ch == '+':
                    stack.append(num1 + num2)
                elif ch == '-':
                    stack.append(num1 - num2)
                elif ch == '*':
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))

            else:
                stack.append(int(ch))
        
        return stack.pop()
