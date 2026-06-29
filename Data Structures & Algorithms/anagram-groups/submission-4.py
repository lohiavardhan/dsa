class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = {}

        for string in strs:
            sorted_string = sorted(string)
            sorted_string = "".join(sorted_string)

            if sorted_string in answer_dict:
                answer_dict[sorted_string].append(string)
            else:
                answer_dict[sorted_string] = [string]
        
        answer_list = []
        for curr_key in answer_dict:
            answer_list.append(answer_dict[curr_key])

        return answer_list