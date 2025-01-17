# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        
        for i in range(len(expression)):
            oper = expression[i]
            if oper == "+" or oper == "-" or oper == "*":
                sub_str1 = expression[:i]
                sub_str2 = expression[i+1:]
                
                s1 = self.diffWaysToCompute(sub_str1)
                s2 = self.diffWaysToCompute(sub_str2)
                
                for i in s1:
                    for j in s2:
                        if oper == "*":
                            res.append(int(i) * int(j))
                        if oper == "+":
                            res.append(int(i) + int(j))
                        if oper == "-":
                            res.append(int(i) - int(j))
        
        if len(res) == 0:
            res.append(int(expression))
        
        return res