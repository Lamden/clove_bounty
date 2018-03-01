from clove.network.bitcoin import Bitcoin


class VirtualCoin(Bitcoin):
    """
    Class with all the necessary VirtualCoin (VC) network information based on
    https://github.com/vcoin-z/virtualcoin/blob/9.2.0/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'virtualcoin'
    symbols = ('VC', )
    seeds = ('dnsseed.vcoin.ca', 'dnsseed.virtualcoin.ca')
    port = 443


class VirtualCoinTestNet(VirtualCoin):
    """
    Class with all the necessary VirtualCoin (VC) testing network information based on
    https://github.com/vcoin-z/virtualcoin/blob/9.2.0/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-virtualcoin'
    seeds = ('testnet-seed.vcoin.ca', 'testnet-seed.virtualcoin.ca')
    port = 80
