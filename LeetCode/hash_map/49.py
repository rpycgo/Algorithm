class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for string in strs:
            ordered_string = ''.join(sorted(string))
            if ordered_string not in group_anagrams:
                group_anagrams.update({ordered_string: [string]})
            else:
                group_anagrams[ordered_string].append(string)
        
        return list(group_anagrams.values())
