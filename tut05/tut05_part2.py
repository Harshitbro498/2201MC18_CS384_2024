def check_balanced(s):
    stk = []
    match = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in match.values():
            stk.append(ch)
        elif ch in match:
            if stk and stk[-1] == match[ch]:
                stk.pop()
            else:
                return "The input string is NOT balanced."

    if not stk:
        return "The input string is balanced."
    else:
        return "The input string is NOT balanced."

s = input("Enter a string with parentheses: ")
print(check_balanced(s))
