
repos = [{'name': 'repo_name', 'path':'path_to_folder_repo'}]
devs = ['User']
log_interval = 1 # number of weeks log required to show
#icons

ico = {
'repo':'https://cdn2.iconfinder.com/data/icons/designer-skills/128/bitbucket-repository-svn-manage-files-contribute-branch-32.png',
'developer':'https://cdn4.iconfinder.com/data/icons/web-development-5/500/developer-api-coding-screen-24.png',
'commit':'https://cdn0.iconfinder.com/data/icons/octicons/1024/git-commit-32.png',
'no':'https://cdn4.iconfinder.com/data/icons/fugue/icon/document-number.png',
'msg':'https://cdn3.iconfinder.com/data/icons/simple-files-1/128/Message-2-16.png',
'link':'https://cdn2.iconfinder.com/data/icons/office-38/24/office-47-16.png',
'progress':'https://cdn1.iconfinder.com/data/icons/simple-arrow/512/arrow_22-16.png',
'date':'https://cdn2.iconfinder.com/data/icons/office-38/24/office-15-16.png',
'close':'http://samuelhewitt.com/assets/img/terminals/icon-ubuntu-close.png',
'minimize':'http://www.hockeywa.org.au/Portals/54/Containers/RedLion/images/round_minus_icon_24.png',
'maximize':'https://cdn4.iconfinder.com/data/icons/cc_mono_icon_set/blacks/32x32/round_plus.png'
}
		
company_detail={'name':'name_of_the_company', 'logo':'url_to_the_location'}
recipients = [	
		{'name': 'name_of_the_recipient', 'email':'email_of_the_recipient'}

	     ]
sender={
	'Subject':'subject_of_the_mail',
	'From':'from_email_id',
	'smtp':'smtp:port',
	'password': "password"
}
template_file='email_temp.jinja'
template_folder='/home/ubuntu/script/emailSend'

