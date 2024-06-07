class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)
        words = sentence.split()
        replaced_words = []
        for word in words:
            shortest_root = next((root for root in root_set if word.startswith(root)), word)
            replaced_words.append(shortest_root)
        return " ".join(replaced_words)
