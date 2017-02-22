#!/usr/bin/env python
import client
import atexit
import sys, getopt
import json

def quit_gracefully():
    print "\nBye"

atexit.register(quit_gracefully)

def usage():
  print "Usage: ", sys.argv[0], " -k keyfile"
  sys.exit(2)

keyfile = None

try:
    opts, args = getopt.getopt(sys.argv[1:], "k:", ["keyfile="])
except getopt.GetoptError as err:
    print "Error parsing arguments", str(err)
    usage()

for opt, arg in opts:
    if opt == '-h':
        usage()
    elif opt in ("-k", "--keyfile"):
        keyfile = arg

if keyfile == None:
    usage()

print "Using keyfile: ", keyfile

key = json.load(open(keyfile))
coinpit_me = client.Client(key['privateKey'])
user = coinpit_me.user_id
site = ".me"
done = False
prompt = user + ">"
print "Connected to ", site, ". Enter METHOD and path. METHOD /api/v1/:path will be sent"
while not done:
    try:
        user_input = raw_input(prompt)
        print "Exec", user_input
    except EOFError:
        done = True
