class Twitter:

    def __init__(self):
        self.tweetsmap = {}
        self.followsmap = {}

        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetsmap:
            self.tweetsmap[userId] = []

        self.tweetsmap[userId].append([self.count, tweetId])
        self.count -= 1
    #each tweet is array of 3


    def getNewsFeed(self, userId: int) -> List[int]:
        #find userId in followsmap, return all followees, return all posts of all followees
        if userId not in self.followsmap:
            self.followsmap[userId] = set()
    
        self.followsmap[userId].add(userId)  # self-follow
        followees = self.followsmap[userId]

        #followees is an array of user Ids
        feed = []
        minHeap = []
        for followee in followees:
            if followee in self.tweetsmap:
                index = len(self.tweetsmap[followee]) - 1
                count, tweet = self.tweetsmap[followee][index]
                minHeap.append([count, tweet, followee, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(feed) < 10:
            count, tweet, followee, index = heapq.heappop(minHeap)
            feed.append(tweet)

            if index >= 0:
                count, tweet = self.tweetsmap[followee][index]
                heapq.heappush(minHeap, [count, tweet, followee, index - 1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        #1 will follow 2
        if followerId not in self.followsmap:
            self.followsmap[followerId] = set()

        self.followsmap[followerId].add(followeeId)

        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followsmap[followerId]:
            self.followsmap[followerId].remove(followeeId)
        
