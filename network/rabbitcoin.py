from clove.network.bitcoin import Bitcoin


class RabbitCoin(Bitcoin):
    """
    Class with all the necessary RabbitCoin (RBBT) network information based on
    https://bitbucket.org/rabbitcoin/rabbitcoin/src/6c1f7b640f48e2b3206b0609156e73d7e4c8df79/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'rabbitcoin'
    symbols = ('RBBT', )
    seeds = ('seed.rabbitco.in', )
    port = 17020
    message_start = b'\xc0\xc0\xc0\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 22,
        'SECRET_KEY': 188
    }

# no testnet
