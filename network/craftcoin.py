from clove.network.bitcoin import Bitcoin


class CraftCoin(Bitcoin):
    """
    Class with all the necessary Diamond network information based on
    https://github.com/craftcoin/craftcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'craftcoin'
    symbols = ('CRC', )
    seeds = ("smp1.spendlitecoins.com", )
    port = 12124
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 57,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 185
    }

# Has no testnet
