#!/usr/bin/env python3

# Copyright (c) 2019 BELL Computer-Netzwerke GmbH
# Copyright (c) 2019 Robert Weiler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import requests
import json

tool_name = "BELL XMC NBI DeviceLister.py"
tool_version = "1.0.0"
http_user_agent = tool_name + "/" + tool_version

parser = argparse.ArgumentParser(description = 'Fetch all known devices from XMC.')
parser.add_argument('--host', help = 'XMC Hostname / IP', default = 'localhost')
parser.add_argument('--httptimeout', help = 'Timeout for HTTP(S) connections', default = 5)
parser.add_argument('--username', help = 'Username for HTTP auth', default = 'admin')
parser.add_argument('--password', help = 'Password for HTTP auth', default = '')
args = parser.parse_args()

api_url = 'https://' + args.host + ':8443/nbi/graphql'
http_headers = {
	'User-Agent': http_user_agent
}
http_params = {
	'query': 'query { network { devices { up ip sysName deviceData { vendor family subFamily } } } }'
}
r = requests.get(api_url, headers = http_headers, auth = (args.username, args.password), params = http_params, timeout = args.httptimeout)
result = r.json()

for d in result['data']['network']['devices']:
	if d['deviceData']['subFamily'] != '':
		family = d['deviceData']['family'] + ' ' + d['deviceData']['subFamily']
	else:
		family = d['deviceData']['family']
	if d['up']:
		print('+ %s (%s %s "%s") is up.' % (d['ip'], d['deviceData']['vendor'], family, d['sysName']))
	else:
		print('- %s (%s %s "%s") is down.' % (d['ip'], d['deviceData']['vendor'], family, d['sysName']))
