print "\n\n *** ZTP Python Script *** \n\n"

import cli
import re

print "\n\n *** Retriving SN *** \n\n"
cli.executep('show inv')
strip = cli.execute('show inv')
st = strip.split()
for s in st:
	if re.match('\w{11}', s):
		sn = s
		break
print ("\n\n *** SN: %s *** \n\n" % sn)


print "\n\n *** Pumping in configuration *** \n\n"
cli.executep('copy tftp://172.16.1.1/bootup/config/%s runn' % sn)
cli.executep('wr')

print "\n\n *** ZTP Python Script Execution Complete *** \n\n"