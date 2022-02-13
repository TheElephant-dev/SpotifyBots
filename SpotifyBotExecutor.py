# Python Built-in imports
import random
from sys import platform as OsName
from time import sleep
import math
from datetime import *

#Custom Python File imports
from libs import EmailSender, BotClass, DataHandler
#EmailSender.Send(Title='TestTitle', MailContent='''Greetings me pirates!''')



################################################################################################################
########## Settings
'''
7200 seconds is 2 hours.
43200 seconds is 12 hours. (but use 43000 to avoid overlapping actions) 
'''
ChangeSongEvery_X_Seconds = 7200
ChangeShiftEvery_X_Seconds = 43200




################################################################################################################
########## Change Settings based on OS
chromedriverpath = ''

if OsName == 'win32':
    chromedriverpath = 'chromedriver'
else:
    chromedriverpath = './chromedriver'




################################################################################################################
###########Get Accounts, Albums, Songs, Platforms, ProxyServer lists.
#-----------------------------------
### Accounts
Accounts = DataHandler.GetAccountsInfo()
for Num in range(len(Accounts)):
    print(f'{" "*Num}-{Num}->{Accounts[Num]}')
#-----------------------------------
### Albums

#-----------------------------------
### Songs

#-----------------------------------
### Platforms



################################################################################################################
########### Main Variables for the process
#Bots
Bots = []

# Get the amount of bots to run
MaxPossibleBotsToRun = math.floor(len(Accounts) / 2)
try:
    AmountOfBotsToRun = 1
    # AmountOfBotsToRun = min(MaxPossibleBotsToRun, int(input(f'(Detected {len(Accounts)} Accounts, so can run up to {MaxPossibleBotsToRun} bots)\nHow Many Bots would you like to run? ')))
    print(F'Running {AmountOfBotsToRun} bots')
except ValueError as Error:
    print(f'Error! Likely you used chars instead of numbers on bot amount request. if this is not the case, the error was: \n{Error}')
    exit()


################################################################################################################
########### Bot Setup

# Start up the bots
for X in range(AmountOfBotsToRun):
    Bots.append(BotClass.BotInstence(BotID=X, BotChromeDriverPath=chromedriverpath, BotAccountUsername=Accounts[X][0], BotAccountPassword=Accounts[X][1], AltBotAccountUsername=Accounts[X + AmountOfBotsToRun][0], AltBotAccountPassword=Accounts[X + AmountOfBotsToRun][1], BotProxyServerIP=Accounts[X][2]))



def ProcessBotsStarting():
    for bot in Bots:
        bot.Birth()


    for bot in Bots:
        bot.Login()


    for bot in Bots:
        bot.GetRidOfCookiesPopup()


    for bot in Bots:
        bot.getSong()


################################################################################################################
########### Bot Action Cycle

ProcessBotsStarting()




ShiftStart = datetime.now()
print(f'ShiftStart = {ShiftStart}')

CurrentSongCounter = 0
CurrentShiftCounter = 0
while True:
    sleep(1)
    CurrentSongCounter += 1
    CurrentShiftCounter += 1


    if CurrentShiftCounter >= ChangeShiftEvery_X_Seconds: # Change Shifts if its past time(restart bots with new accounts)
        CurrentShiftCounter = 1
        print('New Bot Shift!')

        for bot in Bots:
            bot.Kill()
            bot.AltAccountSwitch()

        ProcessBotsStarting()


    if CurrentSongCounter >= ChangeSongEvery_X_Seconds: # Re-roll Songs every 2 hours
        CurrentSongCounter = 1
        print('Time to switch songs!')
        for bot in Bots:
            bot.getSong()
            sleep(3)  # small delay between each song switch to prevent CPU usage spike.
