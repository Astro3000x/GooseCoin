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
elif ls == "1":
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
    
else:
  print("Please Choose 1 or 2")
  exit()
coinfound = False
def menu():
  print("1: Mine 2: Transfer 3: Account Info & Balance 4: Change Password 5: Current Price 6: Log Out")
  mtl = input()
  def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()
    MAX_NONCE=10000000
  coins = [SHA256(str(db["coin2"])), SHA256(str(db["coin3"])), SHA256(str(db["coin4"])), SHA256(str(db["coin5"])), SHA256(str(db["coin6"])), SHA256(str(db["coin7"])), SHA256(str(db["coin8"])), SHA256(str(db["coin9"]))]

  
  if mtl == "1":
    print("Mining...")
    for i in range(1, 100000000):
      found = SHA256(str(i))
      if found in coins:
        print("Coin Found!")
        
        db[uname+"key"+str(db[uname+"amount"])] = str(found)
        
        db[uname+"amount"] += 1
        db["coin2"] = random.randint(1, 100000000)
        db["coin3"] = random.randint(1, 100000000)
        db["coin4"] = random.randint(1, 100000000)
        db["coin5"] = random.randint(1, 100000000)
        db["coin6"] = random.randint(1, 100000000)
        db["coin7"] = random.randint(1, 100000000)
        db["coin8"] = random.randint(1, 100000000)
        db["coin9"] = random.randint(1, 100000000)
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
    print("$2 (Live Price Updates: https://goosecoin.astro3000.dev)")
  elif mtl == "6":
    print("Logging Out")
    time.sleep(2)
    exit()
    
while 1 == 1:
  menu()