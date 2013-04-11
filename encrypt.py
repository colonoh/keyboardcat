def encrypt(plaintext):
  print("Plaintext is", plaintext)
  # map my fingers to potential keys
  a = {'a': 'aqz', 's': 'swx', 'd': 'de', 'f': 'bcfgrtv', 'j': 'hjmnuy', 'k': 'ik', 'l': 'lo', ';': "p'", ' ': ' '}
  result = ''
  for letter in plaintext:
    for key,value in a.items():
      if letter in value:
        result = result + key
  return result

if __name__ == "__main__":
  import sys
  result = encrypt(sys.argv[1])
  print(result)
  #return result
