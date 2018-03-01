from clove.network.bitcoin import Bitcoin


class Altcommunitycoin(Bitcoin):
    """
    Class with all the necessary Altcommunitycoin network information based on
    https://github.com/altcommunitycoin/altcommunitycoin-skunk/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'Altcommunitycoin'
    symbols = ('ALTCOM', )
    nodes = ('109.230.231.216', '109.230.231.221',
             '212.109.218.47')
    port = 29855
    message_start = b'\x4a\x12\x22\x14'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }


# Has no Testnet
