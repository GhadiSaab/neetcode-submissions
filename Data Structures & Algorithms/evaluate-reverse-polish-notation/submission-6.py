class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','*','-','/'}
        for i in tokens:
            if i in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                match i:
                    case '+':
                        stack.append(num1 + num2)
                    case '-':
                        stack.append(num1 - num2)
                    case '/':
                        stack.append(num1 / num2) 
                    case '*':
                        stack.append(num1 * num2)
            else:
                stack.append(i)
                
        return int(stack.pop())
