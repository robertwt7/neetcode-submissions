import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack: [1,2], found operand, pop 2, 1 + 2, put in stack, then iterate again, push to stack, found operand then pop 2
        stack = []

        for t in tokens:
            try:
                stack.append(int(t))
            except Exception as e:
                right = int(stack.pop())
                left = int(stack.pop())
                if t == '+':
                    stack.append(left + right)
                elif t == '*':
                    stack.append(left * right)
                elif t == '-':
                    stack.append(left - right)
                elif t == '/':
                    res = left / right
                    if res < 0:
                        stack.append(math.ceil(res))
                    else:
                        stack.append(math.floor(res))

        return stack[0]