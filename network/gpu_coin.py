from clove.network.bitcoin import Bitcoin


class Gpucoin(Bitcoin):
    """
    Class with all the necessary GPU Coin (GPU) network information based on
    https://github.com/white92d15b7/gpu-coin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'gpucoin'
    symbols = ('GPU', )
    seeds = ('node1.gpucoin.market',
             'node2.gpucoin.market', 'node3.gpucoin.market')
    port = 6897
    message_start = b'\x9f\x18\x0a\x16'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 166
    }


class GpucoinTestNet(Gpucoin):
    """
    Class with all the necessary GPU Coin (GPU) testing network information based on
    https://github.com/white92d15b7/gpu-coin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-gpucoin'
    seeds = ()
    port = 16897
    message_start = b'\x46\x71\xf7\x5e'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
