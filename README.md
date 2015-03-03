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

Sample output:
```
{'ip_addr': '112.95.167.111', 'blacklist_date': '2015-02-18 02:32:51', 'country': 'CN', 'abuse_email': 'abuse@cnc-noc.net', 'log_data': None, 'cidr': '112.88.0.0/13', 'asn': '17623'}
```
