#!/usr/bin/env python
import client
import atexit
import sys, getopt
import json

methods = {}

methods['GET']     = True
methods['POST']    = True
methods['PUT']     = True
methods['DELETE']  = True
methods['PATCH']   = True
methods['OPTIONS'] = True

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
coinpit_me.connect()
user = key['address']
site = ".me"
done = False
prompt = user + ">"
print "Connected to ", site, ". Enter HTTP METHOD path and body. METHOD /api/v1/:path will be sent"
print "Examples: "
print "          GET /account"
print '          PUT /contract/BTCUSD7J14/order/open {"price":1201.2, "uuid":"13ca323b-c2a7-1359-ab35-4a6a1f1de7ea"}'
while not done:
    try:
        user_input = raw_input(prompt)
        parts = user_input.split(" ", 2)
        if(len(parts) < 2):
            print user_input+ ": HTTP Method and url (optionally body) expected. Example: GET /account"
            continue
        method_name = parts[0].upper()
        url = parts[1]
        body = None if len(parts) <= 2 else parts[2]
        if(methods[method_name] == None):
            print method_name + " unrecognized HTTP method"
            continue
        print coinpit_me.rest.auth_server_call(method_name, url, body)
        if(body != None):
            print body
    except EOFError:
        done = True
