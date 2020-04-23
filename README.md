# email-alert
A simple email alert loop using crontab on Linux.

This code is an email alert to verify a metadata (e.g. status code) from requests on URLs and send an email to a single person or a group alerting about whatever you wish. 

The loop is not implemented on the code, instead uses the crontab in Linux to schedule the alert.

Input: you need to place three files in the same directory as the code (contacts.txt, source.txt, message.txt), each one with a specfic information. The source.txt is a duo-line file, the first the sender email and the second with its password; contacts.txt is a multiple line file containing all (or 1) receivers email, one email per line; message.txt is a multiple line with your message body.

source.txt
  email: xxxxxxxx@xxxx.com
  password: whatsup

contacts.txt
  yyyyyy@yyy.com
  vvvvvv@vvv.com
  ...

message.txt
  Good afternoon my good sir,
  
  your page is alive!
