from clove.network.bitcoin import Bitcoin


class Sequence(Bitcoin):
    """
    Class with all the necessary Sequence network information based on
    https://github.com/duality-solutions/Sequence/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'sequence'
    symbols = ('SEQ', )
    seeds = ("seq.dnsseeder.io",
             "seq.dnsseeder.com",
             "seq.dnsseeder.host",
             "seq.dnsseeder.net")
    port = 16662

# no testnet
