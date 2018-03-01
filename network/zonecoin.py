from clove.network.bitcoin import Bitcoin


class Zonecoin(Bitcoin):
    """
    Class with all the necessary Zonecoin network information based on
    https://github.com/st4yinth3d4rk/zonecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'zonecoin'
    symbols = ('ZNE', )
    seeds = ("46.101.95.7", "146.185.147.21")
    port = 7901
    message_start = b'\x4e\x64\x92\x74'
    base58_prefixes = {
        'PUBKEY_ADDR': 80,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 208
    }


# Has no testnet
