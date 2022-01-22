# O(n) - time
# O(n) - space
def balancedBrackets(string):
    push_chars = ['(', '[', '{']
    pop_chars = [')', ']', '}']
    pairs = list(zip(push_chars, pop_chars))
    stack = []
    for char in string:
        if char in push_chars:
            stack.append(char)
        elif char in pop_chars:
            if stack:
                popped_char = stack.pop()
                if (popped_char, char) not in list(pairs):
                    return False
            else:
                return False
    return len(stack) == 0
