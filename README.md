ssh_attackers.py
================

This is a python script that reads the /var/log/denyhosts log file, determines what IP Addresses have been blocked by denyhosts, then creates a JSON key/value with information about the remote IP Address, such as:
* originating IP prefix
* originating bgp ASN
* abuse email address
* originating country
* blacklist date
* logs of the attack

Build the requirements:
```
pip install -r requirements.txt
```

Run:
```
python ssh_attackers.py
```

Sample output of actual data:
```
{'ip_addr': '58.218.211.180', 'blacklist_date': '2015-03-01 04:54:28', 'country': 'CN', 'abuse_email': 'abuse@jsinfo.net', 'log_data': None, 'cidr': '58.208.0.0/12', 'asn': '23650'}
{'ip_addr': '61.147.107.109', 'blacklist_date': '2015-03-01 08:36:51', 'country': 'CN', 'abuse_email': None, 'log_data': None, 'cidr': '61.147.0.0/16', 'asn': '23650'}
{'ip_addr': '136.169.185.193', 'blacklist_date': '2015-03-01 20:40:56', 'country': 'RU', 'abuse_email': None, 'log_data': None, 'cidr': '136.169.184.0/23', 'asn': '24955'}
{'ip_addr': '27.112.8.214', 'blacklist_date': '2015-03-02 02:48:58', 'country': 'CN', 'abuse_email': 'abuse@cnc-noc.net', 'log_data': None, 'cidr': '27.112.8.0/22', 'asn': '4847'}
{'ip_addr': '218.93.122.130', 'blacklist_date': '2015-03-03 09:17:02', 'country': 'CN', 'abuse_email': None, 'log_data': ['Mar  3 08:48:09 bastion sshd[11993]: Invalid user admin from 218.93.122.130', 'Mar  3 08:48:09 bastion sshd[11993]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130', 'Mar  3 08:48:11 bastion sshd[11993]: Failed password for invalid user admin from 218.93.122.130 port 2571 ssh2', 'Mar  3 08:48:13 bastion sshd[11993]: Failed password for invalid user admin from 218.93.122.130 port 2571 ssh2', 'Mar  3 08:48:16 bastion sshd[11993]: Failed password for invalid user admin from 218.93.122.130 port 2571 ssh2', 'Mar  3 08:48:16 bastion sshd[11993]: Connection closed by 218.93.122.130 [preauth]', 'Mar  3 08:48:16 bastion sshd[11993]: PAM 2 more authentication failures; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130', 'Mar  3 08:52:52 bastion sshd[12386]: Invalid user ftpuser from 218.93.122.130', 'Mar  3 08:52:52 bastion sshd[12386]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130', 'Mar  3 08:52:54 bastion sshd[12386]: Failed password for invalid user ftpuser from 218.93.122.130 port 39318 ssh2', 'Mar  3 08:52:54 bastion sshd[12386]: Connection closed by 218.93.122.130 [preauth]', 'Mar  3 08:56:53 bastion sshd[12690]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130  user=operator', 'Mar  3 08:56:55 bastion sshd[12690]: Failed password for operator from 218.93.122.130 port 45672 ssh2', 'Mar  3 08:56:55 bastion sshd[12690]: Connection closed by 218.93.122.130 [preauth]', 'Mar  3 09:00:55 bastion sshd[12793]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130  user=root', 'Mar  3 09:00:57 bastion sshd[12793]: Failed password for root from 218.93.122.130 port 51595 ssh2', 'Mar  3 09:00:58 bastion sshd[12793]: Connection closed by 218.93.122.130 [preauth]', 'Mar  3 09:04:56 bastion sshd[12930]: Invalid user sql from 218.93.122.130', 'Mar  3 09:04:56 bastion sshd[12930]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130', 'Mar  3 09:04:58 bastion sshd[12930]: Failed password for invalid user sql from 218.93.122.130 port 51103 ssh2', 'Mar  3 09:04:58 bastion sshd[12930]: Connection closed by 218.93.122.130 [preauth]', 'Mar  3 09:08:57 bastion sshd[13033]: Invalid user support from 218.93.122.130', 'Mar  3 09:08:57 bastion sshd[13033]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130', 'Mar  3 09:09:00 bastion sshd[13033]: Failed password for invalid user support from 218.93.122.130 port 58272 ssh2', 'Mar  3 09:09:00 bastion sshd[13033]: Connection closed by 218.93.122.130 [preauth]', 'Mar  3 09:12:53 bastion sshd[13149]: Invalid user sysadmin from 218.93.122.130', 'Mar  3 09:12:53 bastion sshd[13149]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130', 'Mar  3 09:12:54 bastion sshd[13149]: Failed password for invalid user sysadmin from 218.93.122.130 port 41514 ssh2', 'Mar  3 09:12:55 bastion sshd[13149]: Connection closed by 218.93.122.130 [preauth]', 'Mar  3 09:16:48 bastion sshd[13238]: Invalid user ubnt from 218.93.122.130', 'Mar  3 09:16:48 bastion sshd[13238]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=218.93.122.130', 'Mar  3 09:16:50 bastion sshd[13238]: Failed password for invalid user ubnt from 218.93.122.130 port 34121 ssh2', 'Mar  3 09:16:50 bastion sshd[13238]: Connection closed by 218.93.122.130 [preauth]'], 'cidr': '218.93.0.0/16', 'asn': '4134'}
```

Future:

The future of this project is to have a central database that will allow individuals to post data into it via an API. With this information aggregated, a scoring system could be created that would allow people to see top attacking hosts. With abuse email addresses and log data, You can also automate abuse emails to providers and inform them of compromised hosts. 
