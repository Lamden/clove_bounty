from clove.network.bitcoin import Bitcoin


class LuckChain(Bitcoin):
    """
    Class with all the necessary LuckChain network information based on
    https://github.com/luckbash/bash/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'LuckChain'
    symbols = ('BASH', )
    seeds = ("seed.luckchain.org",
             "node.luckchain.org",
             "pool.luckchain.org",
             "s4.luckchain.org",
             "s5.luckchain.org",
             "s6.luckchain.org",
             "s7.luckchain.org",
             "s8.luckchain.org",
             "s9.luckchain.org",
             "abe.luckchain.org",
             "faucet.luckchain.org",
             "s1.bitnet.cc",
             "s2.bitnet.cc",
             "s3.bitnet.cc",
             "s4.bitnet.cc",
             "s5.bitnet.cc",
             "s6.bitnet.cc",
             "s7.bitnet.cc",
             "s8.bitnet.cc",
             "s9.bitnet.cc")
    port = 20168


# Has no testnet
