from clove.network.bitcoin import Bitcoin


class Diem(Bitcoin):
    """
    Class with all the necessary Diem network information based on
    https://github.com/diemcoin/carpediemcoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'diem'
    symbols = ('DIEM', )
    seeds = ("dnsseed.carpediemexplorer.com", )
    port = 9449
    message_start = b'\xe4\xe8\xe9\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 30,
        'SCRIPT_ADDR': 75,
        'SECRET_KEY': 158
    }

# Has no testnet
