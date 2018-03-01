from clove.network.bitcoin import Bitcoin


class SecretCoin(Bitcoin):
    """
    Class with all the necessary SecretCoin network information based on
    https://github.com/TeamSecret/SecretCoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'secretcoin'
    symbols = ('SCRT', )
    nodes = ("23.227.190.110", )
    port = 23152
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 191
    }

# no testnet
