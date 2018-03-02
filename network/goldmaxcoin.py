from clove.network.bitcoin import Bitcoin


class GoldMaxCoin(Bitcoin):
    """
    Class with all the necessary GoldMaxCoin (GMX) network information based on
    https://github.com/gmx16/goldmaxcoin-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'goldmaxcoin'
    symbols = ('GMX', )
    seeds = ('node.walletbuilders.com', )
    port = 6309
    message_start = b'\x42\x29\x0e\xb6'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }

# no testnet
