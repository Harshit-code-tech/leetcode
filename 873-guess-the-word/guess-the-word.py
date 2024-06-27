# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def countMatching(worda,wordb):
            return sum(map(lambda index: 1 if worda[index]==wordb[index] else 0, range(len(worda))))
        possibles = set(words)
        while len(possibles):
            nextWord = possibles.pop()
            result = master.guess(nextWord)
            if result == 6:
                return nextWord
            possibles = set(filter(lambda word:countMatching(nextWord,word)==result, possibles))