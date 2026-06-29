class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        hand.sort()

        counter = Counter(hand)
        #print(counter)

        for num in hand:
            if not counter[num]:
                continue
            for i in range(num, num + groupSize):
                if not counter[i]:
                    #print(num, i, counter)
                    return False
                
                counter[i] -= 1
        
        
        return True

        