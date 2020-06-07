def bracketsMathcing(string):
    # create string to match open bracket in string
    openbrackets = "({["
    # create string to match close bracket in string
    closebrackets = ")}]"
    # create hash table to balance brackets open and close key values pairs
    matchbrackets = {")": "(", "}": "{", "]": "["}
    #create empty stack store openning brackets
    stack = []
    # loop through the input string
    for char in string:
        #check if it is open bracket
        if char in openbrackets:
            # insert into stack if true
            stack.append(char)
        # check if it is close bracket
        elif char in closebrackets:
            # check if stack is empty
            if len(stack) == 0:
                # if it is empty, this close brackets is unbalanced
                return False
            # check last item of stack is open bracket of this close bracket using hash table
            if stack[-1] == matchbrackets[char]:
                # if match, remove open bracket from stack
                stack.pop()
            # otherwise return false
            else:
                return False
    # check if stack is empty with open brackets
    return len(stack) == 0

print(bracketsMathcing("((({{{[[[]]]}}})))]"))

