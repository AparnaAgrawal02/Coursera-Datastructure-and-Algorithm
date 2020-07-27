"""1 Problem: Construct a Trie from a Collection of Patterns
Problem Introduction
Reads will form a collection of strings Patterns that we wish to match against a reference genome Text. For
each string in Patterns, we will first find all its exact matches as a substring of Text (or conclude that it
does not appear in Text). When hunting for the cause of a genetic disorder, we can immediately eliminate
from consideration areas of the reference genome where exact matches occur.
Multiple Pattern Matching Problem: Find all occurrences of a collection of patterns in a
text.
Input: A string Text and a collection Patterns containing (shorter) strings.
Output: All starting positions in Text where a string from Patterns appears as a substring.
To solve this problem, we will consolidate Patterns into a directed tree called a trie (pronounced “try”),
which is written Trie(Patterns) and has the following properties.
∙ The trie has a single root node with indegree 0, denoted root.
∙ Each edge of Trie(Patterns) is labeled with a letter of the alphabet.
∙ Edges leading out of a given node have distinct labels.
∙ Every string in Patterns is spelled out by concatenating the letters along some path from the root
downward.
∙ Every path from the root to a leaf, or node with outdegree 0, spells a string from Patterns.
The most obvious way to construct Trie(Patterns) is by iteratively adding each string from Patterns to the
growing trie, as implemented by the following algorithm.
TrieConstruction(Patterns)
Trie ← a graph consisting of a single node root
for each string Pattern in Patterns:
currentNode ← root
for 𝑖 from 0 to |Pattern| − 1:
currentSymbol ← Pattern[𝑖]
if there is an outgoing edge from currentNode with label currentSymbol:
currentNode ← ending node of this edge
else:
add a new node newNode to Trie
add a new edge from currentNode to newNode with label currentSymbol
currentNode ← newNode
return Trie
Problem Description
Task. Construct a trie from a collection of patterns.
Input Format. An integer 𝑛 and a collection of strings Patterns = {𝑝1, . . . , 𝑝𝑛} (each string is given on a
separate line).
Constraints. 1 ≤ 𝑛 ≤ 100; 1 ≤ |𝑝𝑖
| ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; 𝑝𝑖
’s contain only symbols A, C, G, T; no 𝑝𝑖
is
a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.
3
Output Format. The adjacency list corresponding to Trie(Patterns), in the following format. If
Trie(Patterns) has 𝑛 nodes, first label the root with 0 and then label the remaining nodes with the
integers 1 through 𝑛−1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be
encoded by a triple: the first two members of the triple must be the integers 𝑖, 𝑗 labeling the initial and
terminal nodes of the edge, respectively; the third member of the triple must be the symbol 𝑐 labeling
the edge; output each such triple in the format u->v:c (with no spaces) on a separate line.
Time Limits.
language C C++ Java Python C# Haskell JavaScript Ruby Scala
time in seconds 0.5 0.5 2 2 0.75 1 2 2 4
Memory Limit. 512Mb.
Sample 1.
Input:
1
ATA
Output:
0->1:A
2->3:A
1->2:T
Explanation:
0
1
2
3
A
T
A
Sample 2.
Input:
3
AT
AG
AC
Output:
0->1:A
1->4:C
1->3:G
1->2:T
Explanation:
0
1
2
T
3
G
4
C
A
4
Sample 3.
Input:
3
ATAGA
ATC
GAT
Output:
0->1:A
1->2:T
2->3:A
3->4:G
4->5:A
2->6:C
0->7:G
7->8:A
8->9:T
Explanation:
0
1
2
3
4
5
A
G
A
6
C
T
A
7
8
9
T
A
G
Starter Files
The starter solutions for this problem read the input data from the standard input, pass it to a blank
procedure, and then write the result to the standard output. You are supposed to implement your algorithm
in this blank procedure if you are using C++, Java, or Python3. For other programming languages, you need
to implement a solution from scratch. Filename: trie
What To Do
To solve this problem, it is enough to implement carefully the corresponding algorithm covered in the lectures."""




#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    
    tree = build_trie(patterns)
    print(tree)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
