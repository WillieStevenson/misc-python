#!/usr/bin/python

##
#
# A quick/naive way to check status/availability of any sites passed.
# If unavailable, this script sends an alert email to an admin.
#
# Author: Willie Stevenson
#
##

def send_alert(status_code, site_name):

   RECIPIENTS = ['admin1@example.com', 'admin2@example.com']
   SUBJECT = 'Site down/unavailable at ' + time.strftime("%d/%m/%Y %H:%M:%S")
   MSG_TXT = "Status Code: " + status_code + " -> " + site_name + "\n"
   	 
   message = 'Subject: %s\n\n%s' % (SUBJECT, MSG_TXT)

   s = smtplib.SMTP('localhost')
   s.sendmail('localhost', RECIPIENTS, message)
   s.quit()

if __name__ == "__main__":

	import sys
	import subprocess
	import smtplib
	import time

	# put status codes to check against here (i.e., not found, unavailable/down)
	codes = ["404", "503"]

	if len(sys.argv) < 2:
		print "See %s --help / -h / help for more details.\n" % sys.argv[0]
	else:
		for arg in sys.argv[1:]:
			if arg == "--help" or arg == "-h" or arg == "help":
			    print "Must take at least one site as an argument.\n"
			    print "Example Usage\n $ python %s site_name1 site_name2 site_name3\n" % arg[0]
			else:
				status_code = subprocess.check_output("curl -s -o /dev/null -w %{http_code} " + arg, shell=True)

				if (status_code in codes):
					send_alert(status_code, arg)



