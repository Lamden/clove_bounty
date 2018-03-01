from clove.network.bitcoin import Bitcoin


class NewYorkCoin(Bitcoin):
    """
    Class with all the necessary NewYorkCoin network information based on
    https://github.com/NewYorkCoin/newyorkc/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'newyorkcoin'
    symbols = ('NYC', )
    seeds = ("seed.ds.newyorkco.in", "seed.newyorkco.in", )
    port = 17020
    message_start = b'\xc0\xc0\xc0\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 22,
        'SECRET_KEY': 188
    }

# no testnet
