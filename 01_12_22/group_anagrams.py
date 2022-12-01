class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        finlist=[]
        mydict={}
        for a in strs:
            key=''.join(sorted(a))
            if key in mydict:
                mydict[key] = mydict[key] + [a]
            else:
                mydict[key]=[a]
        for value in mydict.values():
            finlist.append(value)
        return finlist