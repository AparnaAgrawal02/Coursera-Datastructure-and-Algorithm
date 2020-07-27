"""2 Problem: Implement TrieMatching
Problem Introduction
Given a string Text and Trie(Patterns), we can quickly check whether any string from Patterns matches a
prefix of Text. To do so, we start reading symbols from the beginning of Text and see what string these
symbols “spell” as we proceed along the path downward from the root of the trie, as illustrated in the
pseudocode below. For each new symbol in Text, if we encounter this symbol along an edge leading down
from the present node, then we continue along this edge; otherwise, we stop and conclude that no string in
Patterns matches a prefix of Text. If we make it all the way to a leaf, then the pattern spelled out by this
path matches a prefix of Text.
This algorithm is called PrefixTrieMatching.
PrefixTrieMatching(Text, Trie)
symbol ← first letter of Text
𝑣 ← root of Trie
while forever:
if 𝑣 is a leaf in Trie:
return the pattern spelled by the path from the root to 𝑣
else if there is an edge (𝑣, 𝑤) in Trie labeled by symbol:
symbol ← next letter of Text
𝑣 ← 𝑤
else:
output “no matches found”
return
PrefixTrieMatching finds whether any strings in Patterns match a prefix of Text. To find whether any
strings in Patterns match a substring of Text starting at position 𝑘, we chop off the first 𝑘 − 1 symbols from
Text and run PrefixTrieMatching on the shortened string. As a result, to solve the Multiple Pattern
Matching Problem, we simply iterate PrefixTrieMatching |Text| times, chopping the first symbol off of
Text before each new iteration.
TrieMatching(Text, Trie)
while Text is nonempty:
PrefixTrieMatching(Text, Trie)
remove first symbol from Text
Note that in practice there is no need to actually chop the first 𝑘 − 1 symbols of Text. Instead, we just read
Text from the 𝑘-th symbol.
Problem Description
Task. Implement TrieMatching algorithm.
Input Format. The first line of the input contains a string Text, the second line contains an integer 𝑛,
each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.
Constraints. 1 ≤ |Text| ≤ 10 000; 1 ≤ 𝑛 ≤ 5 000; 1 ≤ |𝑝𝑖
| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; all strings contain only
symbols A, C, G, T; no 𝑝𝑖
is a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.
Output Format. All starting positions in Text where a string from Patterns appears as a substring in
increasing order (assuming that Text is a 0-based array of symbols).
6
Time Limits.
language C C++ Java Python C# Haskell JavaScript Ruby Scala
time in seconds 1 1 3 7 1.5 2 7 7 6
Memory Limit. 512Mb.
Sample 1.
Input:
AAA
1
AA
Output:
0 1
Explanation:
The pattern AA appears at positions 0 and 1. Note that these two occurrences of the pattern overlap.
Sample 2.
Input:
AA
1
T
Output:
Explanation:
There are no occurrences of the pattern in the text.
Sample 3.
Input:
AATCGGGTTCAATCGGGGT
2
ATCG
GGGT
Output:
1 4 11 15
Explanation:
The pattern ATCG appears at positions 1 and 11, the pattern GGGT appears at positions 4 and 15.
Starter Files
The starter solutions for this problem read the input data from the standard input, pass it to a blank
procedure, and then write the result to the standard output. You are supposed to implement your algorithm
in this blank procedure if you are using C++, Java, or Python3. For other programming languages, you need
to implement a solution from scratch. Filename: trie_matching
What To Do
To solve this problem, it is enough to implement carefully the corresponding algorithm covered in the lectures."""





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
