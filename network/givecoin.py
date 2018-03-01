from clove.network.bitcoin import Bitcoin


class GiveCoin(Bitcoin):
    """
    Class with all the necessary GiveCoin network information based on
    https://github.com/Givecoin/givecoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'givecoin'
    symbols = ('GIVE', )
    seeds = ("givecoin.no-ip.biz",
             "5.250.177.28",
             "66.172.12.54")
    port = 31415
    message_start = b'\xd1\xd2\xd3\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 15,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 143
    }

# no testnet
