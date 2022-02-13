

import selenium
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import selenium.common.exceptions as SeleniumError

import random
from time import sleep


from libs import SongPoolFuncitons as SP
from libs import EmailSender







class BotInstence():
    def __init__(self, BotID: int = 999, BotChromeDriverPath: str = 'MissingChromeDriverPath', BotAccountUsername: str = 'Unknown@Username.com', BotAccountPassword: str = 'UnknownPassword', AltBotAccountUsername: str = 'AltUnknown@Username.com', AltBotAccountPassword: str = 'AltUnknownPassword', BotProxyServerIP: str = '0.0.0.0:0'):
        self.alive = False
        self.ID = BotID
        self.ChromeDriverPath = BotChromeDriverPath

        self.AccountUsername = BotAccountUsername
        self.AltAccountUsername = AltBotAccountUsername
        self.AccountPassword = BotAccountPassword
        self.AltAccountPassword = AltBotAccountPassword
        self.AltMode = False
        print(f'\nBot #{self.ID} Info:\n  AccountUsername = "{self.AccountUsername}" & "{self.AltAccountUsername}"\n  AccountPassword = "{self.AccountPassword}" & "{self.AltAccountPassword}"')

        self.ProxyServerIP = BotProxyServerIP
        self.LoggedIn = False

        # Start Browser
        self.chrome_options = webdriver.ChromeOptions()
        # self.chrome_options.add_argument("--mute-audio")
        # self.chrome_options.add_argument("--version")
        # self.chrome_options.add_argument("--detachDriver(True)")
        # self.chrome_options.add_argument("--start-maximized")
        #self.chrome_options.add_argument("--headless")
        #self.chrome_options.add_argument( f'--proxy-server={self.ProxyServerIP}')  # Set the Proxy Argument for the browser to run in.

        self.DesiredCaps = DesiredCapabilities().CHROME
        # self.DesiredCaps["pageLoadStrategy"] = "normal"  #  Waits for full page load
        self.DesiredCaps["pageLoadStrategy"] = "eager"  # Do not wait for full page load

        self.browser = None # added upon birth
        self.wait = None # added upon birth






        #Initial Actions
    def Birth(self):
        self.alive = True

        print(f'Spawning a browser for bot #{self.ID}')
        self.browser = webdriver.Chrome(self.ChromeDriverPath, desired_capabilities=self.DesiredCaps, options=self.chrome_options)  # Run the browser, and with chrome options above.
        self.wait = WebDriverWait(self.browser, 10)  # set the timeout of "waits" to X mas seconds.
        self.browser.get('https://spotify.com/login') # go to the spotify login page. (to preload and cache the page before login)

        # Browser Visuals
        self.browser.set_window_size(800, 700)  # Set window Size  - only effect visuals
        self.browser.set_window_position(50 + (30 * int(self.ID)), 50 + ((30 * int(self.ID)) / 2))  # move window slightly down and to the right - only effect visuals
        self.browser.execute_script("document.body.style.zoom='60%'")  # Set window ZOOM size to 60%  - only effect visuals

    def Kill(self):
        print(f'Killing Bot #{self.ID} being {self.browser} . . . ', end='')
        self.browser.quit()
        print('Dead.')
        self.alive = False






    def Login(self):
        print(f'-Bot Num #{self.ID} Trying to login with {self.AccountUsername}...', end='')
        self.browser.get('https://spotify.com/login') # go to the spotify login page.

        self.wait.until(EC.visibility_of_element_located((By.ID, "login-button")))  # wait untill the "login" button is clickable.
        self.wait.until(EC.element_to_be_clickable((By.ID, "login-button"))) #wait untill the "login" button is visible

        self.browser.find_element_by_id("login-username").send_keys(self.AccountUsername) # Fill in Email\username
        self.browser.find_element_by_name("password").send_keys(self.AccountPassword) # Fill in Password
        self.browser.find_element_by_id("login-button").click() # Click the "login" button

        try:
            WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@ng-if="response.error"]'))) # wait for X seconds max until you find an error while logging in.
            ErrorElement = self.browser.find_element_by_xpath('//*[@ng-if="response.error"]').text # Grab the text error.
            print(f'-Bot Num #{self.ID} Login Error: "{ErrorElement}"\n     >With Email: "{self.AccountUsername}"\n       >And password: "{self.AccountPassword}"')
            EmailSender.Send(Title='Bot Login Failed!', MailContent=f'Greetings Mike,\n-Bot Num #{self.ID} Login Error: "{ErrorElement}"\n     >With Email: "{self.AccountUsername}"\n       >And password: "{self.AccountPassword}"\n Failed to login.')
            self.Kill()

        except SeleniumError.TimeoutException:
            print(f'-Bot Num #{self.ID} Loggged in!') # announce that the bot logged in!
            return True



    def GetRidOfCookiesPopup(self):
        if self.alive == False:
            return 'DeadBot'
        try:
            WebDriverWait(self.browser, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]'))) # wait X seconds trying to find element, and timeout if not found.
            self.browser.find_element_by_xpath('//*[@class="onetrust-close-btn-handler onetrust-close-btn-ui banner-close-button ot-close-icon"]').click()  # Close Cookies Message
            print(f'bot #{self.ID} Clicked X on Cookies message popup')

        except SeleniumError.TimeoutException:
            print(f'bot #{self.ID} Didnt find X on Cookies message popup')


    def getSong(self):
        if self.alive == False:
            return 'DeadBot'

        SongChosen = None
        if random.randint(0, 15) <= 2:  # 2/15 song choosers are random
            SongChosen = 'https://open.spotify.com/playlist/6qZnImkqxbRtL9FiwqHkGK'
            self.browser.get(SongChosen)
            sleep(2)
            self.browser.find_elements_by_xpath('//*[@data-testid="play-button"]')[1].click() # click the second element with this xpath after 2 seconds.

        else:
            SongChosen = SP.GetRandomSong()
            self.browser.get(SongChosen)

        print(f'bot #{self.ID} Going to {SongChosen}')


    def AltAccountSwitch(self):
        TempUsername = self.AccountUsername
        TempPassword = self.AccountPassword

        self.AccountUsername = self.AltAccountUsername
        self.AccountPassword = self.AltAccountPassword

        self.AltAccountUsername = TempUsername
        self.AltAccountPassword = TempPassword
