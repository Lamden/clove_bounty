from clove.network.bitcoin import Bitcoin


class ARCHcoin(Bitcoin):
    """
    Class with all the necessary ARCHcoin network information based on
    https://github.com/EdgarSoares/ARCH/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'archcoin'
    symbols = ('ARCH', )
    seeds = ("supernode.archcoin.co")
    port = 8998
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 151
    }

# Has no testnet
