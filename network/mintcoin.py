from clove.network.bitcoin import Bitcoin


class Mintcoin(Bitcoin):
    """
    Class with all the necessary Mintcoin network information based on
    https://github.com/mintcoinproject/mintcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'mintcoin'
    symbols = ('MNT', )
    seeds = ("mintseed.keremhd.name.tr", )
    port = 12788
    message_start = b'\xce\xd5\xdb\xfa'
    base58_prefixes = {
        'PUBKEY_ADDR': 51,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 179
    }

# no testnet
