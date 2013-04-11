import encrypt as encrypt
import cProfile, pstats
import decrypt3 as decrypt3
import sys

ciphertext = encrypt.encrypt(sys.argv[1])


cProfile.run('wordlist = decrypt3.read_words()', 'rundata')
result = decrypt3.decrypt3(ciphertext,wordlist)

# check results
if sys.argv[1] not in result:
	print("BAD"*100)

p = pstats.Stats('rundata')
p.sort_stats('cumulative').print_stats(10)


#cProfile.run('decrypt3.decrypt3(a,wordlist)', 'rundata')
#p = pstats.Stats('rundata')
#p.sort_stats('cumulative').print_stats(10)