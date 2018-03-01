from clove.network.bitcoin import Bitcoin


class Rubies(Bitcoin):
    """
    Class with all the necessary Rubies (RBIES) network information based on
    https://github.com/BetterBetsLobos/rubies-core/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'rubies'
    symbols = ('RBIES', )
    seeds = ('seed1.rbies.org', 'seed2.rbies.org', 'seed3.rbies.org', 'seed4.rbies.org', 'node1.betterbets.io',
             'node2.betterbets.io', 'node3.betterbets.io', 'node4.betterbets.io', 'node5.betterbets.io',
             'node6.betterbets.io', 'node7.betterbets.io', 'node8.betterbets.io', 'rbies2.bost.link')
    port = 8423
    message_start = b'\x77\x33\x42\x15'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 29,
        'SECRET_KEY': 188
    }

# no testnet
