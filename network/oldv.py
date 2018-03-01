from clove.network.bitcoin import Bitcoin


class OldV(Bitcoin):
    """
    Class with all the necessary OldV network information based on
    https://github.com/OLDV/OLDV/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'oldv'
    symbols = ('OLV', )
    seeds = ("vsyncnode1.servep2p.com", )
    port = 18154
    message_start = b'\x50\x33\x24\x12'
    base58_prefixes = {
        'PUBKEY_ADDR': 71,
        'SCRIPT_ADDR': 132,
        'SECRET_KEY': 153
    }

# no testnet
