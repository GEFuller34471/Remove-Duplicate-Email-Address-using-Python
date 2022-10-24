# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pandas as pd
import os
import glob


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

msg = "Hello World!!"
print(msg)

csv1 = pd.read_csv('DataFiles\hotmailContacts20221023.csv')
csv2 = pd.read_csv('DataFiles\outlookContacts20221023.csv')
csv3 = pd.read_csv('DataFiles\PersonalFolderContacts20221023.csv')

print(csv1.info())
print(csv1.head(22))
print("")
print(csv2.head(22))
print("")
print(csv3.head(22))
print("")

