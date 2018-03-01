from clove.network.bitcoin import Bitcoin


class IcebergCoin(Bitcoin):
    """
    Class with all the necessary IcebergCoin network information based on
    https://github.com/ICBcoin/icebergcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'IcebergCoin'
    symbols = ('ICB', )
    seeds = ("seed.icebergco.in",
             "seed.shurpool.com",
             "embi.zapto.org")
    port = 20703
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 103,
        'SCRIPT_ADDR': 43,
        'SECRET_KEY': 231
    }

# No testnet
