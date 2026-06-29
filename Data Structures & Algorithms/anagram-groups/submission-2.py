class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_anagrams = {}

        for index, string in enumerate(strs):
            
            if "".join(sorted(string)) in list_anagrams:
                list_anagrams["".join(sorted(string))] = list_anagrams["".join(sorted(string))] + list([index])
            else:
                list_anagrams["".join(sorted(string))] = list([index])
            
            return list(list_anagrams.values)
            
        return_list = []
        for key in list_anagrams.keys():
            new_list = []
            for index in list_anagrams[key]:
                new_list.append(strs[index])
            
            return_list.append(new_list)


        return return_list

        