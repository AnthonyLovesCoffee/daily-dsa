def validParenthesis(string):
    stack = [] 
    for c in string: 
        if c in '([{':
            stack.append(c) 
        else: 
            if not stack or \
                (c == ')' and stack[-1] != '(') or \
                (c == '}' and stack[-1] != '{') or \
                (c == ']' and stack[-1] != '['):
                return False 
            stack.pop()
    return not stack 

print(validParenthesis("[[}]]"))