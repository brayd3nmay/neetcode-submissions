class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+":
                    res = stack.pop() + stack.pop()
                    stack.append(res)
                case "-":
                    b, a = stack.pop(), stack.pop()
                    res = a - b
                    stack.append(res)
                case "*":
                    res = stack.pop() * stack.pop()
                    stack.append(res)
                case "/":
                    b, a = stack.pop(), stack.pop()
                    res = int (a / b)
                    stack.append(res)
                case _: # digit
                    stack.append(int(t))
        return stack[0]