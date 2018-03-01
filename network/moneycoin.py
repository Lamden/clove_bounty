from clove.network.bitcoin import Bitcoin


class MoneyCoin(Bitcoin):
    """
    Class with all the necessary MoneyCoin network information based on
    https://github.com/moneyproject/moneycoin/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'moneycoin'
    symbols = ('MONEY', )
    seeds = ("seed.moneycoin.pw", )
    port = 15554
    message_start = b'\xa1\x2b\x1f\xb1'
    base58_prefixes = {
        'PUBKEY_ADDR': 50,
        'SCRIPT_ADDR': 125,
        'SECRET_KEY': 191
    }

# no testnet
