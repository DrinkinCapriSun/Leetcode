class Solution:
    # jewels and stones expect an string
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #where we add the increment
        count = 0
        #use for loop to iterate or repeat the (Input: jewels = "aA", stones = "aAAbbbb") and check each letters
        for jew in jewels:
            for sto in stones:
                #if statement to compare each letters of jew and sto
                if sto == jew:
                    #if true, increment the count variable
                    count += 1
        #return to count, pay attention to indention
        return count