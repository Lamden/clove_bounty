from clove.network.bitcoin import Bitcoin


class VaultCoin(Bitcoin):
    """
    Class with all the necessary Vault_Coin network information based on
    https://github.com/Vaultcoins/Vaultcoins/blob/master-0.8/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'vault_coin'
    symbols = ('VLTC', )
    nodes = ("162.250.125.26",
             "120.145.149.109")
    port = 15050
    message_start = b'\xeb\xd0\xc6\xeb'
    base58_prefixes = {
        'PUBKEY_ADDR': 71,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 199
    }


class VaultCoinTestNet(VaultCoin):
    """
    Class with all the necessary Vault_Coin testing network information based on
    https://github.com/Vaultcoins/Vaultcoins/blob/master-0.8/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-vault_coin'
    seeds = ("testnet-seed.vaultcointools.com",
             "testnet-seed.weminemnc.com")
    port = 25050
    message_start = b'\xcc\xd1\xe7\xe1'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
