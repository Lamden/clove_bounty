from clove.network.bitcoin import Bitcoin


class CaliphCoin(Bitcoin):
    """
    Class with all the necessary CaliphCoin network information based on
    https://github.com/caliphcoin/CaliphCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'caliphcoin'
    symbols = ('CALC', )
    seeds = ("electrum3.cryptolife.net", )
    port = 29291
    message_start = b'\xde\xc1\x9e\xe0'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 156
    }

# Has no testnet
