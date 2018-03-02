from clove.network.bitcoin import Bitcoin


class UnitedArabEmiratesCoin(Bitcoin):
    """
    Class with all the necessary United Arab Emirates Coin network information based on
    https://github.com/uaecoin/UAECOIN-United-Arab-Emirates-Coin/blob/master/src/net.cpp
    (date of access: 02/13/2018)
    """
    name = 'united_arab_emirates_coin'
    symbols = ('UAEC', )
    nodes = ("107.155.87.16", )
    port = 44887
    message_start = b'\xaa\xa2\xb2\xc4'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 16,
        'SECRET_KEY': 196
    }

# Has no testnet
