GrowTweet
=========

It's a small project for Growbots recruitment.

### Descripton

It is a simple application which uses Twitter API. It allows users to see their “second line” followers, in other words - followers, of their followers.

## Common scenario:
- I go to “/” page
- I see “Connect Twitter account” button
- I press “Connect Twitter account” button
- I see Twitter popup, I follow oAuth flow authorizing app
- I get redirected to “/followers/followers” page
- There is AJAX request to the server and after a while we get table with data
- I see a list of my “2nd line” followers. Each contains
- A Twitter handle, like “@madonna”
- A number of my followers, that this person follows (example, Bob and Rick follow me, Andrew follows both of them, the number is 2). 

### API

API details can be viewed under URL `/api/`. Special library called Swagger handles it. 

**1. get-followers**
A browser calls AJAX request under URL `/getfollowers/`. It takes new 'followers of my followers' data from Twitter server via the Twitter's API.
For the call some variables are taken from the browsers session.

**2. current-followers**
URL request under `/currentfollowers/{user_name}/` with GET method returns JSON data with the latest 'followers of my followers' for the user_name.



