# Google-IT-Automation-Python
## Project Problem Statement
Okay, here's the scenario:

You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

Upload the new products to your online store. That's done using uploadImage.py, Images and descriptions should be uploaded separately, using two different web endpoints. Done using supplier_image_upload.py
Send a report back to the supplier, letting them know what you imported. run.py and report_email.py does this.
Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:

Run a script on your web server to monitor system health.
Send an email with an alert if the server is ever unhealthy. health_check.py checks the health of webserver and sends an email if things go wrong(try stress -cpu 80 command to stress the cpu so it sends an cpu usage alert to the mail).

