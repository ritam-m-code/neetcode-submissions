class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))

            if s in anagrams:
                anagrams[s].append(strs[i])
            else:
                anagrams[s] = [strs[i]]

        return list(anagrams.values())


        
            
        