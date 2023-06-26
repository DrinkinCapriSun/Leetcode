class Solution:
    #here we see that operations is expected to be a list
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        #giving a value to x that will be use later to increment and decrement
        x = 0
        #we used for loop here because we need to iterate or repeating each elemenet in the list which is this "Input: operations = ["--X","X++","X++"]" here we see multiple input
        for num in operations:
            #just giving conditions to the input
            if num == "++X":
                #if condition is true, incremement the x variable
                x += 1
            elif num == "X++":
                x += 1
            elif num == "--X":
                x -= 1
                #if condition is false, decrement the x variable
            else:
                x -= 1
        #PAY ATTENTION!! pay attention to the indention of each code, took me alot of time to fix the problem, the problem was return wasn't indented right
        #here it means that for loop iterates or repeat through all operations first before returning or stopping
        return x



