from clove.network.bitcoin import Bitcoin


class MobileCash(Bitcoin):
    """
    Class with all the necessary MobileCash (MBL) network information based on
    https://github.com/jk14/mobilecash/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'mobilecash'
    symbols = ('MBL', )
    seeds = ('dnsseed.mbl.cash')
    port = 14415
    message_start = b'\xfa\xbd\xb5\xd8'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 110,
        'SECRET_KEY': 178
    }

# no testnet
