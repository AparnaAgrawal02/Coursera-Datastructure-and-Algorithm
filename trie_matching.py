# python3
import sys

NA = -1
def build_trie(patterns):
    tree = dict()
    tree[0]={}
    totalvert=0
    for string in patterns:
        t=0
        for i in range(len(string)):
            cusym=string[i]
        
            if cusym in tree[t]:
                t=tree[t][cusym]
    
            else:
                totalvert+=1
                tree[t][cusym]=totalvert
                t=totalvert
                tree[totalvert]={}



    # write your code here
    return tree

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def PrefixTrieMatching(text,trie):
	
	symbole=text[0]
	pattern=""
	i=0
	v=0
	while(1==1):

		if trie[v]=={}:
			return True
		elif trie[v]!={} and i < len(text):
			i+=1
			
			if symbole in trie[v] :
				v=trie[v][symbole]
				if i<len(text):
					symbole=text[i]
				else:
					symbole=""

			else:
				
				return False
		    
		else:
			return False



def TrieMatching(text,patterns):
	result = []
	trie=build_trie(patterns)
	k=0
	while k < len(text):
		if PrefixTrieMatching(text[k:], trie):
			result+=[k]
		k+=1
	return result
text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = TrieMatching (text,  patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
