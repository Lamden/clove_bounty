from clove.network.bitcoin import Bitcoin


class Pioneershares(Bitcoin):
    """
    Class with all the necessary Pioneershares network information based on
    https://github.com/BlockPioneers/pioneershares/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'pioneershares'
    symbols = ('PIO', )
    seeds = ("seed.blockpioneers.info", "seed2.blockpioneers.info")
    port = 8572
    message_start = b'\xc3\xc5\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 30,
        'SECRET_KEY': 183
    }

# no testnet
