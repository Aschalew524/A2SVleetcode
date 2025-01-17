# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {i: i for i in ascii_lowercase}

        def find(x):
            while x != parent[x]:
                x = find(parent[x])
            return x

        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            if x_root > y_root:
                parent[x_root] = y_root
            else:
                parent[y_root] = x_root

        for i in range(len(s1)):
            union(s1[i], s2[i])

        ans = ""
        for i in baseStr:
            ans += find(i)

        return ans