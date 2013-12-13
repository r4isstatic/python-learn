#!/usr/bin/env python

#This again uses the os module, but then creates a system command to activate a Growl notification
import os
os.system("growlnotify -m 'growling from python'")