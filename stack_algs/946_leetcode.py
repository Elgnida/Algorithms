def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    stack = []
    j = 0
    for i in pushed:
        stack.append(i)
        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return print(bool(not stack))
                

validateStackSequences([1,2,3,4,5], [4,5,3,2,1])