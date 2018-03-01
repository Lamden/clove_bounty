from clove.network.bitcoin import Bitcoin


class ARbit(Bitcoin):
    """
    Class with all the necessary ARbit network information based on
    https://github.com/arbitcoin/arbit/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'ARbit'
    symbols = ('ARB', )
    seeds = ('162.243.203.211', '178.62.56.172')
    port = 31930
    message_start = b'\xe3\xa7\x7c\x0e'
    base58_prefixes = {
        'PUBKEY_ADDR': 23,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 151
    }

# Has no Testnet
