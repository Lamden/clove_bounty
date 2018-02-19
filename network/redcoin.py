from clove.network.bitcoin import Bitcoin


class  RedCoin(Bitcoin):
    """
    Class with all the necessary  RedCoin (RED) network information based on
    https://github.com/roofsdev/roofs/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'redcoin'
    symbols = ('RED', )
    seeds =  ('dnsseed.redcoinpool.org', 'dnsseed.bytesized-vps.com', 'dnsseed.ltc.xurious.com')
    port = 11631


# no testnet