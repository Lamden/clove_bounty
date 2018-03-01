from clove.network.bitcoin import Bitcoin


class GlobalTourCoin(Bitcoin):
    """
    Class with all the necessary Global Tour Coin (GTC) network information based on
    https://github.com/gtccoins/gtccoin/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'globaltourcoin'
    symbols = ('GTC', )
    seeds = ('wallet.cryptolife.net', 'explore.cryptolife.net',
             'seed4.cryptolife.net', 'seed2.cryptolife.net')
    port = 28111
    message_start = b'\xd4\xca\xaf\xeb'
    base58_prefixes = {
        'PUBKEY_ADDR': 11,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 139
    }

# no testnet
