# SW_miniproject
This project implements Twitter and Google APIs to determine if a twitter user is a bot, pull the user's latest tweets, and determine the sentiment of the user based on his/her tweets. We implemented the backend in python because there were many helpful examples online and the syntax was more familiar to us that other options. For the front end, a HTML page was made where the user can input a twitter handle, which is then saved as a javascript vaiable. The twitter handle is then passed to, and returned from, the python backend using flask since it is the simplest way to interact with the python script.

## Front End
The front end is presented in HTML but uses underlying JavaScript and AJAX to accept and proccess inputs from the user. When a user inputs a Twitter handle, AJAX posts the value to a Flask backend function that uses the value as a variable for Botometer and Google's API. JavaScript will later receive the values returned by Flask and display them on a second webpage, separating the output from Botometer and from Google's NLP service. No error checking is currently present but the APIs will both fail if an unavailable Twitter handle is passed.

### User Experience
Our app contains a text box where the user can input a twitter handle and a button for the user to click to submit. The user will then see the account's overall bot score as well as subscores for fake followers, self declared bots, manually labelled bots, spammer bots, financial bot, and other Bots. Each score ranges from 0-5 with higher scores indicating bot-like behavior. The accounts primary language and conditional bot probability (the percentage of accounts that are bots given an overall score at least as high as the user's score) are also displayed. Next, the account's latest tweets, timestamps, and numnber of retweets are displayed. Additionally, the average sentiment, magnitude-weighted average sentiment, average magnitude, average retweets, and percent originality of the tweets are all displayed. Finally, the app combines all the data to provide an overall impression of the account.

### Pictures
#### Homepage
![2022-09-25_14h56_26](https://user-images.githubusercontent.com/75260880/192160521-846e64c6-2ac3-42be-ab1a-6280d5c193ae.png)

#### Results Page Mock-Up
![testcase 1](https://user-images.githubusercontent.com/75260880/192161595-4a4d9df5-8b58-47ce-8d76-2715092a519e.png)

### Video
#### Colab backend simulation (using @wbz)
https://user-images.githubusercontent.com/75260880/192161054-b888022f-ae53-4b23-ad7a-3032e02057c1.mp4

#### Colab backend simulation (using @BU_tweets)
https://user-images.githubusercontent.com/75260880/192162377-eb17f3b4-8904-4757-b914-e62a0dc085c3.mp4

## Backend
The backend was written in python and consisted of a call to the Twitter botometer API to determine if the user is a bot, the Twitter API to pull user tweets, and the Google NLP API to determine sentiment.

For the Flask [8] aspect of the backend, the Python file awaits the screen name to be passed from JavaScript. From there a function takes the screen name and converts it to a string to be recognized by the APIs.

### Twitter Botometer
We connected to the Twitter botometer [1] used the RapidAPI. We used the python API call given in the botometer documentation [2] to pass the account's screen name into the botometer and receive the account's overall bot score as well as subscores for fake followers, self declared bots, manually labelled bots, spammer bots, financial bot, and other Bots. Each score ranges from 0-5 with higher scores indicating bot-like behavior. The accounts primary language and conditional bot probability (the percentage of accounts that are bots given an overall score at least as high as the user's score) are also returned.

### Pulling Tweets
We pull the user's last 10 tweets using Twitter's tweepy python library. We consulted sources [3,4] to understand how to call the API. We then displayed the tweets, the time stamp of the tweet, and the number of retweets each tweet recieved.

### Google NLP Sentiment Analysis
The user's tweets are passed to Google's Clound Natural Language Processer [5]. We used the documented call to the API [6]. Since no direct python call was given, we took the cUrl call and passed it through an online cUrl to python translater [7]. For each tweet, we stored the sentiment score (how positive/negative the tweet is) the magnitude (how much sentiment is conveyed), the number of retweets it got, and whether the tweet itself was a retweet. We then calculated the average sentiment score (between -1 and 1, where the more positive the score the more positive the tweet), the average sentiment score weighted by tweet magnitude (also between -1 and 1), the average tweet magnitude (between 0 and inf, where the larger the value the more sentiment is expressed), the average number of retweets that the user got from original tweets, and the percentage of the user's tweets that are original. 

### Overall User Impression
We used the data gathered to comment on the user's bot probability, positivity, emotionality, influence, and originality.

| Overall Bot Score | Bot Probability Label |
|-------------------|-----------------------|
| 0.9 < score       | DEFINATELY A BOT      |
| 0.7 < score < 0.9 | MAYBE A BOT           |
| 0.5 < score < 0.7 | LIKELY NOT A BOT      |
|       score < 0.5 | NOT A BOT             |

| Average Sentiment Score | Positivity Label |
|-------------------------|------------------|
|  0.5 < score            | VERY POSITIVE    |
|    0 < score <  0.5     | POSITIVE         |
| -0.5 < score <  0       | NEGATIVE         |
|        score < -0.5     | VERY NEGATIVE    |

| Magnitude Score | Emotionality Label |
|-----------------|--------------------|
| 1 < score       | EMOTIONAL TONE     |
|     score < 1   | NEUTRAL TONE       |

| Average Retweet Score | Influence Label |
|-----------------------|-----------------|
| 20 < score            | INFLUENTIAL     |
|     score < 20        | NOT INFLUENTIAL |

| % Original Tweets Score | Originality Label      |
|-------------------------|------------------------|
| 75% < score             | ORIGINAL TWEETS        |
| 50% < score < 75%       | MOSTLY ORIGINAL TWEETS |
| 25% < score < 50%       | SOME ORIGINAL TWEETS   |
|       score < 25%       | MOSTLY RETWEETS        |

## Further Work
Unfortunately, we did not have the time to perform error checking so the app will not work if you enter an incorrect twitter handle. Additionally, we did not have time to determine the main topics that an account tweets about. Finally, the functions to properly receive and convert the JavaScript input to a Python variable are as of yet incomplete.

## Sources
1. https://botometer.osome.iu.edu/
2. https://github.com/IUNetSci/botometer-python
3. https://medium.com/mlearning-ai/how-to-get-tweets-by-python-and-twitter-api-2022-a440c635c3ac
4. https://github.com/mehranshakarami/AI_Spectrum/tree/main/2022/Twitter_API
5. https://cloud.google.com/natural-language
6. https://cloud.google.com/natural-language/docs/reference/rest/v1beta2/documents/analyzeSentiment?hl=en_US&apix_params=%7B%22resource%22%3A%7B%22document%22%3A%7B%22content%22%3A%22sgjlkjklnglrk%22%2C%22type%22%3A%22PLAIN_TEXT%22%7D%7D%7D
7. https://www.scrapingbee.com/curl-converter/python/
8. https://pythongeeks.org/python-flask-introduction/
