# -*- coding: utf-8 -*-
import imaplib
import time
import email.message
import ConfigParser
import os

def open_connection(verbose=False):
    # Connect to the server
    hostname = "imap.gmail.com"
    if verbose: print 'Connecting to', hostname
    connection = imaplib.IMAP4_SSL(hostname)

    # Login to our account
    #username = "naamabidar@gmail.com"
    username = "cohendana38@gmail.com"
    password = "YellowCat"
    if verbose: print 'Logging in as', username
    connection.login(username, password)
    return connection

if __name__ == '__main__':
    c = open_connection(verbose=True)
    #print c
    new_message = email.message.Message()
    new_message["From"] = "kev@gmail.com"
    new_message["Subject"] = "Open Position For Cyber Security Expert"
    new_message.set_payload("Name: Kevin Mitnick\n\nLinkedin: http://linkеdin.com/in/kevinmitnick")
    c.append('INBOX', '', imaplib.Time2Internaldate(time.time()), str(new_message))
    #try:
    #finally:
    c.logout()
