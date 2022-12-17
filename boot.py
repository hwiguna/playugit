print("in boot.py")

import urepl
print("urepl imported")

import ugit
print("ugit imported")

urepl.wificonnect()
print("wifi Connected")

print("About to pull files from github...")
ugit.pull_all_files()
print("pull_all_files() completed!")

print("running Hello.py...")
import hello