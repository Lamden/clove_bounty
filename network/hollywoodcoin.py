from clove.network.bitcoin import Bitcoin


class HollywoodCoin(Bitcoin):
    """
    Class with all the necessary HollywoodCoin (HWC) network information based on
    https://github.com/Hollywoodcoiin/hollywood_team/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'hollywoodcoin'
    symbols = ('HWC', )
    seeds = ('seed.hollywoodcoin.biz', )
    port = 10267
    message_start = b'\x3b\x40\x9d\x4f'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 168
    }

# no testnet
