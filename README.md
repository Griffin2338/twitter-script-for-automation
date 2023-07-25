# twitter-script-for-automation
Creating new photos according to twits of account.

The script designed to do the followings:

Retrieve tweets from a specified Twitter account using the twint library and save them to a CSV file named tweets.csv.
Process the tweets, remove specific characters and emojis, and replace certain strings with others.
Open a Photoshop file (PSD) and update a specific text layer in the PSD with the processed tweet text.
Use Google Image Crawler to download images related to the processed tweet.
Replace image placeholders in the PSD file with downloaded images and save the modified PSD as PNG files.
