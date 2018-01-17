from pydigiexplorer_websocket import ws_listen
from pprint import pprint

def on_block(hash):
    print("block: %s" % hash)


def on_transaction(tx_info):
    pprint(tx_info)


ws_listen(on_transaction, on_block)