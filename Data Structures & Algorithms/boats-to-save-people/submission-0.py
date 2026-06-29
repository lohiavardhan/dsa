class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()

        l = 0
        r = len(people) - 1
        answer = 0
        visited = set()

        for l in range(len(people)):
            if l in visited:
                continue
            

            while r > l and ((people[l] + people[r] > limit) or (r in visited)):
                
                r -= 1
            
            print(f'{l=}, {r=}, {people[l]=}, {people[r]=}, {limit=}, {visited=}, {answer=}')
            
            answer += 1
            visited.add(l)
            visited.add(r)
            r = len(people) - 1

            print(visited)


        return answer