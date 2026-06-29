class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False
        
        hashmap = {}
        hand.sort()

        for num in hand:
            hashmap[num] = hashmap.get(num, 0) + 1

        straights = len(hand) // groupSize

        required = 1
        keys = list(hashmap.keys())
        
        #print(required, maximum_freq)

        
        if len(keys) % 2 == 0:
            for i, num in enumerate(keys):
                if hashmap[num] != required:
                    #print(f'EVEN {i=}, {num=}, {required=}, {hashmap[num]=}')
                    return False
                
                if i == len(keys)/2 - 1:
                    continue
                elif i >= len(keys)/2 - 1:
                    required -= 1
                else:
                    required += 1
        else:
            for i, num in enumerate(keys):
                #print(f'ODD {i=}, {num=}, {required=}, {hashmap[num]=}, {len(keys)//2=}, {len(keys)//2+1=}, {len(keys)//2+2=}')
                if hashmap[num] != required:
                    return False
                
                if i + 1 == len(keys)//2 or i + 1 == len(keys)//2 + 1:
                    continue
                elif i + 1 > len(keys)//2+1:
                    required -= 1
                else:
                    required += 1
        
        return True
            





        return True