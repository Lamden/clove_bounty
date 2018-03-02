from clove.network.bitcoin import Bitcoin


class DigiCube(Bitcoin):
    """
    Class with all the necessary DigiCube network information based on
    https://github.com/iGotSpots/DigiCube/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'digicube'
    symbols = ('CUBE', )
    seeds = ("digicubeseeds.freestaking.com", )
    port = 8888
    message_start = b'\xba\xcb\xdc\xad'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 117,
        'SECRET_KEY': 156
    }

# no testnet
