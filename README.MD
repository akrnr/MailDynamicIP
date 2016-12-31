MailDynamicIP  v1.0
===================

You can use this program if you are not using a static IP and want to connect to your machine remotely.

The program finds out the IP address of the machine and checks if changed during the last check and then sends an e-mail to inform you with the latest one.

**Usage:**
1-  You just need to configure files under config (**IPConfig** and **MailConfig**). 
    `$ python App.py`

2-  I suggest you to use **crontab** in order to check IP regularly and inform you when it's changed.
    `*/5 * * * * python /path/of/jobs/App.py &>> /path/of/jobs/logs/mailip.log`


Please, feel free to feedback.

Orhun Dalabasmaz</br>
odalabasmaz@gmail.com
