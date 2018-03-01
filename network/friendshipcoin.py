from clove.network.bitcoin import Bitcoin


class FriendshipCoin2(Bitcoin):
    """
    Class with all the necessary FriendshipCoin2 network information based on
    https://github.com/friendshipCoin/friendshipcoin/blob/master/src/net.cpp
    (date of access: 02/15/2018)
    """
    name = 'friendshipcoin2'
    symbols = ('FSC2', )
    seeds = ("pool.friendshipcoins.com", "blocks.friendshipcoins.com")
    port = 37636
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 96,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 224
    }

# no testnet
