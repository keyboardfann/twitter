#!/usr/bin/env python
import twitter
import argparse

#Setting up Twitter API
api = twitter.Api(
	consumer_key='x',
	consumer_secret='x',
	access_token_key='x',
	access_token_secret='x'
)

### For test
user="AShinOfficial"

### Get user's status
statuses = api.GetUserTimeline(screen_name=user)

for s in statuses:
 print s.user.screen_name + ' (' + s.created_at + ')'
 #Add the .encode to force encoding
 print s.text.encode('utf-8')
 print ''


### Get Following
print 'Get Following'
users = api.GetFriends()
for u in users:
 print u.screen_name
 print ''

## Get Friendship
print 'Get Friendship'
friend = api.LookupFriendship(screen_name=user)
print friend
print ''

## Get the user like tweets
print 'Get Favior'
favior = api.GetFavorites(screen_name=user)
print favior
print ''


## Get GetFollowerIDs
#print 'GetFollowerIDs'
#response = api.GetFollowerIDs(None)
#result += [x for x in data['fo']]
#print ''

### Get followers
#print 'Get followers'
#followers = api.GetFollowers(screen_name=user)
#for u in followers:
# print u.screen_name
# print ''

### Get Trend
print 'Japan trend'
trend = api.GetTrendsWoeid(id=1118129)
print trend
### If want to see detail article , use search to search the term

### Get User
#print 'Get user'
#getuser = api.GetUser(screen_name=user)
#print getuser
