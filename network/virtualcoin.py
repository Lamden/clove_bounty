from clove.network.bitcoin import Bitcoin


class VirtualCoin(Bitcoin):
    """
    Class with all the necessary VirtualCoin (VC) network information based on
    https://github.com/vcoin-z/virtualcoin/blob/9.2.0/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'virtualcoin'
    symbols = ('VC', )
    seeds = ('dnsseed.vcoin.ca', 'dnsseed.virtualcoin.ca', )
    port = 443
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 70,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 198
    }


class VirtualCoinTestNet(VirtualCoin):
    """
    Class with all the necessary VirtualCoin (VC) testing network information based on
    https://github.com/vcoin-z/virtualcoin/blob/9.2.0/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-virtualcoin'
    seeds = ('testnet-seed.vcoin.ca', 'testnet-seed.virtualcoin.ca', )
    port = 80
    message_start = b'\xfc\xc1\xb7\xdc'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
