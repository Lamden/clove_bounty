from clove.network.bitcoin import Bitcoin


class PioneerCoin(Bitcoin):
    """
    Class with all the necessary PioneerCoin (PCOIN) network information based on
    https://github.com/PCOIN/PIONEERCOIN/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'pioneercoin'
    symbols = ('PCOIN', )
    seeds = ('seed5.cryptolife.net', 'seed2.cryptolife.net',
             'seed3.cryptolife.net', 'electrum3.cryptolife.net')
    port = 35514
    message_start = b'\xfe\xc3\xb9\xde'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 183
    }

# no testnet
