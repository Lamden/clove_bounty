from clove.network.bitcoin import Bitcoin


class KubosCoin(Bitcoin):
    """
    Class with all the necessary KubosCoin network information based on
    https://github.com/KUBOSCOIN/kubos/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'kuboscoin'
    symbols = ('KUBO', )
    seeds = ("node.walletbuilders.com")
    port = 7715
    message_start = b'\xf2\x05\x42\x70'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 173
    }
