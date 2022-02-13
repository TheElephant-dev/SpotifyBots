
<p align="center">
   Spotify Automatic Song Listeners 
</p>

# Disclaimer
This project was made for Educational Use only. i do not condone these scripts being used to commit any malicious or fraudulent action.

# Configuration&usage
Setup on multible files is required for optimal results.

## Stage #1: "Bot Accounts":
In `Accounts.js` file:
- you must provide valid spotify account login credentials. Examples will be shown inside the file, or:
  - Email: `Emailiastro@sambasnailmail.com` <----- Example Email
  - Password: `My1st_passWordy%Pass&wor0` <----- Example password
  - ProxyIP: `86.46.169.12` <----- Example Proxy IP
- https://smailpro.com/ could be provide temporary GMAIL email recievers for spotify account creation.


## Stage #2: "Notifications":
### This stage is optional, but recommended.
In `\libs\EmailSender.py` you can provide valid gmail login credentials.
Can be used to recieve phone notifications when an account fails to log in.(likely detected as a bot) to be replaced by you.


## Stage #3: "Songs":
In `\libs\SongPoolFuncitons.py` you must provide song\track links for the bots to Listen to.

## Stage #4: "Bot Setup":
### This stage is optional, but recommended.
In `SpotifyBotExecutor.py` you may want to change
- `ChangeSongEvery_X_Seconds = 7200` <----- to the number of seconds each bot will wait before switching to a different song. (a single spotify "listen" requires a minimum of ~ a minute)
- `ChangeShiftEvery_X_Seconds = 43200` <----- to change the amount of time each "listener" will stay active on spotify for before shutting down\switching.
- `AmountOfBotsToRun = 1` <----- the default amount of bots to run. (you will be asked anyway once you run the script.)


## Stage #5: "ChromeDriver":
Make sure you have the proper version of "<a href="https://chromedriver.chromium.org/downloads" target="_blank">chromedriver</a>" based on your version of chrome (can be seen from the image below)

<p align="center">
   <img src="readmeimages\GetChromeVersion.png">
</p>
   
   
   







