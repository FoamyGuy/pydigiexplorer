import json
import time
from pprint import pprint
import requests

try:
    import thread
except ImportError:
    import _thread as thread
import websocket

import pydigiexplorer as digi

API_URL = "https://digiexplorer.info/"
WS_URL = "wss://digiexplorer.info/"

def ws_listen(on_transcation, on_block):
    def ping(*args):
        time.sleep(30)
        print(">>> Ping...")
        ws.send('2')

    def subscribe(*args):
        ws.send('2probe')

    def on_message(ws, message):
        #print("message received:\n{}".format(message))

        if message == "3probe":
            print("Subscribing to inv...")
            ws.send("5")
            ws.send('425["subscribe", "inv"]')

        if message == '42["subscribed"]':
            thread.start_new_thread(ping, ())

        if message == "3":
            print("<<< Pong...")
            thread.start_new_thread(ping, ())

        if '["block",' in message:
            hash = message.replace('42["block","', '')
            hash = hash.replace('"]', '')
            if on_block is not None:
                on_block(hash)
            #pprint(digi.block(hash))

        if '["tx"' in message:
            tx_info = message.replace('42["tx",', '')
            tx_info = tx_info.replace(']', '')
            if on_transcation is not None:
                on_transcation(json.loads(tx_info))
            #print(txid)

    def on_error(ws, error):
        print("error")
        print(error)

    def on_close(ws):
        print("### Socket Closed ###")

    def on_open(ws):
        print("### Socket Opened ###")
        thread.start_new_thread(subscribe, ())

    millis = int(round(time.time() * 1000))
    r = requests.get(API_URL + "socket.io/?EIO=2&transport=polling&t={}-0".format(millis))
    sid = r.headers['Set-Cookie'].split('io=')[1]
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        WS_URL + "socket.io/?EIO=2&transport=websocket&sid={}".format(sid),
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()