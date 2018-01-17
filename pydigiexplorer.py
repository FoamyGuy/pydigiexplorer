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

def sync_info():
    return json.loads(requests.get(API_URL + "sync/").content.decode("utf-8"))

def peer_info():
    return json.loads(requests.get(API_URL + "peer/").content.decode("utf-8"))

def status_info():
    return json.loads(requests.get(API_URL + "status/?q=getInfo").content.decode("utf-8"))

def status_difficulty():
    return json.loads(requests.get(API_URL + "status/?q=getDifficulty").content.decode("utf-8"))

def status_best_block_hash():
    return json.loads(requests.get(API_URL + "status/?q=getBestBlockHash").content.decode("utf-8"))

def status_last_block_hash():
    return json.loads(requests.get(API_URL + "status/?q=getLastBlockHash").content.decode("utf-8"))



#pprint(blocks(limit=10, blockDate="2014-01-10"))
#pprint(addresses_utxo(["DJR9SuYSZMs353xuV4nj5Ro6cmFQ2iphtw", "DNHX9Ae6ZxyVVNNt9NtqVbMRMKBsxKbfXM"]))
#pprint(transactions_for_multiple_addresses(["DJR9SuYSZMs353xuV4nj5Ro6cmFQ2iphtw", "DNHX9Ae6ZxyVVNNt9NtqVbMRMKBsxKbfXM"]))
#pprint(block("5136e9a8962bd7ca4deb887135d353fab7e74d40faaddf7e9410aa7065247f03"))

#pprint(addresses_utxo(["DT19owMp6fXWJWxTASg62KAXUcNwQwSJtN", "DJnqfjzRFUYHoUEgKWhptxB73cGshfHaPe"]))
#pprint(status_last_block_hash())

#pprint(block("21f98a20612b75d63e68cdf11f196f68e16b0d29d0ac4c8e75a2fe11ec5afae8"))
#pprint(block_index(1191987))

#pprint(address_utxo("DU3GN9DHPBFwAnZbk5YDhLmXZZi2599BYC"))

"""
Javascript socket implementation
var socket = io("http://<insight-server>:<port>/");
socket.on('connect', function() {
  // Join the room.
  socket.emit('subscribe', room);
})
socket.on(eventToListenTo, function(data) {
  console.log("New transaction received: " + data.txid)
})
"""

