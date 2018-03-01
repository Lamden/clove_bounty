from clove.network.bitcoin import Bitcoin


class AtomicCoin(Bitcoin):
    """
    Class with all the necessary AtomicCoin network information based on
    https://github.com/Atomic-coin/ATOM-Atomic-coin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'atomiccoin'
    symbols = ('ATOM', )
    nodes = ("199.127.226.157", )
    port = 8567
    message_start = b'\x81\x99\x92\x18'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 151
    }

# Has no testnet
