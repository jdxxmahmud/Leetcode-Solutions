class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        hashTable = Counter(arr)
        
        sortedHash = dict(sorted(hashTable.items(), key= lambda item: item[1]))

        removedElement = 0

        for val in sortedHash.values():
            if k >= val:
                k -= val
                removedElement += 1
            else:
                break

        return len(sortedHash) - removedElement

        return 0
