from clove.network.bitcoin import Bitcoin


class RiceCoin(Bitcoin):
    """
    Class with all the necessary RiceCoin network information based on
    https://github.com/TeamRicecoin/Ricecoin-project/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ricecoin'
    symbols = ('RICE', )
    seeds = ("130.193.81.218")
    port = 41981
    message_start = b'\x72\x37\x24\x07'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 161
    }

# no testnet
