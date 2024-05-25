class PrefixNode:
  def __init__(self):
    self.chars = {}  # Dictionary to store child nodes for each character
    self.count = 0  # Number of words ending at this node (including itself)

class PrefixTree:
  def __init__(self):
    self.root = PrefixNode()

  def insert(self, word):
    node = self.root
    for char in word:
      if char not in node.chars:
        node.chars[char] = PrefixNode()
      node = node.chars[char]
      node.count += 1  # Increment count at each node along the word

  def search(self, prefix):
    node = self.root
    score = 0
    for char in prefix:
      if char not in node.chars:
        return 0  # Prefix not found
      node = node.chars[char]
      score += node.count  # Add count of this node and all its children
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