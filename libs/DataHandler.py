import os
import json


def GetAccountsInfo():
    Data = []
    #Check if the accounbts.json exist
    if os.path.exists('Accounts.json'):
        AllAccounts = []
        CurrentAccount = []


        # Opening JSON file (returns JSON object as)
        File = open('Accounts.json', )
        # a dictionary
        FileData = json.load(File)
        # Iterating through the json accounts and get each account as list
        for Account in FileData['Accounts']:
            # print(Account)
            CurrentAccount.append(Account['Email'])
            CurrentAccount.append(Account['Password'])
            CurrentAccount.append(Account['ProxyIP'])
            AllAccounts.append(CurrentAccount)
            CurrentAccount = []
        File.close()


        return AllAccounts
    else:
        print('Error: Could not load up Accounts.json -SelfError\n\n')
        return [['MissingEmail'], ['MissingPassword']]



