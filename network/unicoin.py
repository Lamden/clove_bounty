from clove.network.bitcoin import Bitcoin


class UniCoin(Bitcoin):
    """
    Class with all the necessary UniCoin network information based on
    https://github.com/unicoindev/unicoin/blob/master/src/chainparams.cpp
    (date of access: 02/19/2018)
    """
    name = 'unicoin'
    symbols = ('UNIC', )
    seeds = ("altminers.com", )
    port = 50667
    message_start = b'\x75\x6e\x69\x63'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 224
    }

# no testnet
