from clove.network.bitcoin import Bitcoin


class UniversalRoyalCoin(Bitcoin):
    """
    Class with all the necessary Universal Royal Coin (UNRC) network information based on
    https://github.com/replicant17/UNRC-sources/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'universalroyalcoin'
    symbols = ('UNRC', )
    seeds = ('seed2.unrc.eu', 'seed3.unrc.eu', 'seed4.unrc.eu', 'seed5.unrc.eu')
    port = 24298
    message_start = b'\xb5\xf5\xe5\xb6'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 188
    }

# no testnet
