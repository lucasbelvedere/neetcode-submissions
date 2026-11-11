'''
Input: a class "Twitter" with 5 functions
Output: Implement the functions

Init: Initializes the Twitter object, where we keep the main data structures.
PostTweet: Updates a map where the key is a userId and the value is a list of [time, tweetId] pairs. We can use a list since every tweetId is already unique.
GetNewsFeed: Fetches at most k = 10 of the most recent tweets from the user and the users they follow. A priority queue can do that.
Follow and Unfollow: Add/remove a followeeId to/from a map where the key is a followerId and the value is a set of all the userIds that user follows.

GetNewsFeed Time and Space Complexity:
Time Complexity: O(f + k log f), where f is the number of users this user follows and k = 10, since we fetch at most 10 posts. That gives O(f + 10 log f), which simplifies to O(f).
Space Complexity: O(f) extra space, since the following set and the heap each hold at most f entries.

Whole class:
Time Complexity: O(1) for postTweet, follow, and unfollow.
Space Complexity: O(T + F), where T is the total number of tweets stored in self.posts and F is the total number of follow relationships stored in self.follows.
'''

class Twitter:

    def __init__(self):
        self.time = 0 # real life scenario, use uuid7 for database efficiency
        self.follows = defaultdict(set)
        self.posts = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, priority_queue = [], []
        following = self.follows[userId] | {userId} # union operator for sets

        for user in following:
            posts = self.posts[user]
            if len(posts) > 0:
                i = len(posts) - 1
                most_recent_post = posts[i]
                # [time, tweetId, user, next index]
                priority_queue.append([most_recent_post[0], most_recent_post[1], user, i - 1])

        heapq.heapify(priority_queue)
        while priority_queue and len(res) < 10:
            post = heapq.heappop(priority_queue)
            res.append(post[1])
            if post[3] >= 0:
                next_post = self.posts[post[2]][post[3]]
                heapq.heappush(priority_queue, [next_post[0], next_post[1], post[2], post[3] - 1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

