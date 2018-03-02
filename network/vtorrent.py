from clove.network.bitcoin import Bitcoin


class VTorrent(Bitcoin):
    """
    Class with all the necessary VTorrent (VTR) network information based on
    https://github.com/vtorrent/vTorrent-Client/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'vtorrent'
    symbols = ('VTR', )
    seeds = ('vtrseed.mooo.com', 'vtrseed1.mooo.com', 'vtrseed.ignorelist.com', )
    port = 22524
    message_start = b'\x22\x05\x35\x70'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 203
    }

# no testnet
