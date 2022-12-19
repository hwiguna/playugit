print("in pull.py")

#import urepl
#print("urepl imported")

import ugit
print("ugit imported")

#urepl.wificonnect()
#print("wifi Connected")

print("About to pull files from github...")
ugit.pull_all()
print("pull_all() completed!")

print("running Hello.py...")
import hello