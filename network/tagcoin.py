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
    message_start = b'\xf4\xed\xe2\xb9'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 193
    }

# no testnet
