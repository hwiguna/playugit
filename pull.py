print("in pull.py")

import urepl
print("urepl imported")

import ugit
print("ugit imported")

#print("giturl = ", ugit.giturl)
#print("call_trees_url = ", ugit.call_trees_url)
#print("raw = ", ugit.raw)

urepl.wificonnect()
print("wifi Connected")

print("About to pull files from github...")
ugit.pull_all_files()
print("pull_all_files() completed!")

print("running Hello.py...")
import hello