from clove.network.bitcoin import Bitcoin


class TakCoin(Bitcoin):
    """
    Class with all the necessary TakCoin network information based on
    https://github.com/takcoindevcoin/tak/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'takcoin'
    symbols = ('TAK', )
    seeds = ("node.walletbuilders.com")
    port = 32965
    message_start = b'\x6f\xc1\xd5\xb7'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 193
    }

# no testnet
