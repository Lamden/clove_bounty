from clove.network.bitcoin import Bitcoin


class EcoCoin(Bitcoin):
    """
    Class with all the necessary EcoCoin (ECO) network information based on
    https://github.com/ECOcoin-src/ECO-source/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'ecocoin'
    symbols = ('ECO', )
    seeds = ('ecocoin.info', )
    port = 11047
    message_start = b'\x32\x5e\x6f\x86'
    base58_prefixes = {
        'PUBKEY_ADDR': 13,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 141
    }

# no testnet
