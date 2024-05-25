class PrefixNode:
  def __init__(self):
    self.chars = [None] * 26  # Pre-allocate space for lowercase alphabets (if applicable)
    self.count = 0  # Number of words ending at this node (including itself)

class PrefixTree:
  def __init__(self):
    self.root = PrefixNode()

  def insert(self, word):
    node = self.root
    for char in word:
      if not node.chars[ord(char) - ord('a')]:  # Efficient char lookup (assuming lowercase)
        node.chars[ord(char) - ord('a')] = PrefixNode()
      node = node.chars[ord(char) - ord('a')]
      node.count += 1  # Increment count at each node

  def search(self, prefix):
    node = self.root
    score = 0
    for char in prefix:
      if not node.chars[ord(char) - ord('a')]:
        return 0  # Prefix not found, early termination
      node = node.chars[ord(char) - ord('a')]
      score += node.count
    return score


class Solution(object):
    def sumPrefixScores(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        prefix_tree = PrefixTree()
        for word in words:
          prefix_tree.insert(word)

        result = [0] * len(words)
        for i, word in enumerate(words):
         result[i] = prefix_tree.search(word)
        return result