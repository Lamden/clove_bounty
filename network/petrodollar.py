from clove.network.bitcoin import Bitcoin


class PetroDollar(Bitcoin):
    """
    Class with all the necessary PetroDollar network information based on
    https://github.com/bryceweiner/petrodollar/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'petrodollar'
    symbols = ('p$', )
    nodes = ("162.243.147.115", )
    port = 23932
    message_start = b'\xad\xe2\xa1\x90'
    base58_prefixes = {
        'PUBKEY_ADDR': 117,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 224
    }

# no testnet
