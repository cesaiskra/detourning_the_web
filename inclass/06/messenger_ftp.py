import random
import videomash
import paramiko
import sys
from twilio.rest import TwilioRestClient

username = 'dh_iv479w'
password = 'T7Y22tMz'


nouns = open('nouns.txt', 'r').readlines()
word1 = random.choice(nouns).strip()
word2 = random.choice(nouns).strip()

print word1, word2

# videomash.mash(word1, word2)
videomash.mash('pee', 'poo')


host = "vids.lav.io"
port = 22
transport = paramiko.Transport((host, port))

transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

path = './vidds.lav.io/' + outfile
localpath = sys.argv[1]
sftp.put(outfile, path)

sftp.close()
transport.close()
print 'Upload done.'

url = 'http://vidds.lav.io/' + outfile
print url

body = word1 + ' ' + word2 + ': ' + url

client = TwilioRestClient(sid, token)
message = client.messages.create(to='+14152382494', from='twilio_number', body=body)