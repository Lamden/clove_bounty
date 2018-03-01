from clove.network.bitcoin import Bitcoin


class Zilbercoin(Bitcoin):
    """
    Class with all the necessary Zilbercoin (ZBC) network information based on
    https://github.com/Zilbercoin/SRC/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'zilbercoin'
    symbols = ('ZBC', )
    seeds = ('node.walletbuilders.com', 'znode2.zilbercoin.space')
    port = 10393
    message_start = b'\x02\xe1\x16\x38'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 158
    }

# no testnet
