class Solution:
    #command parameter takes a str and expect a return of str
    def interpret(self, command: str) -> str:
        #variable with a empty str value where we put the incrementation
        interpreted_output = ""
        #we need to iterate or repeat the str of the parameter command also by using (len) we can see the length of each str
        for inter in range(len(command)):
            #we are trying to see the index of (inter) whether it has a str equal to 'G' if yes, then increment 'G' to an empty variable
            if command[inter] == 'G':
                interpreted_output += 'G'
            #check the index of (index) whether it has '('
            elif command[inter] == '(':
                #If the next character (command[inter + 1]) is a closing parenthesis ')', we interpret it as the string 'o'
                #In this case, we add or concatenate the string 'o' to the interpreted_output string using +=.
                #Additionally, we increment the inter variable by 1 to skip the closing parenthesis since it has been interpreted.
                if command[inter + 1] == ')':
                    interpreted_output += 'o'
                    inter += 1
                #If the next three characters (command[inter + 1:inter + 4]) are 'al)', we interpret it as the string 'al'.
                #In this case, we add or concatenate the string 'al' to the interpreted_output string.
                #Additionally, we increment the inter variable by 3 to skip the closing parenthesis and the characters 'a' and 'l' since they have been interpreted.
                elif command [inter + 1:inter + 4] == 'al)':
                    interpreted_output += 'al'
                    inter += 3

        return interpreted_output

