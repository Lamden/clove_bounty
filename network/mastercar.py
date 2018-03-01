from clove.network.bitcoin import Bitcoin


class MasterCar(Bitcoin):
    """
    Class with all the necessary MasterCar network information based on
    https://github.com/TotalPanda/Mastercar/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'mastercar'
    symbols = ('MCAR', )
    seeds = ("52.28.35.168")
    port = 10333
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 178
    }

# no testnet
