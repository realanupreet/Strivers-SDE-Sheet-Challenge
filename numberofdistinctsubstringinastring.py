class TrieNode: 
   def __init__(self):
       self.links = {}
  
def countDistinctSubstrings(s):
   # Write your code here
   
#------------------BRUTE------------------
#     st = set()
   
#     for i in range(0, len(s)):
#         word = ""
#         for j in range(i, len(s)):
#             word += s[j]
#             st.add(word)
#     return len(st)+1





#------------------OPTIMAL------------------
   root = TrieNode()
   cnt = 1


   for i in range(0,len(s)):
       node = root
       for j in range(i, len(s)): 
           v= s[j]
           if not v in node.links:
               node.links[v] = TrieNode()
               cnt+=1
           node = node.links[v]
   
   return cnt