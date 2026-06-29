class Twitter:

    def __init__(self):
        self.dictionary = defaultdict(list)
        self.follow_dict = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.dictionary[userId].append(-tweetId)
        heapq.heapify(self.dictionary[userId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []

        for item in self.dictionary[userId]:
            res.append(item)
        
        for following in self.follow_dict[userId]:
            for item in self.dictionary[following]:
                res.append(item)
        
        heapq.heapify(res)

        answer = []
        while res:
            answer.append(-heapq.heappop(res))
        
        return answer[:10]

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followeeId not in self.follow_dict[followerId]:
            self.follow_dict[followerId].append(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId and followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)