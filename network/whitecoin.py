from clove.network.bitcoin import Bitcoin


class Whitecoin(Bitcoin):
    """
    Class with all the necessary Whitecoin (XWC) network information based on
    https://github.com/Whitecoin-org/whitecoin/blob/master/src/chainparams.cpp
    (date of access: 02/16/2018)
    """
    name = 'whitecoin'
    symbols = ('XWC', )
    seeds = ('dnsseed.oizopower.nl', 'dnsseed-cn.whitecoin.info', 'seed1.oizopower.nl',
             'seed2.oizopower.nl', 'seed3.oizopower.nl', 'xwcseeder.ftc-c.com')
    port = 15814
    message_start = b'\x18\x2d\x43\xf3'
    base58_prefixes = {
        'PUBKEY_ADDR': 73,
        'SCRIPT_ADDR': 87,
        'SECRET_KEY': 201
    }

# no testnet
