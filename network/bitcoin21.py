from clove.network.bitcoin import Bitcoin


class Bitcoin21(Bitcoin):
    """
    Class with all the necessary Bitcoin21 network information based on
    https://github.com/bitcoin21/v1.0/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'Bitcoin21'
    symbols = ('XBTC21', )
    seeds = ("seed1.cryptolife.net", "seed2.cryptolife.net", "seed3.cryptolife.net",
             "electrum1.cryptolife.net", "wallet.cryptolife.net", "explore.cryptolife.net")
    port = 21008
    message_start = b'\xb4\xf8\xe2\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 3,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 131
    }


# Has no Testnet
