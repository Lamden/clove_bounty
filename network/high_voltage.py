from clove.network.bitcoin import Bitcoin


class HighVoltage(Bitcoin):
    """
    Class with all the necessary HighVoltage network information based on
    https://github.com/highvoltagecoin/highvoltagecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'highvoltage'
    symbols = ('HVCO', )
    seeds = ("seeder1.highvoltagecoin.tech", "seeder2.highvoltagecoin.tech")
    port = 47824
    message_start = b'\xb1\xb6\xf8\xa6'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 168
    }


# has no testnet
