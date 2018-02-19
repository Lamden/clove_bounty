from clove.network.bitcoin import Bitcoin


class Vault_Coin(Bitcoin):
    """
    Class with all the necessary Vault_Coin network information based on
    https://github.com/Vaultcoins/Vaultcoins/blob/master-0.8/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'vault_coin'
    symbols = ('VLTC', )
    seeds = ("162.250.125.26",
             "120.145.149.109")
    port = 15050
	
   
class Vault_CoinTestNet(Vault_Coin):
    """
    Class with all the necessary Vault_Coin testing network information based on
    https://github.com/Vaultcoins/Vaultcoins/blob/master-0.8/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-vault_coin'
    seeds = ("testnet-seed.vaultcointools.com",
             "testnet-seed.weminemnc.com")
    port = 25050              
	

	
	

	