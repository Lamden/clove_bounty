from clove.network.bitcoin import Bitcoin


class LoMoCoin(Bitcoin):
    """
    Class with all the necessary LoMoCoin network information based on
    https://github.com/lomocoin/lomocoin-qt/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'lomocoin'
    symbols = ('LMC', )
    seeds = ("seed.lomocoin.com", )
    port = 6801
    message_start = b'\xa6\xb8\xc9\xd5'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 176
    }

# no testnet
