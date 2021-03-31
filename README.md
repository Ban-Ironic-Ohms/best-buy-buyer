# best-buy-buyer
To run, you need to set some stuff up. Here they are:

sel.py is the main running file. We need to set it up.

## Step 1:
Find the file path for chromedriver.exe. It should be in the same folder as sel.py. 

On line 12 of sel.py, add the file path where it says 'PATH TO GIT CLONE/best-buy-buyer/chromedriver'

This could be something like /Users/testUsr/desktop/best-buy-buyer/chromedriver

1. Do not include .exe
2. use / not \
3. Do not use reletive path

## Step 2
What do you want to buy?

On line 15, replace the link with the link you want. just copy, paste, and have fun

## Step 3
Selenium

For this, you need to import selenium

```
py -3 -m pip install selenium
```

## Step 4
Running the program

You can run the program sel.py with the command 
```
py -3 sel.py
```
in the git folder

You will get a prompt in the terminal for your email, phone, etc. This is private and local. It will only be given to Best Buy when you checkout

## Expected Outcome
The program will open a Chrome window where you can see everything happen. You may be able to run in headless mode by uncommenting the line 10. This is not a supproted use case

## Mac OS
Included is the MacOS Chrome Driver file. I dont have a mac, so I cant test it. If you want to add a PR to make it work, that would be appreciated. I think it will work as long as you select the correct file for your OS