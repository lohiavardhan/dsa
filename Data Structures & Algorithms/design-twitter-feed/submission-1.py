class Twitter:

    def __init__(self):
        self.dictionary = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.dictionary[userId].append(-tweetId)
        heapq.heapify(self.dictionary[userId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        answer = []

        while self.dictionary[userId]:
            answer.append(heapq.heappop(self.dictionary[userId]))

        print(answer)
        self.dictionary[userId] = answer
        heapq.heapify(self.dictionary[userId])

        answer = [-n for n in answer]
        return answer

        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        for item in self.dictionary[followeeId]:
            self.dictionary[followerId].append(item)
        
        heapq.heapify(self.dictionary[followerId])
        

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        for item in self.dictionary[followeeId]:
            if item in self.dictionary[followerId]:
                self.dictionary[followerId].remove(item)

        heapq.heapify(self.dictionary[followerId])
