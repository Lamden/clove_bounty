from clove.network.bitcoin import Bitcoin


class GCNcoin(Bitcoin):
    """
    Class with all the necessary GCN coin (GCN) network information based on
    https://github.com/GregGeoghegan/GCN-zone-source/blob/master/src/net.cpp
    (date of access: 02/22/2018)
    """
    name = 'gcncoin'
    symbols = ('GCN', )
    seeds = ('225.149.199.33', '49.211.161.66')
    port = 3908
    message_start = b'\xd8\xc7\xef\xeb'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }

# no testnet
