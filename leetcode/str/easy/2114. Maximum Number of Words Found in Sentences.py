class Solution
    #sentences parameter take a 'list' and expect an 'str'
    def mostWordsFound(self, sentences: List[str]) -> int:
        #This variable will keep track of the maximum number of words found in a single sentenc
        max_word_count = 0
        #iterate or repeat each 'sentence' in 'sentences list'
        for sentence in sentences:
            #splitting the sentence using split() and store in 'words' variable
            words = sentence.split()
            #we calculate the number of words in the 'sentence' by using len() on 'words' list and store in 'word_count' variable
            word_count = len(words)
            #comparing 'word_count' and 'max_word_count'
            #if 'word_count' is greater than 'max_word_count' we update max_word_count to the value of word_count
            # This ensures that max_word_count always holds the maximum number of words found in any sentence processed so far.
            if word_count > max_word_count:
                max_word_count = word_count

        return max_word_count
