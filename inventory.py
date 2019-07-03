#!/usr/bin/env python

import json
import sys

if __name__ == "__main__":
	hostvars =  dict(ansible_host="127.0.0.1")
	if sys.argv[1] in ['--list', '--ini']:
		num_hosts = int(sys.argv[2]) if len(sys.argv) > 2 else 5
		len_hosts = len(str(num_hosts))
		hosts = ['host{}'.format(str(i).zfill(len_hosts)) for i in range(num_hosts)]
		if sys.argv[1] == '--ini':
			
			output = '[local]\n'
			output += '\n'.join(hosts)
			output += '\n[local:vars]\n'
			output += '\n'.join(['{}={}'.format(k, v) for k, v in hostvars.items()])
		else:
			output = json.dumps(dict(local=dict(hosts=hosts, vars=hostvars)), indent=4)
	elif sys.argv[1] == '--host':
		output = json.dumps(hostvars, indent=True)
	print(output)
