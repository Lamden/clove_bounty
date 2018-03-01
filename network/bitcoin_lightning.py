from clove.network.bitcoin import Bitcoin


class BitcoinLightning(Bitcoin):
    """
    Class with all the necessary Bitcoin Lightning (BLT) network information based on
    https://github.com/Bitcoinlightning/Bitcoin-Lightning/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'bitcoinlightning'
    symbols = ('BLT', )
    seeds = ('165.227.219.245', '159.89.38.145',
             '159.89.47.190', '159.89.40.45')
    port = 17127
    message_start = b'\x1c\x4e\xb6\xc3'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
