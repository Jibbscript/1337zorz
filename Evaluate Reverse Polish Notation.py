class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "*": (lambda a, b: a * b),
            "/": (lambda a, b: a / b)
        }
        
        tkn_stack = []
        
        for tkn in tokens:
            if tkn in operators:
                arg2 = tkn_stack.pop()
                arg1 = tkn_stack.pop()
                result = operators[tkn](arg1, arg2)
                if tkn == "/":
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                tkn_stack.append(result)
            else:
                tkn_stack.append(int(tkn))
        
        return tkn_stack.pop()
