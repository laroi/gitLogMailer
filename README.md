# Git Log Mailer
This is a simple python script which will fetch logs from git and send it as a mail. All the configurations are defiend in config.py

## Dependencies
### Libraries
- subprocess
- jinja2
- smtplib
- datetime
- MIMEMultipart
- MIMEText

### Git logging format
For this mail to work perfectly. The commit message should have specific format. The format is commit message pipe (|) link pipe status in caps. Here 
- commit message is the actual message you want to add
- link is the link to the issue which you were trying to resolve 
- status is the current status of the todo (INPROGRESS | COMPLETED) 

`commit message | link | STATUS`


## Usage
 `python sendMail.py`
 
## Configs

### repos
  You can add multiple repos. This field will accept array of dictionaries with the following format <br>
 `repos = [{'name': 'repo_name', 'path':'path_to_folder_repo'}]`
 
###devs
 This field should the array of name of developers. This should be same as the git global name <br>
 `devs = ['User']`
 
###log_interval
 This field defines the interval of log that should be extracted. It is mentioned in weeks <br>
 `log_interval = 1 # number of weeks log required to show`
### company_detail
 This field accepts a dictionary as input where you can provice name of the organization and url of the logo of the organization. It will be used by the email template to display it on top <br>
 `company_detail={'name':'name_of_the_company', 'logo':'url_to_the_location'}`
### recipients
  This field defines the recipeints of the mail. It accepts an array of dictionary with name of the recipient and email address
 `recipients = [{'name': 'name_of_the_recipient', 'email':'email_of_the_recipient'}]`
 
### sender
  This field will hold all the credentials of sender email. It is a dictionary where you can add subject of the mail, from email id, password and smtp server detials
  
  `sender={'Subject':'subject_of_the_mail','From':'from_email_id','smtp':'smtp:port','password': "password"}`

### template_file
  This is name of the template file<br>
  `template_file='email_temp.jinja'`
### template_folder
  This is the location of the template file <br>
  `template_folder='/home/ubuntu/script/emailSend'`
## Important Note
  This script uses `subprocess.check_output` with argument `shell = True`, which is discouraged due to security reasons ad could be a threat if used without proper knowledge. Read more about that [here] (https://docs.python.org/2/library/subprocess.html#frequently-used-arguments) 
