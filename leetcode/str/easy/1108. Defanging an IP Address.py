class Solution:
    #function named defandIPaddr. self is staple first parameter when using class. address: str is just means that address parameter will receive a string.
    def defangIPaddr(self, address: str) -> str:
        #.replace is a function that replace the target '.' into [.] basically, instead of using '.' here we use [.]
        return address.replace('.' , '[.]')