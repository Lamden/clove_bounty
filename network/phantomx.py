from clove.network.bitcoin import Bitcoin


class Phantomx(Bitcoin):
    """
    Class with all the necessary Phantomx (PNX) network information based on
    https://github.com/phantomxdev/phantomx/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'phantomx'
    symbols = ('PNX', )
    seeds = ('78.109.28.154',
             '5.9.13.72',
             '45.76.248.87',
             '77.246.157.77',
             '80.211.206.236',
             '45.77.155.37')
    port = 31978
    message_start = b'\xd6\x27\xd6\xe2'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 155
    }

# no testnet
