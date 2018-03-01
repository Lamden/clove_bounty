from clove.network.bitcoin import Bitcoin


class SpaceCoin(Bitcoin):
    """
    Class with all the necessary SpaceCoin network information based on
    https://github.com/midnight-miner/spacecoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'spacecoin'
    symbols = ('SPACE', )
    seeds = ('seed1.spacecoin.info', 'seed2.spacecoin.info')
    port = 9172
    message_start = b'\xf4\xf2\xf9\xfb'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 52,
        'SECRET_KEY': 191
    }


# Has no testnet
