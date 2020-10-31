#!/usr/bin/env python3

import os, datetime
import reports
import email

cur_date = datetime.datetime.now().strftime('%Y-%m-%d');
def generate_pdf(path):
	pdf = ""
	texts = os.listdir(path)
	for text in texts:
		if file.endswith(".txt"):
    		with open(path + file, 'r') as f:
        		line = f.readlines()
        		name = line[0].strip()
        		weight = line[1].strip()
        		pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"
  	return pdf

if __name__ == "__main__":
	  path = "supplier-data/descriptions/"
	  title = "Process Updated on " + current_date 
	  #generate the package for pdf body
	  package = generate_pdf(path)
	  reports.generate_report("/tmp/processed.pdf", title, package)
		
	  #generate email information
	  sender = "automation@example.com"
	  receiver = "student-02-5e4c919a3ccc@example.com"
	  subject = "Upload Completed - Online Fruit Store"
	  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	  attachment = "/tmp/processed.pdf"
	  
	  #generate email for the online fruit store report and pdf attachment
	  message = emails.generate_email(sender, receiver, subject, body, attachment)
	  emails.send_email(message)	
