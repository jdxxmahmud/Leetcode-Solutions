class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        res = []

        vowels = "aeiou"

        prefix_db = [[0, False] for _ in range(len(words) + 1)]

        for idx, word in enumerate(words):
            prefix_db[idx + 1][0] = prefix_db[idx][0]
            
            if word[0] in vowels and word[-1] in vowels:
                prefix_db[idx + 1][1] = True
                prefix_db[idx + 1][0] += 1

        for query in queries:
            if prefix_db[query[0] + 1][1] and prefix_db[query[1] + 1][1]:
                res.append(prefix_db[query[1] + 1][0] - prefix_db[query[0] + 1][0] + 1)
            else:
                res.append(prefix_db[query[1] + 1][0] - prefix_db[query[0]][0])
        return res
