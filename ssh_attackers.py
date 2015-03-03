from ipwhois import IPWhois


def get_attacker_info(ip_addr):
    ip_lookup = IPWhois(ip_addr)
    asn = ip_lookup.lookup()['asn']
    country = ip_lookup.lookup()['nets'][-1]['country']
    if country is None:
        country = ip_lookup.lookup()['asn_country_code']
    abuse = ip_lookup.lookup()['nets'][-1]['abuse_emails']
    cidr = ip_lookup.lookup()['nets'][-1]['cidr']
    return {"asn": asn, "country": country, "abuse_email": abuse, "cidr": cidr, "ip_addr": ip_addr}


if __name__ == "__main__":
    log_file = open('/var/log/denyhosts','r')
    lookup_list = []
    denied_host_count = 0
    for log_entry in iter(log_file):
        if 'new denied hosts' in log_entry:
            denied_host_count += 1
    log_file.close()
    print "Total Denied Hosts: %s" % denied_host_count

    log_file = open('/var/log/denyhosts','r')
    for log_entry in iter(log_file):
        if 'new denied hosts' in log_entry:
            date = log_entry.split(',')
            date = date[0]
            ip_address = log_entry.split(' ')[-1]
            ip_address = ip_address.strip('\'[').split('\'')[0]
	    attacker_info = get_attacker_info(ip_address) 
	    attacker_info['blacklist_date'] = date
	    lookup_list.append(attacker_info)
	    print attacker_info 
    log_file.close()

    #print lookup_list