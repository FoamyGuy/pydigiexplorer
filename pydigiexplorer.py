import json
from pprint import pprint
import requests

API_URL = "https://digiexplorer.info/api/"

def block(hash):
    return json.loads(requests.get(API_URL + "block/%s/" % hash).content.decode("utf-8"))

def block_index(index):
    hash = json.loads(requests.get(API_URL + "block-index/%s/" % index).content.decode("utf-8"))['blockHash']
    print(hash)
    return block(hash)

def blocks(limit=10, blockDate=None):
    return json.loads(requests.get(API_URL + "blocks?limit=%s&blockDate=%s" % (limit, blockDate)).content.decode("utf-8"))

def transaction(txid):
    return json.loads(requests.get(API_URL + "tx/%s/" % txid).content.decode("utf-8"))

def transactions(block_hash=None, address=None):
    if block_hash:
        return json.loads(requests.get(API_URL + "txs/?block=%s" % block_hash).content.decode("utf-8"))
    if address:
        return json.loads(requests.get(API_URL + "txs/?address=%s" % address).content.decode("utf-8"))

def transactions_for_multiple_addresses(addrs):
    addrs_str = ",".join(addrs)
    return json.loads(requests.get(API_URL + "addrs/%s/txs/" % addrs_str).content.decode("utf-8"))

def address(addr):
    return json.loads(requests.get(API_URL + "addr/%s/" % addr).content.decode("utf-8"))

def address_balance(addr):
    return json.loads(requests.get(API_URL + "addr/%s/balance/" % addr).content.decode("utf-8"))

def address_total_received(addr):
    return json.loads(requests.get(API_URL + "addr/%s/totalReceived/" % addr).content.decode("utf-8"))

def address_total_sent(addr):
    return json.loads(requests.get(API_URL + "addr/%s/totalSent/" % addr).content.decode("utf-8"))

def address_unconfirmed_balance(addr):
    return json.loads(requests.get(API_URL + "addr/%s/unconfirmedBalance/" % addr).content.decode("utf-8"))

def address_utxo(addr):
    return json.loads(requests.get(API_URL + "addr/%s/utxo/" % addr).content.decode("utf-8"))

def addresses_utxo(addrs):
    addrs_str = ",".join(addrs)
    print(addrs_str)
    return json.loads(requests.get(API_URL + "addrs/%s/utxo/" % addrs_str).content.decode("utf-8"))




#pprint(blocks(limit=10, blockDate="2014-01-10"))
#pprint(addresses_utxo(["DJR9SuYSZMs353xuV4nj5Ro6cmFQ2iphtw", "DNHX9Ae6ZxyVVNNt9NtqVbMRMKBsxKbfXM"]))
pprint(transactions_for_multiple_addresses(["DJR9SuYSZMs353xuV4nj5Ro6cmFQ2iphtw", "DNHX9Ae6ZxyVVNNt9NtqVbMRMKBsxKbfXM"]))
#pprint(block_index(1191987))