import inspect
import importlib.util
import ipaddress
import os
import sys

from pytest import mark

sys.path.append(os.getcwd())  # noqa

from clove.network.bitcoin import Bitcoin

networks = sorted([file for file in os.listdir('network') if file not in ('__init__.py', '__pycache__')])


def test_filename():
    for filename in os.listdir('network'):
        assert not filename[0].isdigit(), \
            'Python filename cannot start with digit: ' + filename


@mark.parametrize('filename', networks)
def test_network_definition(filename):
    spec = importlib.util.spec_from_file_location(
        'module.name',
        f'network/{filename}'
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    classes = []
    members = dir(module)
    assert 'Bitcoin' in members, 'Not importing Bitcoin'
    for member in dir(module):
        if member.startswith('__') or member == 'Bitcoin':
            continue
        item = getattr(module, member)
        if inspect.isclass(item) and issubclass(item, Bitcoin):
            classes.append(item)

    assert len(classes) in (1, 2)

    # testing names
    if len(classes) == 2:
        names = sorted([cls.__name__ for cls in classes])
        assert f'{names[0]}TestNet' == names[1]

        # checking the same port and seeds/nodes
        if classes[0].port == classes[1].port:
            assert classes[0].seeds + classes[0].nodes != classes[1].seeds + classes[1].nodes, \
                f'[{filename}] mainet and testnet cannot use the same seeds/nodes and ports.'

        if classes[0].seeds + classes[0].nodes == classes[1].seeds + classes[1].nodes:
            assert classes[0].port != classes[1].port
    else:
        assert not classes[0].__name__.endswith('TestNet')

    # testing fields
    for network in classes:
        assert '_' not in network.__name__, '{} is not a valid python class name (remove _)'.format(network.__name__)
        assert isinstance(network.name, str)
        assert isinstance(network.symbols, tuple)
        assert isinstance(network().default_symbol, str)
        assert getattr(network, 'seeds') or getattr(network, 'nodes'), f'[{network.__name__}] no seeds and nodes'
        if hasattr(network, 'seeds'):
            assert isinstance(network.seeds, tuple)
            for seed in network.seeds:
                try:
                    ipaddress.ip_address(seed)
                    ip = True
                except ValueError:
                    ip = False
                assert not ip, 'IP found instead of a domain: {}'.format(seed)
        else:
            assert isinstance(network.nodes, tuple)
            for node in network.nodes:
                if node.endswith('.onion'):
                    continue
                assert ipaddress.ip_address(node)
        assert isinstance(network.port, int)
        assert isinstance(network.blacklist_nodes, dict)
