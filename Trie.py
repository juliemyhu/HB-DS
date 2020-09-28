class TrieNode(object):
  def __init__(self):
    self.children = {} # key = character, value = a different TrieNode
    self.is_final = False # a boolean (is it the end of some word ive entered)

  def add_child(self, character):
    if character not in self.children:
        self.children[character] = TrieNode() 

  def get_next(self, character):
    if character in self.children:  
      return self.children[character]
    else:
      return None

  def set_final(self):
    self.is_final = True

class Trie(object):
  def __init__(self):
      self.root = TrieNode()
  
  def add_word(self, word):
    current = self.root
    for letter in word:
        current.add_child(letter)
        current = current.get_next(letter)
    current.set_final()
       
  def contains_word(self, word): # true or false if there is a path from root to the right node
    current = self.root
    for letter in word:
      current = current.get_next(letter)
      if current is None:
        return False
    return current.is_final
