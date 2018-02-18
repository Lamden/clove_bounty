from clove.network.bitcoin import Bitcoin


class ProjectX(Bitcoin):
    """
    Class with all the necessary Project-X (NANOX) network information based on
    https://github.com/Tillkoeln/x/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'projectx'
    symbols = ('NANOX', )
    seeds = ('dnsseed111.ddns.net', 'p-x.ddns.net', 'stratumtest.ddns.net', 'dns-seed.ddns.net', 'node4.version2.org',
			 '185.45.193.24', '185.45.193.21', '185.82.202.164', '185.82.202.159', '185.82.202.160', '185.82.202.142',
			 '185.82.202.143', '185.106.121.130', '185.117.73.207', '185.117.73.210')
    port = 42123

# no testnet
