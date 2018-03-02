from clove.network.bitcoin import Bitcoin


class Electra(Bitcoin):
    """
    Class with all the necessary Electra (ECA) network information based on
    https://github.com/Electra-project/Electra/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'electra'
    symbols = ('ECA', )
    nodes = ('35.164.59.217', '212.24.103.180', '139.162.166.112', '158.129.230.143', '217.77.59.45',
             '5.9.73.100', '52.41.97.84', '78.164.100.196', '88.99.249.223', '93.115.61.93')
    port = 5817
    message_start = b'\xb4\xf1\xa2\xb5'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 40,
        'SECRET_KEY': 161
    }

# no testnet
