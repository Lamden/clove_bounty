from clove.network.bitcoin import Bitcoin


class BitcoinPlus(Bitcoin):
    """
    Class with all the necessary Bitcoin Plus (XBC) network information based on
    https://github.com/bitcoinplusorg/xbcwalletsource/blob/origin/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'bitcoinplus'
    symbols = ('XBC', )
    seeds = ('seednode1.bitcoinplus.net', 'seednode2.bitcoinplus.net',
             'seednode3.bitcoinplus.net', 'seednode4.bitcoinplus.net', 'seednode5.bitcoinplus.net')
    port = 8884
    message_start = b'\x2d\x3f\xa2\xf5'
    base58_prefixes = {
        'PUBKEY_ADDR': 25,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
