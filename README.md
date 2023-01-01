# AUTOMATED TASKS

![Automation](https://images.unsplash.com/photo-1495055154266-57bbdeada43e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80)

This repository is for my automated tasks. Automation describes a wide range of technologies that reduce human intervention in processes, namely by predetermining decision criteria, subprocess relationships, and related actions, as well as embodying those predeterminations in machines.

## INSTALLATION
1) ```git clone https://github.com/dogaegeozden/automated_tasks.git```
2) ```cd automated_tasks```
3) ```pip3 install -r requirements.txt```
4) ```sudo echo 'export TWILIOSID="WriteYourTwilioSid"' >> /root/.bashrc```
5) ```sudo echo 'export TWILIOTOKEN="WriteYourTwilioToken"' >> /root/.bashrc```
6) ```sudo echo 'export MYTWILIOPHONENUM="WriteYourTwilioPhoneNum"' >> /root/.bashrc```
7) ```sudo echo 'export MYREGULARPHONENUM="WriteYourTargetPhoneNum"' >> /root/.bashrc```
8) ```source /root/.bashrc```
9) ```echo 'export TWILIOSID="WriteYourTwilioSid"' >> ~/.bashrc```
10) ```echo 'export TWILIOTOKEN="WriteYourTwilioToken"' >> ~/.bashrc```
11) ```echo 'export MYTWILIOPHONENUM="WriteYourTwilioPhoneNum"' >> ~/.bashrc```
12) ```echo 'export MYREGULARPHONENUM="WriteYourTargetPhoneNum"' >> ~/.bashrc```
13) ```source ~/.bashrc```
14) ```Type crontab -e as a regular user and add the fallowing to the end of the file without quotes to send a text message every day."45 22 * * * /usr/bin/python3 /path/to/umbrellaReminding.py"```
15) ```Type crontab -e as the root user and add the fallowing to the end of the file without quotes to send a text message every hour. "45 * * * * /usr/bin/python3 /path/to/portScanning.py"```
