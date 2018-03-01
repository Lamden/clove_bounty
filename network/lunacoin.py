from clove.network.bitcoin import Bitcoin


class LunaCoin(Bitcoin):
    """
    Class with all the necessary Luna Coin (LUNA) network information based on
    https://github.com/lunawallet/lunawallet/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'lunacoin'
    symbols = ('LUNA', )
    seeds = ('212.24.102.92')
    port = 38353
    message_start = b'\xe4\xa8\xbb\xe5'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 176
    }

# no testnet
