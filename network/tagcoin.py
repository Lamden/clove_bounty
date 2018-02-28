from clove.network.bitcoin import Bitcoin


class TagCoin(Bitcoin):
    """
    Class with all the necessary TagCoin (TAG) network information based on
    https://github.com/tagcoin/tagcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'tagcoin'
    symbols = ('TAG', )
    seeds = ('dnsseed.tagbond.com', 'tag.cryptopools.com', '52.6.244.211',
             'seed1.tagbond.com', 'seed4.tagbond.com')
    port = 8623

# no testnet
