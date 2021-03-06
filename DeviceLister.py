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

from urllib3.exceptions import InsecureRequestWarning

TOOL_NAME = "BELL XMC NBI DeviceLister.py"
TOOL_VERSION = "1.1.0"
HTTP_USER_AGENT = TOOL_NAME + "/" + TOOL_VERSION
ERR_SUCCESS = 0
ERR_GENERIC = 255

requests.packages.urllib3.disable_warnings(category = InsecureRequestWarning)

parser = argparse.ArgumentParser(description = 'Fetch all known devices from XMC.')
parser.add_argument('--host', help = 'XMC Hostname / IP', default = 'localhost')
parser.add_argument('--httptimeout', help = 'Timeout for HTTP(S) connections', default = 5)
parser.add_argument('--insecurehttps', help = 'Do not validate HTTPS certificates', default = False, action = 'store_true')
parser.add_argument('--username', help = 'Username for HTTP auth', default = 'admin')
parser.add_argument('--password', help = 'Password for HTTP auth', default = '')
parser.add_argument('--version', help = 'Print version information and exit', default = False, action = 'store_true')
args = parser.parse_args()

if args.version:
	print(HTTP_USER_AGENT)
	exit(ERR_SUCCESS)

api_url = 'https://' + args.host + ':8443/nbi/graphql'
http_headers = {
	'User-Agent': HTTP_USER_AGENT
}
http_params = {
	'query': 'query { network { devices { up ip sysName nickName deviceData { vendor family subFamily } } } }'
}

try:
	r = requests.get(api_url, headers = http_headers, auth = (args.username, args.password), params = http_params, timeout = args.httptimeout, verify = not args.insecurehttps)
	if r.status_code != requests.codes.ok:
		r.raise_for_status()
	result = r.json()
except BaseException as e:
	print('Failed to fetch data from XMC:')
	print(e)
	exit(ERR_GENERIC)

for d in result['data']['network']['devices']:
	family = d['deviceData']['family']
	devName = d['sysName']
	if d['deviceData']['subFamily'] != '':
		family = family + ' ' + d['deviceData']['subFamily']
	if devName == "" and d['nickName'] != "":
		devName = d['nickName']
	if d['up']:
		print('+ %s (%s %s "%s") is up.' % (d['ip'], d['deviceData']['vendor'], family, devName))
	else:
		print('- %s (%s %s "%s") is down.' % (d['ip'], d['deviceData']['vendor'], family, devName))

exit(ERR_SUCCESS)
