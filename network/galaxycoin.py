from clove.network.bitcoin import Bitcoin


class GalaxyCoin(Bitcoin):
    """
    Class with all the necessary GalaxyCoin network information based on
    https://github.com/m0gliE/galaxycoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'galaxycoin'
    symbols = ('GLX', )
    seeds = ("galaxycoin.no-ip.biz")
    port = 15521
    message_start = b'\xfd\xc0\xe9\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 98,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 226
    }

# no testnet
