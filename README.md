"# BlinkPay" 

This is the part of blinkpay project.
This part contain only backend of project it contains some features like import .xlsxfile from admin pannel and it will automatically save to dbsqlite3 database in local system where we are expecting the data from the database to fill the SBI form automatically by using selenium automation.
Here,SBI Form Captcha is read and bypass by easyocr model of machine learning.

# How To Run?
**1. Install Python in local Computer.**
**2. Run pip install -r requirements.txt**
**3. Run server python manage.py runserver**
**4. After the run server you will have go localhost:/8000/admin**
**5. After that you have to put username :- admin and password :- 1234**
**6. Then upload your .xlxs file from admin pannel**
**7. Then go to localhost://8000/<card_id>/ to automate specific details Now it will automatically automate**
