# AUTOMATED TASKS

![Automation](https://images.unsplash.com/photo-1495055154266-57bbdeada43e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80)

This repository is for my automated tasks. Automation describes a wide range of technologies that reduce human intervention in processes, namely by predetermining decision criteria, subprocess relationships, and related actions, as well as embodying those predeterminations in machines.

## INSTALLATION
1) ```git clone https://github.com/dogaegeozden/automated_tasks.git```
2) ```cd automated_tasks```
3) ```pip3 install -r requirements.txt```
4) ```Edit the credentials.json file write your own credentials```
5) ```Type crontab -e as the root user and add the fallowing to the end of the file without quotes to send a text message every hour. "30 22,21 * * * /usr/bin/python3 /home/username/Desktop/automated_taks/reminder.py"```
