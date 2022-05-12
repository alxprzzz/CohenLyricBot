# @CohenLyricBot 

![CohenLyricBot](https://user-images.githubusercontent.com/102554461/167990557-c794e46e-a0ce-4d8c-849e-2c38048e4354.png)

This LyricBot posts rearranged lyrics by Leonard Cohen every 12 hours on Twitter. Cohen is a hugely influential poet, novelist, musician, and lyricist with a career that spanned nearly 50 years. Cohen had an illustrious career, with his most popular song “Hallelujah” having been covered over 300 times since its release in 1985.

I initially gathered data about Cohen using an API by LyricGenius, which included many elements of metadata I didn’t need– including his biography, who performed his covers, and his spoken word albums. After I made a few other requests and included a list of words to exclude in my parameters, I received over 217 Kilobytes of data (instead of the 7 Megabytes I had initially gotten) that still included metadata which made it difficult to extra just the lyrics. 

I decided to follow a different path by web scraping lyric data from the fan website, The Leonard Cohen Files using BeautifulSoup. This worked well for me as I was able to better specify which data I wanted, which ended up being 184 Kilobytes of lyrics and song titles. I further cleaned up the data by extracting just the lyrics, removing white spaces, and split the lyrics in preparation for them to be posted on Twitter. 

In my final Python file, I used the random and Tweepy libraries in order to randomize and tweet the lyrics. All files were then uploaded to AWS Lambda, where it is scheduled to tweet rearranged lyrics from 15 of Cohen’s albums every 12 hours. 


![darkercard1](https://user-images.githubusercontent.com/102554461/167990534-f7c4a8ae-e7b9-40c8-a215-9a264b79f118.jpeg)

