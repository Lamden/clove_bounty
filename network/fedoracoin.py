from clove.network.bitcoin import Bitcoin


class FedoraCoin(Bitcoin):
    """
    Class with all the necessary FedoraCoin (TIPS) network information based on
    https://github.com/fedoracoin-dev/fedoracoin/blob/master-0.9/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'fedoracoin'
    symbols = ('TIPS', )
    seeds = ('seed.fedoracoin.net', 'tips1.netcraft.ch', 'tips2.netcraft.ch')
    port = 44890
    message_start = b'\xde\xad\x13\x37'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 128
    }


class FedoraCoinTestNet(FedoraCoin):
    """
    Class with all the necessary FedoraCoin (TIPS) testing network information based on
    https://github.com/fedoracoin-dev/fedoracoin/blob/master-0.9/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-fedoracoin'
    seeds = ('testnet-dnsseed.fedoracoin.com', )
    port = 19336
    message_start = b'\xda\xaf\xa5\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 193
    }
