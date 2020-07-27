"""4 Problem: Construct the Suffix Tree of a String
Problem Introduction
Storing Trie(Patterns) requires a great deal of memory. So let’s process Text into a data structure instead.
Our goal is to compare each string in Patterns against Text without needing to traverse Text from beginning
to end. In more familiar terms, instead of packing Patterns onto a bus and riding the long distance down
Text, our new data structure will be able to “teleport” each string in Patterns directly to its occurrences in
Text.
A suffix trie, denoted SuffixTrie(Text), is the trie formed from all suffixes of Text. From now on, we
append the dollar-sign (“$”) to Text in order to mark the end of Text. We will also label each leaf of the
resulting trie by the starting position of the suffix whose path through the trie ends at this leaf (using 0-based
indexing). This way, when we arrive at a leaf, we will immediately know where this suffix came from in Text.
However, the runtime and memory required to construct SuffixTrie(Text) are both equal to the combined
length of all suffixes in Text. There are |Text| suffixes of Text, ranging in length from 1 to |Text| and having
total length |Text| ·(|Text| + 1)/2, which is Θ(|Text|
2
). Thus, we need to reduce both the construction time
and memory requirements of suffix tries to make them practical.
Let’s not give up hope on suffix tries. We can reduce the number of edges in SuffixTrie(Text) by combining the edges on any non-branching path into a single edge. We then label this edge with the concatenation
of symbols on the consolidated edges. The resulting data structure is called a suffix tree, written SuffixTree(Text).
To match a single Pattern to Text, we thread Pattern into SuffixTree(Text) by the same process used for
a suffix trie. Similarly to the suffix trie, we can use the leaf labels to find starting positions of successfully
matched patterns.
Suffix trees save memory because they do not need to store concatenated edge labels from each nonbranching path. For example, a suffix tree does not need ten bytes to store the edge labeled “mabananas$”
in SuffixTree(“panamabananas$”); instead, it suffices to store a pointer to position 4 of “panamabananas$”,
as well as the length of “mabananas$”. Furthermore, suffix trees can be constructed in linear time, without
having to first construct the suffix trie! We will not ask you to implement this fast suffix tree construction
algorithm because it is quite complex.
Problem Description
Task. Construct the suffix tree of a string.
Input Format. A string Text ending with a “$” symbol.
Constraints. 1 ≤ |Text| ≤ 5 000; except for the last symbol, Text contains symbols A, C, G, T only.
Output Format. The strings labeling the edges of SuffixTree(Text) in any order.
Time Limits.
language C C++ Java Python C# Haskell JavaScript Ruby Scala
time in seconds 1 1 3 10 1.5 2 10 10 6
Memory Limit. 512Mb.
10
Sample 1.
Input:
A$
Output:
A$
$
Explanation:
1 0
$ A$
Sample 2.
Input:
ACA$
Output:
$
A
$
CA$
CA$
Explanation:
3 1
2 0
$ A CA$
$ CA$
11
Sample 3.
Input:
ATAAATG$
Output:
AAATG$
G$
T
ATG$
TG$
A
A
AAATG$
G$
T
G$
$
Explanation:
2 3 4 0
1 5
7 6
A
A T
T
ATG$ TG$ G$ AAATG$
AAATG$ G$
$ G$
Starter Files
The starter solutions for this problem read the input data from the standard input, pass it to a blank
procedure, and then write the result to the standard output. You are supposed to implement your algorithm
in this blank procedure if you are using C++, Java, or Python3. For other programming languages, you need
to implement a solution from scratch. Filename: suffix_tree
What To Do
You can construct a trie from all the suffixes of the initial string as in the first problem. Then you can
“compress” it into the suffix tree by deleting all nodes of the trie with only one child, merging the incoming
and the outgoing edge of such node into one edge, concatenating the edge labels. However, if you do this
and also store the substrings as edge labels directly, this will be too slow and also use too much memory.
Use the hint from the lecture to only store the pair (start, length) of the substring of text corresponding
to the edge label instead of storing this substring itself. Also note that when you create an edge from a
node to a leaf of the tree, you don’t need to go through the whole substring corresponding to this edge
character-by-character, you already know the start and the length of the corresponding substring. If it’s still
too slow, you’ll need to build the suffix tree directly without building the suffix trie first. To do that, you’ll
need to do almost the same, but creating the nodes only when branching happens by breaking the existing
edge in the middle.

"""





# python3
import sys
sys.setrecursionlimit(11000)
class SuffixTree(object):
  class Node(object):
    def __init__(self,	lab):
      self.lab	=	lab	#	label	on	path	leading	to	this	node
      self.out	=	{}  #	outgoing	edges;	maps	characters	to	nodes
      
  def __init__(self,	s):
	
    self.root=self.Node(None)
    self.root.out[s[0]]	= self.Node(s)	#	trie	for	just	longest	suf
								#	add	the	rest	of	the	suffixes,	from	longest	to	shortest
    for	i	in range(1,	len(s)):#	start	at	root;	we’ll	walk	down	as	far	as	we	can	go
      cur	= self.root
      j=i
      while(j<len(s)):
        if	s[j]	in	cur.out:
          child	=	cur.out[s[j]]
          lab	=	child.lab
          #	Walk	along	edge	until	we	exhaust	edge	label	or
          #	until	we	mismatch
          k	=	j+1
          while	k-j	< len(lab)	and	s[k]	==	lab[k-j]:
            k	+= 1
          if	k-j	== len(lab):
            cur	=	child	#	we	exhausted	the	edge
          
            j	=	k
          else:
            #	we	fell	off	in	middle	of	edge
            cExist,	cNew	=	lab[k-j],	s[k]
              #	create	“mid”:	new	node	bisecting	edge
            mid	= self.Node(lab[:k-j])
            mid.out[cNew]	= self.Node(s[k:])
            #	original	child	becomes	mid’s	child
            mid.out[cExist]	=	child
            #	original	child’s	label	is	curtailed
            child.lab	=	lab[k-j:]
            #	mid	becomes	new	child	of	original	parent
            cur.out[s[j]]	=	mid
            
        else:
          #	Fell	off	tree	at	a	node:	make	new	edge	hanging	off	it
          cur.out[s[j]]	= self.Node(s[j:])

def recursion(st,result,j):
  result.append(j.lab)
  for r in j.out:
    
    recursion(st,result,j.out[r])
def build_suffix_tree(text):
  result=[]
  st=SuffixTree(text)
  for i in st.root.out:
    recursion(st,result,st.root.out[i])

  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))
