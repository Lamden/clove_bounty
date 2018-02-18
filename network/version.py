from clove.network.bitcoin import Bitcoin


class Version(Bitcoin):
    """
    Class with all the necessary Version (V) network information based on
    https://github.com/noise23/version/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'version'
    symbols = ('V', )
    seeds = ('dns.seed.version2.org', 'node1.version2.org', 'node2.version2.org', 
			 'node3.version2.org', 'node4.version2.org')
    port = 9988

# no testnet
