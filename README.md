# XMC API Clients - Python - DeviceLister

A simple tool that fetches all known devices from XMC.

## Dependencies

DeviceLister.py requires the Python module `requests` to be installed. PIP may be used to install it:

`pip install requests`

## Usage

Tested with Python 3.7.4.

`DeviceLister.py -h`:

<pre>
usage: DeviceLister.py [-h] [--host HOST] [--httptimeout HTTPTIMEOUT]
                       [--username USERNAME] [--password PASSWORD]

Fetch all known devices from XMC.

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           XMC Hostname / IP
  --httptimeout HTTPTIMEOUT
                        Timeout for HTTP(S) connections
  --username USERNAME   Username for HTTP auth
  --password PASSWORD   Password for HTTP auth
</pre>
