#!/usr/bin/python

##
#
# A quick/naive way to check status/availibility of any sites passed.
# If unavailible, this script sends an alert email to an admin.
#
# Author: Willie Stevenson
#
##

def send_alert(status_code, site_name):

   RECIPIENTS = ['admin1@example.com', 'admin2@example.com']
   SUBJECT = 'Site down/unavailible at ' + time.strftime("%d/%m/%Y %H:%M:%S")
   MSG_TXT = "Status Code: " + status_code + " -> " + site_name + "\n"
   	 
   message = 'Subject: %s\n\n%s' % (SUBJECT, MSG_TXT)

   s = smtplib.SMTP('localhost')
   s.sendmail('localhost', RECIPIENTS, message)
   s.quit()

if __name__ == "__main__":

	import sys
	# import os
	import subprocess
	import smtplib
	import time

	if len(sys.argv) < 2:
		print "See %s --help / -h / help for more details.\n" % sys.argv[0]
	else:
		for arg in sys.argv[1:]:
			if arg == "--help" or arg == "-h" or arg == "help":
			    print "Must take at least one site as an argument.\n"
			    print "Example Usage\n $ python %s site_name1 site_name2 site_name3\n" % arg[0]
			else:
				#status_code = os.system("curl -s -o /dev/null -w %{http_code} " + arg)
				status_code = subprocess.check_output("curl -s -o /dev/null -w %{http_code} " + arg, shell=True)

				if (status_code == "404" or status_code == "502" or status_code == "503" or status_code == "504"):
					send_alert(status_code, arg)



