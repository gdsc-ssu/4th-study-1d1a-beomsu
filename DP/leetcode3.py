"""
- substring 중에서 제일 길이가 긴 녀석을 찾아야함.
- 찾아야하는 substring은 abc 순으로 나열된 녀석임.

- 아스키 코드 값으로 확인해보기
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str_list=[]
        ret=0
        for cursor in range(len(s)):
            count_dict={s[cursor]:1}
            for move in range(cursor+1,len(s)):
                if count_dict.get(s[move],False):
                    sub_str_list.append(''.join(count_dict.keys()))
                    break
                else:
                    count_dict[s[move]]=1
                    
            sub_str_list.append(''.join(count_dict.keys()))
        
        
        #Find the longest substring
        if len(sub_str_list) !=0: 
            ret=len(max(sub_str_list,key=lambda x: len(x)))
        
        return ret