class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        word = []
        maxlength = 0
        for ch in s:
            if ch in word:
                maxlength = max(maxlength, len(word))
                word = word[word.index(ch)+1:]
                
            word.append(ch)
        maxlength = max(maxlength, len(word))
        return maxlength