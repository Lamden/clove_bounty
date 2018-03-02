from clove.network.bitcoin import Bitcoin


class PRCoin(Bitcoin):
    """
    Class with all the necessary PRCoin network information based on
    https://github.com/prcoin/prcoin-wallet
    (date of access: 02/19/2018)
    """
    name = 'prcoin'
    symbols = ('PRC', )
    nodes = ("73.78.96.65", "218.144.45.133")
    port = 8535
    message_start = b'\xef\xc1\x40\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 183
    }

# no testnet
