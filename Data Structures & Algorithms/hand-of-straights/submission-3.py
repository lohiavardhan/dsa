class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False
        
        hand.sort()
        counter = Counter(hand)

        for i in range(len(hand)):
            if not counter[hand[i]]:
                continue
            
            for j in range(hand[i], groupSize + 1):
                
                if not counter[j]:
                    return False
                
                counter[j] -= 1
            
        
        return True