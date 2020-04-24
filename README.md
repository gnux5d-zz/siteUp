# siteUp
A simple email alert loop using crontab in Linux.

This code is an email alert to verify a metadata (e.g. status code) from requests on URLs and send an email to a single person or a group alerting about whatever you wish. 

The loop is not implemented in the code, instead uses the crontab in Linux to schedule the alert.

Input: you need to place three files in the same directory as the code (contacts.txt, source.txt, message.txt), each one with a specfic information. The source.txt is a duo-line file, the first the sender email and the second with its password; contacts.txt is a multiple line file containing all (or 1) receivers email, one email per line; message.txt is a multiple line with your message body.


Setting up the email alert in crontab, scheduled to every 2 minutes. (Just an example)

- openning the crontab file to set the new job

$ crontab -e

Add the line:

*/2 * * * * /path/to/bin/python3 /path/to/alert/alert.py >> /same/path/as/alert/alert.log

The redirect stdout to a log file is optional but recommended! 

PS: remember to set up yout Gmail sender email, allowing less secure apps to ON.
