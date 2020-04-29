# final_project
I design a game of stroking the appropriate part of the kitten, using basic Mote Carlo simulation techniques to get statistical results and analyze.

Game description:
There are four poses for kittens, "sleep,sit,stand,all fours", and the corresponding scoring parts for each pose are different. For example, in "sit", the scoring parts are 'back', 'foot1', 'foot3', 'head'. And 'heart' representing user has touched scoring parts, while 'thunder' representing user hasn't touched correct part. The kitten switches its pose after being touched twice. The user gains more than 5 hearts to win the game. If a non-scoring part is encountered during the game, user will gain thunder, and when the number of thunder is more than 3,  the user fails.

I design three types of user, first one is general user who plays the game casually; second one is preferred user who has his/her own preference to touch the kitten. For example, some people like to touch the kitten's stomach all the time, while others like to touch its head. And third one is smart user who is good at previous result of the game, such as which part gains 'heart', and then he/she will try it in the later games.

I predict that the successful rate of smart user would be higher among these three types of user. After recording the winning rate of 10000 games, it turns out that my prediction is correct.


This project made me understand that I have to use my brain to play games in the future.
