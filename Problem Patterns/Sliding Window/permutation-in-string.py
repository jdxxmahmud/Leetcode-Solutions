# Problem Link: https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Hash = Counter(s1)

        left, right = 0, 0

        charLeft = len(s1)

        temp = {char: 0 for char in s1Hash.keys()}
        
        print(s1Hash)
        print(charLeft, temp)


        while right < len(s2):

            currChar = s2[right] 

            if currChar in s1Hash:
                if temp[currChar] < s1Hash[currChar]:
                    temp[currChar] += 1
                    charLeft -= 1
                else:
                    while s2[left] != currChar:
                        if s2[left] in temp and temp[s2[left]] > 0:
                            temp[s2[left]] -= 1
                            charLeft += 1

                        left += 1

                    left += 1
            else:
                while left < right:

                    leftChar = s2[left]

                    if leftChar in temp and temp[leftChar] > 0:
                        temp[leftChar] -= 1
                        charLeft += 1

                    left += 1

            print(charLeft, temp)
            
            if charLeft == 0:
                return True

            right += 1

        return False
