import urllib

u = urllib.urlopen('https://www.google.com')
con = u.read()
print con

print "end"

