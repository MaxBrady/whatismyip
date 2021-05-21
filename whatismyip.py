#!/usr/bin/python3
import os


ip = os.getenv('REMOTE_ADDR')





site_title = "Max's Test Site"
print('Content-Type: text/html\n\n')
print('')
# Print Header
print('<html>')

print('<head>')
print('<title>%s</title>' % site_title)
print('</head>')
print('<body>')
print("<b>Max's IP Page</b>")
print('My ip adress is %s' % ip)
print('</body>')
print('</html>')
