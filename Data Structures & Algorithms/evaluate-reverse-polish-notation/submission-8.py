class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}

        stack = []
        for t in tokens:
            if t in operators:
                b, a = stack.pop(), stack.pop()

                print(f"a: {a}, b: {b}")
                match t:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case "/":
                        stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack[0]
