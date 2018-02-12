from clove.network.bitcoin import Bitcoin


class Paycon(Bitcoin):
    """
    Class with all the necessary CON network information based on
    https://github.com/cryptotech/paycon/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'paycon'
    symbols = ('CON', )
    seeds = (
        'zaqxschmq4bfj64d.onion',
        'xnmbxhbbhngvp5ea.onion',
        '4rvjnfn5wiyk2aqp.onion',
        'sun6z3scsrloydgf.onion',
        'rgz3eevnrwjvnozm.onion',
        'xuzhdunw6pm2cnxo.onion',
        '3tkpjldbbidxwfv3.onion',
        'pjxv27nvd4ce32xb.onion',
        'as6l375o37zaif3w.onion',
        'v2s6pz5ipuey457f.onion',
        '62jhprfz3abtkvbe.onion',
        'keqtj27fa6hn3xu7.onion',
        'hlgv4zokymhz26tx.onion',
        'dfuwr2vvbxm6dx3k.onion',
        '4363xyabb3hkjocd.onion',
        'tfxfu7yxe5dkauwf.onion',
        'xnmbxhbbhngvp5ea.onion',
        'ev6uqghx5jjfotep.onion',
        'ndawxkpfmjgbmycd.onion',
        'yey3rnjdsdc77rrp.onion',
        'j7dsfqsdt6pjedvq.onion',
    )
    port = 9455


class PayconTestNet(Paycon):
    """
    Class with all the necessary CON testing network information based on
    https://github.com/cryptotech/paycon/blob/master/src/net.cpp
    (date of access: 01/18/2018)
    """
    name = 'test-paycon'
    seeds = ()
    port = 25072
