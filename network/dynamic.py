from clove.network.bitcoin import Bitcoin


class Dynamic(Bitcoin):
    """
    Class with all the necessary Dynamic (DYN) network information based on
    https://github.com/duality-solutions/Dynamic/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'dynamic'
    symbols = ('DYN', )
    seeds = ('dyn2.dnsseeder.io', 'dyn2.dnsseeder.com',
             'dyn2.dnsseeder.host', 'dyn2.dnsseeder.net')
    port = 33300

# no testnet
