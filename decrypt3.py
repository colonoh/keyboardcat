# nodes in the trie are dict{letter, link to next node}
class Trie:
  # trie node deliminter 
  _end = '_end_'
  _head_node = dict()
  
  # add a word the trie
  def add(self, word):
    current_node = self._head_node
    for letter in word:
      # if the letter exists, refer to the node it points to, otherwise, add it and refer to an empty node (dict)
      current_node = current_node.setdefault(letter, dict())
    #(current_node.setdefault(letter,dict()) for letter in word)
    # no moar letters, end of word, put a end thingy on it
    current_node = current_node.setdefault(self._end, self._end)
   
  # see if a word is in the trie
  def __contains__(self, word):
    current_node = self._head_node
    for letter in word:
      if letter in current_node:
        current_node = current_node[letter]
      else:
        return False
    # if we're at the end of a word
    if self._end in current_node:
      return True
    else:
      return False

  # has doesn't care if it's the whole word or not
  def has(self, word):
    current_node = self._head_node
    for letter in word:
      if letter in current_node:
        current_node = current_node[letter]
      else:
        return False
    return True



def decrypt3(ciphertext, wordlist):
  print("Ciphertext is", ciphertext)
  a = {'a': 'aqz', 's': 'swx', 'd': 'de', 'f': 'bcfgrtv', 'j': 'hjmnuy', 'k': 'ik', 'l': 'lo', ';': "p'"}

  #ciphertext = 'dad'
  #ciphertext = 'djfkjddfkjflj'

  # initate the candidates list with the expansion of the first ciphertext letter
  candidates = list(a[ciphertext[0]])
  for letter in ciphertext[1:]:
    # take every candidate and create a new canidate appended with a new letter, one for every new letter
    candidates2 = []
    for single_candidate in candidates:
      for x in a[letter]:
        y = single_candidate + x
        if wordlist.has(y):
          candidates2.append(y)
    candidates = candidates2

  # temporary final check, get rid of incomplete words
  for candidate in candidates:
    if candidate not in wordlist:
      candidates.remove(candidate)
  print("Result is", candidates)
  return candidates
  
def read_words():
  wordlist = Trie()
  wordfile = open('wordlist.txt', 'r', encoding='utf-8')
  # add the words from the dictionary to the trie
  #for line in wordfile:
  with open(r'wordlist.txt') as f:
    for line in f:
      wordlist.add(str(line).strip().lower())
    # get rid of newlines and force lowercase
    #line = str(line).strip().lower()
    #wordlist.add(str(line).strip().lower())
  #[wordlist.add(str(line).strip().lower()) for line in wordfile]
  wordfile.close()
  print("Wordlist created.")
  return wordlist
