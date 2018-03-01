from clove.network.bitcoin import Bitcoin


class Paypeer(Bitcoin):
    """
    Class with all the necessary PAYP network information based on
    https://github.com/paypeer/paypeer/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'paypeer'
    symbols = ('PAYP', )
    seeds = (
        'seed1.paypeer.co',
        'seed2.paypeer.co',
        'seed3.paypeer.co',
        'seed4.paypeer.co',
        'ok1.altcoinsfoundation.com',
    )
    port = 33714
    message_start = b'\x13\x02\x1b\x3c'
    base58_prefixes = {
        'PUBKEY_ADDR': 56,
        'SCRIPT_ADDR': 50,
        'SECRET_KEY': 184
    }


class PaypeerTestNet(Paypeer):
    """
    Class with all the necessary PAYP testing network information based on
    https://github.com/paypeer/paypeer/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-paypeer'
    seeds = ()
    port = 33715
    message_start = b'\x3c\x2d\x1e\x0f'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 109,
        'SECRET_KEY': 183
    }
