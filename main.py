import os
from bitcoin import *
from hashlib import sha256
from replit import db
import time
import random
print("Goose Coin Crypto")
print('''🌳⚪🌕🌚🌚🐘🌚🐘⚪⚪⚪⚪⚪⚪🌕⚪⚪⚪⚪⚪⚪⚪⚪
🌕💼🙊🙊🌕🌕⚫🌕⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌕
🌕💼🍊🙊🌕⚪🐘🌚🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌕
⚪🌚💼🌚⚫⚪⚪🌚🌕⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌕
⚪⚪🌕🐘🌕🌚🌚🐘⚫🌚🐘🌚🌚🌚🌚🌚🌚🌚🌚⚪⚪⚪🌕
⚪⚪⚪⚪⚪🌚🌕⚪🌚⚫🌚🌕🌚🌕🌕🌕🐘🌚🐘⚪⚪⚪🌕
⚪⚪⚪⚪🌚🌕🌚⚫🌚🌚🌕🌚🌚🌚🌚🌚⚪🌕🐘🌚⚪⚪🌕
⚪⚪⚪⚪⚪⚪🌚🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌚⚪⚪🌕
⚪⚪⚪⚪⚪⚪🌚🐘⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌕⚫⚪🌕
⚪⚪⚪⚪⚪⚪🌚🐘⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚫⚪🌕
⚪⚪⚪⚪⚪⚪🐘🌚⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🌕⚫⚪🌕
⚪⚪⚪⚪⚪⚪🌕🌚🌕⚪⚪⚪⚪⚪⚪⚪⚪🌚🌚⚫🐘⚪🌕
⚪⚪⚪⚪⚪⚪⚪🌚🌚🌕🌚⚪⚪⚪⚪⚪🌚⚫🌚🌚⚪⚪🌕
⚪⚪⚪⚪⚪⚪⚪⚪🌕🌕🌚⚫🌚🌚🌚🌚🌚🌚🌕🌚⚪⚪🌕
⚪⚪⚪⚪⚪⚪⚪⚪⚪🌕🌚🌚🌚🌚🌕🌚⚪⚪⚪⚪⚪⚪🌕
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🍪⚪⚪⚪🍪⚪⚪⚪⚪⚪🌕
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🍪⚪⚪⚪💰⚪⚪⚪⚪⚪🌕
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🍪⚪⚪⚪💰⚪⚪⚪⚪⚪🌕
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🍑🍪⚪⚪⚪⚪🍪⚪⚪⚪⚪🌕
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🍪🍪📀⚪⚪🍪⚪⚪⚪⚪🌕
⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪🍪💰🍑🍪⚪🍪🍪⚪⚪⚪⚪🌕
⚪🍐🍐🍐🍐🍐🍐🍐🍐🍐⚪⚪🌕⚪🍪⚪🍪🍪🍪⚪🌚🌚🌕''')
print("1: Log In 2: Sign Up")
ls = input()
if ls == "2":
  uname = input("Username: ")
  pword = input("Password: ")
  if uname not in db.keys():
    db[uname] = uname
    db[uname+"password"] = pword
    db[uname+"amount"] = 0
    db[uname+"keys"] = []
    
  else:
    print("UserName Already Taken")
    exit()
if ls == "1":
  uname = input("Username: ")
  pword = input("Password: ")
  
  if uname+"password" not in db.keys():
    print("Account Does Not Exist")
    exit()
  
  elif db[uname+"password"] == pword:
    print("Logged In")
    db[uname] = uname
  elif db[uname+"password"] != pword:
    print("PassWord Incorrect")
    exit()
    

coinfound = False
def menu():
  print("1: Mine 2: Transfer 3: Account Info & Balance 4: Change Password 5: Log Out")
  mtl = input()
  def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
    MAX_NONCE=10000000
  coins = [SHA256(os.environ['originalcoin']), SHA256(os.environ['coin2']), SHA256(os.environ['coin3']), SHA256(os.environ['coin4']), SHA256(os.environ['coin5']), SHA256(os.environ['coin6']), SHA256(os.environ['coin7']), SHA256(os.environ['coin8']), SHA256(os.environ['coin9'])]

  
  if mtl == "1":
    print("Mining...")
    for i in range(1, 100000000):
      found = SHA256(str(i))
      if found in coins:
        print("Coin Found!")
        db[uname+"amount"] += 1
        db[uname+"key"+str(db[uname+"amount"])] = str(found)
        os.environ['coin2'] = str(random.randint(1, 1000000))
        os.environ['coin3'] = str(random.randint(1, 1000000))
        os.environ['coin4'] = str(random.randint(1, 1000000))
        os.environ['coin5'] = str(random.randint(1, 1000000))
        os.environ['coin6'] = str(random.randint(1, 1000000))
        os.environ['coin7'] = str(random.randint(1, 1000000))
        os.environ['coin8'] = str(random.randint(1, 1000000))
        os.environ['coin9'] = str(random.randint(1, 1000000))
        
        break
  elif mtl == "2":
    
    print("Amount Of Coins To Transfer:")
    transferamt = int(input())
    print("Account Username To Transfer To:")
    transferacc = input()
    if transferacc in db.keys():
      db[uname+"amount"] -= transferamt
      db[transferacc+"amount"] += transferamt
    else:
      print("User Does Not Exist")
  elif mtl == "3":
    unameamount = uname+"amount"
    print(f"Account Info\nUsername: {uname}\nAmount Of Goose Coin: {str(db[unameamount])}")
  elif mtl == "4":
    print("Enter Previous Password:")
    pre1 = input()
    print("Confirm Previous Password:")
    pre2 = input()
    if pre1 == pre2:
      if pre1 == db[uname+"password"]:
        print("Passwords correct. New password:")
        new1 = input()
        print("Confirm New Password:")
        new2 = input()
        if new1 == new2:
          db[uname+"password"] = new1
          print("Password Changed.")
    else:
      print("Passwords do not match.")
  elif mtl == "5":
    print("Logging Out")
    time.sleep(2)
    exit()
    
while 1 == 1:
  menu()