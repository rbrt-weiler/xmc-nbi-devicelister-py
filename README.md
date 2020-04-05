# XMC NBI DeviceLister (Python)

DeviceLister uses the GraphQL-based API provided by the Northbound Interface (NBI) of [Extreme Management Center (XMC)](https://www.extremenetworks.com/product/extreme-management-center/) to fetch and display a list of all devices. The list includes the following pieces of information for each device:

* up/down (as +/- and text)
* IP address
* vendor and model
* system name or nick name

The tool is intended to provide a quick overview of the managed devices and to serve as a starting point for other tools.

## Branches

This project uses two defined branches:

* `master` is the primary development branch. Code within `master` may be broken at any time.
* `stable` is reserved for code that interprets without errors and is tested. Track `stable` if you just want to use the software.

Other branches, for example for developing specific features, may be created and deleted at any time.

## Dependencies

DeviceLister.py requires the Python module `requests` to be installed. PIP may be used to install it:

`pip install requests`

## Usage

Tested with Python 3.7.{3,4} and 3.8.0.

`DeviceLister.py -h`:

```text
  -h, --help            show this help message and exit
  --host HOST           XMC Hostname / IP
  --httptimeout HTTPTIMEOUT
                        Timeout for HTTP(S) connections
  --insecurehttps       Do not validate HTTPS certificates
  --username USERNAME   Username for HTTP auth
  --password PASSWORD   Password for HTTP auth
  --version             Print version information and exit
```

## Source

The original project is [hosted at GitLab](https://gitlab.com/rbrt-weiler/xmc-nbi-devicelister-py), with a [copy over at GitHub](https://github.com/rbrt-weiler/xmc-nbi-devicelister-py) for the folks over there. Additionally, there is a project at GitLab which [collects all available clients](https://gitlab.com/rbrt-weiler/xmc-nbi-clients).
