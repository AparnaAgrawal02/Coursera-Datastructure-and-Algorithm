"""3 Problem: Extend TrieMatching
Problem Introduction
The goal in this problem is to extend the algorithm from the previous problem such that it will be able to
handle cases when one of the patterns is a prefix of another pattern. In this case, some patterns are spelled
in a trie by traversing a path from the root to an internal vertex, but not to a leaf.
Problem Description
Task. Extend TrieMatching algorithm so that it handles correctly cases when one of the patterns is a
prefix of another one.
Input Format. The first line of the input contains a string Text, the second line contains an integer 𝑛,
each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.
Constraints. 1 ≤ |Text| ≤ 10 000; 1 ≤ 𝑛 ≤ 5 000; 1 ≤ |𝑝𝑖
| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; all strings contain only
symbols A, C, G, T; it can be the case that 𝑝𝑖 is a prefix of 𝑝𝑗 for some 𝑖, 𝑗.
Output Format. All starting positions in Text where a string from Patterns appears as a substring in
increasing order (assuming that Text is a 0-based array of symbols). If more than one pattern
appears starting at position 𝑖, output 𝑖 once.
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
8
Sample 2.
Input:
ACATA
3
AT
A
AG
Output:
0 2 4
Explanation:
Text contains occurrences of A at positions 0, 2, and 4, as well as an occurrence of AT at position 2.
Note that the trie looks as follows in this case:
T G
A
When spelling Text from position 0, we don’t reach a leaf. Still, there is an occurrence of the pattern
A at this position.
Starter Files
The starter solutions for this problem read the input data from the standard input, pass it to a blank
procedure, and then write the result to the standard output. You are supposed to implement your algorithm
in this blank procedure if you are using C++, Java, or Python3. For other programming languages, you need
to implement a solution from scratch. Filename: trie_matching_extended
What To Do
To solve this problem, you may want to store in each node of the trie an additional flag indicating whether
the path from the root to this node spells a pattern.
"""




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
                
                
                if i == len(string)-1:
                    tree[t][cusym][1]=1
                t=tree[t][cusym][0]
    
            else:
                if i == len(string)-1:
                   x=1
                else:
                   x=-1
                totalvert+=1
                tree[t][cusym]=[totalvert,x]
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
	ans=0
	while(1==1):
		if trie[v]=={}:
			return True
		elif trie[v]!={} and i < len(text):
			i+=1
			
			if symbole in trie[v] :
				if trie[v][symbole][1] == 1:
					return True
				v=trie[v][symbole][0]
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
