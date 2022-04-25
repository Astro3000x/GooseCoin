import os
from bitcoin import *
from hashlib import sha256
from replit import db
import time
import random
print("Goose Coin Crypto")
print('''🌳⚪🌕🌚🌚🐘🌚🐘⚪⚪⚪⚪⚪⚪🌕⚪⚪⚪⚪⚪⚪⚪⚪🌕
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
⚪🍐🍐🍐🍐🍐🍐🍐🍐🍐⚪⚪🌕⚪🍪⚪🍪🍪🍪⚪🌚🌚🌕⚫''')
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
  
  elif db[uname+"password"] == pword:
    print("Logged In")
    db[uname] = uname
  elif db[uname+"password"] != pword:
    print("PassWord Incorrect")
    exit()
    

coinfound = False
def menu():
  print("1: Mine 2: Transfer 3: Account Info & Balance 4: Log Out")
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
        os.environ['coin2'] = random.randint(1, 100000000)
        os.environ['coin3'] = random.randint(1, 100000000)
        os.environ['coin4'] = random.randint(1, 100000000)
        os.environ['coin5'] = random.randint(1, 100000000)
        os.environ['coin6'] = random.randint(1, 100000000)
        os.environ['coin7'] = random.randint(1, 100000000)
        os.environ['coin8'] = random.randint(1, 100000000)
        os.environ['coin9'] = random.randint(1, 100000000)
        
        break
  elif mtl == "2":
    
    print("Amount Of Coins To Transfer:")
    transferamt = int(input())
    print("Account Username To Transfer To:")
    transferacc = input()
    if transferacc in db.keys():
      db[uname+"amount"] -= transferamt
      db[transferacc+"amount"] += transferamt
  elif mtl == "3":
    unameamount = uname+"amount"
    print(f"Account Info\nUsername: {uname}\nAmount Of Goose Coin: {str(db[unameamount])}")
  elif mtl == "4":
    print("Logging Out")
    time.sleep(2)
    exit()
    
while 1 == 1:
  menu()