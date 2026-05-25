class Twitter:

    def __init__(self):
        self.tweetsmap = {}
        self.followsmap = {}

        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetsmap:
            self.tweetsmap[userId] = []
        self.tweetsmap[userId].append([-1 * self.count, tweetId])
        self.count += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        if userId not in self.followsmap:
            self.followsmap[userId] = set()
        self.followsmap[userId].add(userId)

        
        for followee in self.followsmap[userId]:
            if followee in self.tweetsmap:
                for tweet in self.tweetsmap[followee]:
                    feed.append(tweet)

        heapq.heapify(feed)

        answer = []
        
        for i in range(10):
            if feed:
                count, post = heapq.heappop(feed)
                answer.append(post)
        return answer
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followsmap:
            self.followsmap[followerId] = set()
        self.followsmap[followerId].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followsmap and followeeId in self.followsmap[followerId]:
            self.followsmap[followerId].remove(followeeId)
        
