# Problem Link: https://leetcode.com/problems/bag-of-tokens
# March 3, 2024

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        left, right = 0, len(tokens) - 1

        while left <= right:
            
            if left == right:
                if power >= tokens[left]:       
                    score += 1
                    power -= tokens[left]
                    break
                else:
                    break

            if tokens[left] < power:
                score += 1
                power -= tokens[left]
                left += 1
            elif score > 0:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break

        return score

        
