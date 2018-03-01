from clove.network.bitcoin import Bitcoin


class ManetCoin(Bitcoin):
    """
    Class with all the necessary Manet_Coin network information based on
    https://github.com/Manetcoin/mat-source/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'manet_coin'
    symbols = ('MAT', )
    seeds = ("node.45.76.117.168", )
    port = 17795
    message_start = b'\x95\xde\x8a\x8d'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 178
    }

# no testnet
