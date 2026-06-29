from collections import defaultdict
import heapq
from typing import List

class Twitter:
    def __init__(self):
        self.tweets = defaultdict(list)        # userId -> list of (time, tweetId)
        self.follows = defaultdict(set)        # followerId -> set of followeeIds
        self.time = 0                          # global timestamp

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1                         # decreasing so "most recent" is smallest
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        # include self + followees
        users = [userId] + list(self.follows[userId])

        for u in users:
            arr = self.tweets[u]
            if arr:
                idx = len(arr) - 1 
                t, tid = arr[idx]
                heapq.heappush(heap, (t, tid, u, idx - 1))

        res = []
        while heap and len(res) < 10:
            t, tid, u, idx = heapq.heappop(heap)
            res.append(tid)
            if idx >= 0:
                nt, ntid = self.tweets[u][idx]
                heapq.heappush(heap, (nt, ntid, u, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
