from clove.network.bitcoin import Bitcoin


class SaveTheOcean(Bitcoin):
    """
    Class with all the necessary Save The Ocean network information based on
    https://github.com/SaveTheOceanMovement/SaveTheOceanCoin/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'save_the_ocean'
    symbols = ('STO', )
    nodes = ("52.169.14.55", )
    port = 4555
    message_start = b'\xd1\xa3\xb4\xc2'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 191
    }

# no testnet
