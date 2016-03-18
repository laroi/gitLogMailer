#!/usr/bin/python
import subprocess
import jinja2
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config

repos = config.repos
devs = config.devs
recipients = config.recipients
templateLoader = jinja2.FileSystemLoader( searchpath=config.template_folder)
templateEnv = jinja2.Environment( loader=templateLoader )
repo_array = []
dev_array = []
log_array = []
template = templateEnv.get_template(config.template_file)


class Logs:
	def __init__(self, subject, link, status, date):
		self.subject = subject
		self.link = link
		self.status = status
		self.date = date
class Developer:
	def __init__(self, developer, logs=None):
		self.developer = developer.title()
		self.logs = logs
class Repo:
	def __init__(self, repo_name, developer=None, graph=None):
		self.repo_name = repo_name
		self.developer = developer
		self.graph = graph	
class Mailer:
	def __init__(self, mail_smtp, mail_from, mail_password):
		self.server = smtplib.SMTP(mail_smtp)
		print mail_smtp
		print mail_from
		print mail_password
		self.server.starttls()
		self.server.login(mail_from, mail_password)
	def sendMail(self, recipient, body):
		msg = MIMEMultipart('alternative')
		msg['Subject'] = config.sender['Subject'] + " : " +str(datetime.date.today())
		msg['From'] = config.sender['From']
		msg['To'] = recipient
		bdy = MIMEText(body, 'html')
		msg.attach(bdy)
		print config.sender['Subject']
		print config.sender['From']
		print recipient 
		self.server.sendmail(config.sender['From'], recipient, msg.as_string())
	def kill(self):
		self.server.quit()

def getCommitters(dir):
	committers = subprocess.check_output('/usr/bin/git --git-dir='+dir+' shortlog -sn HEAD | awk \'{print $2}\'', shell=True)
#	print committers
	return committers
def getLogs(committer, dir):
	command ='/usr/bin/git --git-dir=' + dir + ' log --author=' + committer  + ' --pretty=format:"%s^%cd " --date="short" --after="' + config.log_interval + ' weeks ago"'
	logs = subprocess.check_output(command, shell=True)
	if (logs != 'None' and len(logs) > 0):
#		print logs
		return logs
	else:
		return None
def getGraph(dir):
	graph_cmd = '/usr/bin/git --git-dir=' + dir + ' log --graph --abbrev-commit --decorate --format=format:\'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)\' --all --since=2.weeks'
	graph = subprocess.check_output(graph_cmd, shell=True)
	graphlines = graph.split("\n");
	formatted_graph='';
	for line in graphlines:
		line = '<span style="color:red; font-weight: bold;">' + line
		line = line.replace('[1;34m', '<span style="color:#B8857A">')
		line = line.replace('[1;32m', '<span style="color:#95BF40">')
		line = line.replace('[1;37m', '<span style="color:#4F5445">')
		line = line.replace('[2;37m', '<span style="color:#336699">')
		line = line.replace('[37m', '<span style="color:#997733">')
		line = line.replace('[1;33m', '<span style="color:#3D8F81">')	
		line = line.replace('[m', '</span>')
		line += "</span><br>"
		formatted_graph += line
	return formatted_graph

def getContent():
	for repo in repos:
		rep = Repo(repo['name'])
		committers = getCommitters(repo['path'])
		dev_array = []
		rep.graph = getGraph(repo['path'])
		for committer in committers.split('\n'):
			if (len(committer)>0 and committer in devs):
				dev = Developer(committer)	
				log_array = []
				logs = getLogs(committer, repo['path'] )
				if logs:
					logs = logs.split('\n')
					for log in logs:
						log = log.split('^')
						if len(log) > 1:
							date = log[1]
						spllog = log[0].split('|')
						if len(spllog) == 3:
							subject = spllog[0]
							link = spllog[1]
							status = spllog[2]
						else:
							subject = spllog[0]
							link = None
							status = None
						lo = Logs(subject, link, status, date)
						log_array.append(lo)
						dev.logs = log_array
				else:
					dev.logs = []
				dev_array.append(dev)
				rep.developer = dev_array;
		repo_array.append(rep)
		endDate =datetime.date.today()
		startDate = endDate - datetime.timedelta(days=14)
	
	return template.render(repo = repo_array, company_detail=config.company_detail, icons=config.ico, startDate=str(startDate), endDate=str(endDate))

body = getContent()
mail_obj = Mailer(config.sender['smtp'], config.sender['From'], config.sender['password'])
for recipient in recipients:
	mail_body = jinja2.Environment().from_string(body).render(name=recipient['name']) 
	mail_obj.sendMail(recipient['email'], mail_body)

mail_obj.kill()
