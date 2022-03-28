import random as rd
import pprint as pp
import bitcoinrpc.authproxy as ba
import tkinter as tk
import tkinter.scrolledtext as ts 
import matplotlib.figure as fig
import matplotlib.backends.backend_tkagg as bac

ip_1 = '136.167.123.200'
ip_2 = '136.167.46.223'
rpc_1 = ''
rpc_2 = ''
wallet_1 = 'Alice'
wallet_2 = 'Bob'
wallet_3 = 'John'
addr_1 = ''
addr_2 = ''
joined = False
update_ms = 1000

def JoinNodes():
    global joined
    try:
        if joined:
            rpc_1.disconnectnode(ip2_entry.get().strip() + ':18444')
        else:
            rpc_1.addnode(ip2_entry.get().strip() + ':18444', 'add')
    except:
        block1_entry.set('No connection')

def UpdateStatus():
    global joined
    global rpc_1
    global rpc_2
    global rpc_3
    try:
        nodes = rpc_1.getaddednodeinfo()
        for node in nodes:
            if node['addednode'] == ip2_entry.get().strip() + ':18444':
                joined = node['connected']
                if joined:
                    join_entry.set('Joined')
                else:
                    join_entry.set('Seperated')
        utxo = rpc_1.listunspent()
        utxo1_list.delete(0, tk.END)
        for tx in utxo:
            utxo1_list.insert(tk.END, tx['txid'])
            utxo1_list.insert(tk.END, '          TxOut Balance (BTC) = ' + str(tx['amount']))
        balance_1 = rpc_1.getbalance()
        balance_3 = rpc_3.getbalance()
        balance1_entry.set(round(balance_1,4))
        balance3_entry.set(round(balance_3,4))
        blocks = rpc_1.getblockcount()
    except:
        join_entry.set('')
        blocks = 'No connection'
    block1_entry.set(blocks)
        
    try:
        utxo = rpc_2.listunspent()
        utxo2_list.delete(0, tk.END)
        for tx in utxo:
            utxo2_list.insert(tk.END, tx['txid'])
            utxo2_list.insert(tk.END, '          TxOut Balance (BTC) = ' + str(tx['amount']))
        balance_2 = rpc_2.getbalance()            
        balance2_entry.set(round(balance_2,4))
        blocks = rpc_2.getblockcount()
    except:
        blocks = 'No connection'
    block2_entry.set(blocks)
    my_win.after(update_ms, UpdateStatus)

def ConnectNode1():
    global rpc_1
    global rpc_3
    global addr_1
    global addr_3
    url = 'http://bit:coin@' + ip1_entry.get() + ':18888/wallet/'+wallet_1
    url_3 = 'http://bit:coin@' + ip1_entry.get() + ':18888/wallet/'+wallet_3
    rpc_1 = ba.AuthServiceProxy(url, timeout=10)
    rpc_3 = ba.AuthServiceProxy(url_3, timeout=10)
    try:
        addr_1 = rpc_1.getnewaddress()
        addr_3 = rpc_3.getnewaddress()
    except:
        addr_1 = 'Alice does not exist'
        addr_3 = 'John does not exist'
    addr1_entry.set(addr_1)
    addr3_entry.set(addr_3)

def ConnectNode2():
    global rpc_2
    global addr_2
    url = 'http://bit:coin@' + ip2_entry.get() + ':18888/wallet/'+wallet_2
    rpc_2 = ba.AuthServiceProxy(url, timeout=10)
    try:
        addr_2 = rpc_2.getnewaddress()
    except:
        addr_2 = 'Bob does not exist'
    addr2_entry.set(addr_2)    

def Payment1():
    if pass_entry.get().strip() == pass_code:
        txout = pmt1_txout.get().strip()
        tx_dict = {'txid':txout, 'vout':0}
        addr_amt = {pmt1_to.get().strip():float(pmt1_amt.get().strip())}
        rawtx_id = rpc_1.createrawtransaction([tx_dict], [addr_amt])  
        raw_tx = rpc_1.signrawtransactionwithwallet(rawtx_id)['hex']
        rawtx1_entry.set(raw_tx)
    
def Payment2():
    if pass_entry.get().strip() == pass_code:
        txout = pmt2_txout.get().strip()
        tx_dict = {'txid':txout, 'vout':0}
        addr_amt = {pmt2_to.get().strip():float(pmt2_amt.get().strip())}
        rawtx_id = rpc_2.createrawtransaction([tx_dict], [addr_amt])
        raw_tx = rpc_2.signrawtransactionwithwallet(rawtx_id)['hex']
        rawtx2_entry.set(raw_tx)

def Broadcast1():
    if pass_entry.get().strip() == pass_code:
        raw_tx = rawtx1_entry.get().strip()
        tx_id = rpc_1.sendrawtransaction(raw_tx)
        pmt1_txid.set(tx_id)

def Broadcast2():
    if pass_entry.get().strip() == pass_code:
        raw_tx = rawtx2_entry.get().strip()
        tx_id = rpc_2.sendrawtransaction(raw_tx)
        pmt2_txid.set(tx_id)

def GodMoney1():
    if pass_entry.get().strip() == pass_code:
        tx = rpc_1.generatetoaddress(1, addr_1)

def GodMoney2():
    if pass_entry.get().strip() == pass_code:
        tx = rpc_2.generatetoaddress(1, addr_2)

def Mining1():
    if pass_entry.get().strip() == pass_code:
        rpc_1.generatetoaddress(100, 'bcrt1q74knn7lm3dv4026jdg0wl090qcmw4ty54seeyz')

def Mining2():
    if pass_entry.get().strip() == pass_code:
        rpc_2.generatetoaddress(100, 'bcrt1q74knn7lm3dv4026jdg0wl090qcmw4ty54seeyz')

my_win = tk.Tk()
my_win.geometry('950x600')
my_win.title('Bitcoin Node Monitors')

join_entry = tk.StringVar()
tk.Entry(my_win, textvariable=join_entry, width=10).place(x=400,y=5)
tk.Button(master=my_win, text="Join", command = JoinNodes).place(x=470,y=1)

tk.Label(my_win, text = 'FIRST BITCOIN NODE').place(x=140,y=10)
tk.Label(my_win, text = 'IP Address:').place(x=10,y=40)
ip1_entry = tk.StringVar()
ip1_entry.set(ip_1)
tk.Entry(my_win, textvariable = ip1_entry).place(x=110,y=40)
tk.Button(master=my_win, text="Connect", command = ConnectNode1).place(x=270,y=40)

tk.Label(my_win, text = 'Total Blocks:').place(x=10,y=70)
block1_entry = tk.StringVar()
tk.Entry(my_win, textvariable = block1_entry).place(x=110,y=70)

tk.Label(my_win, text = "Alice's Bitcoin:").place(x=10,y=100)
addr1_entry = tk.StringVar()
tk.Entry(my_win, textvariable = addr1_entry, width=40).place(x=110,y=100)
balance1_entry = tk.StringVar()
tk.Entry(my_win, textvariable = balance1_entry, width=7).place(x=360,y=100)
tk.Label(my_win, text = "BTC").place(x=410,y=100)

tk.Label(my_win, text = 'Unspent Transaction Output (UTXO):').place(x=10,y=130)
frame_1 = tk.Frame(my_win)
frame_1.place(x=10,y=160)
utxo1_bar = tk.Scrollbar(frame_1, orient=tk.VERTICAL)
utxo1_list = tk.Listbox(frame_1, yscrollcommand = utxo1_bar.set, width=70, height=6)
utxo1_list.pack(side=tk.LEFT)
utxo1_bar.config(command = utxo1_list.yview)
utxo1_bar.pack(side=tk.RIGHT, fill=tk.Y)

tk.Label(my_win, text='Fund Source:').place(x=10,y=280)
pmt1_txout = tk.StringVar()
tk.Entry(my_win, textvariable=pmt1_txout, width=40).place(x=90,y=280)
tk.Label(my_win, text='Pay To:').place(x=10,y=310)
pmt1_to = tk.StringVar()
tk.Entry(my_win, textvariable=pmt1_to, width=40).place(x=90,y=310)
tk.Label(my_win, text='Amount:').place(x=335,y=280)
pmt1_amt = tk.StringVar()
tk.Entry(my_win, textvariable=pmt1_amt, width=7).place(x=390,y=280)
tk.Button(master=my_win, text="Pay Now", command = Payment1).place(x=380,y=305)
tk.Label(my_win, text='Raw Tx Data with Payer Signature:').place(x=10,y=340)
rawtx1_entry = tk.StringVar()
tk.Entry(my_win, textvariable=rawtx1_entry, width=70).place(x=10,y=360)

tk.Button(master=my_win, text="Broadcast", command=Broadcast1).place(x=10,y=385)
tk.Label(my_win, text='Transaction ID:').place(x=90,y=390)
pmt1_txid = tk.StringVar()
tk.Entry(my_win, textvariable=pmt1_txid, width=40).place(x=190,y=390)

tk.Label(my_win, text='Alice Asks God for Money').place(x=10,y=500)
tk.Button(master=my_win, text="Oh Lord My God", command=GodMoney1).place(x=155,y=495)

tk.Label(my_win, text = 'Other Random Miners').place(x=10,y=535)
tk.Button(master=my_win, text="Mine 100 blocks", command=Mining1).place(x=157,y=530)

tk.Label(my_win, text = 'SECOND BITCOIN NODE').place(x=630, y=10)
tk.Label(my_win, text = 'IP Address: ').place(x=500, y=40)
ip2_entry = tk.StringVar()
ip2_entry.set(ip_2)
tk.Entry(my_win, textvariable = ip2_entry).place(x=610, y=40)
tk.Button(master=my_win, text="Connect", command = ConnectNode2).place(x=780,y=40)

tk.Label(my_win, text = 'Total Blocks:').place(x=500,y=70)
block2_entry = tk.StringVar()
tk.Entry(my_win, textvariable = block2_entry).place(x=610,y=70)

tk.Label(my_win, text = "Bob's Bitcoin:").place(x=500,y=100)
addr2_entry = tk.StringVar()
tk.Entry(my_win, textvariable = addr2_entry, width=40).place(x=610,y=100)
balance2_entry = tk.StringVar()
tk.Entry(my_win, textvariable = balance2_entry, width=7).place(x=860,y=100)
tk.Label(my_win, text = "BTC").place(x=900,y=100)

tk.Label(my_win, text = 'Unspent Transaction Output (UTXO):').place(x=500,y=130)
frame_2 = tk.Frame(my_win)
frame_2.place(x=500,y=160)
utxo2_bar = tk.Scrollbar(frame_2, orient=tk.VERTICAL)
utxo2_list = tk.Listbox(frame_2, yscrollcommand=utxo2_bar.set, width=70, height=6)
utxo2_list.pack(side=tk.LEFT)
utxo2_bar.config(command = utxo2_list.yview)
utxo2_bar.pack(side=tk.RIGHT, fill=tk.Y)

tk.Label(my_win, text='Fund Source:').place(x=500,y=280)
pmt2_txout = tk.StringVar()
tk.Entry(my_win, textvariable=pmt2_txout, width=40).place(x=580,y=280)
tk.Label(my_win, text='Pay To:').place(x=500,y=310)
pmt2_to = tk.StringVar()
tk.Entry(my_win, textvariable=pmt2_to, width=40).place(x=580,y=310)
tk.Label(my_win, text='Amount:').place(x=825,y=280)
pmt2_amt = tk.StringVar()
tk.Entry(my_win, textvariable=pmt2_amt, width=7).place(x=880,y=280)
tk.Button(master=my_win, text="Pay Now", command=Payment2).place(x=870,y=305)

tk.Label(my_win, text='Raw Tx Data with Payer Signature:').place(x=500,y=340)
rawtx2_entry = tk.StringVar()
tk.Entry(my_win, textvariable=rawtx2_entry, width=70).place(x=500,y=360)

tk.Button(master=my_win, text="Broadcast", command=Broadcast2).place(x=500,y=385)
tk.Label(my_win, text='Transaction ID:').place(x=580,y=390)
pmt2_txid = tk.StringVar()
tk.Entry(my_win, textvariable=pmt2_txid, width=40).place(x=680,y=390)

tk.Label(my_win, text = "Alice's Mafia Friend John:").place(x=270,y=450)
addr3_entry = tk.StringVar()
tk.Entry(my_win, textvariable=addr3_entry, width=40).place(x=410,y=450)
balance3_entry = tk.StringVar()
tk.Entry(my_win, textvariable=balance3_entry, width=7).place(x=660,y=450)
tk.Label(my_win, text = "BTC").place(x=700,y=450)

tk.Label(my_win, text = 'Bob Asks God for Money').place(x=690,y=500)
tk.Button(master=my_win, text="Oh Lord My God", command=GodMoney2).place(x=830,y=495)

tk.Label(my_win, text = 'Other Random Miners').place(x=690,y=535)
tk.Button(master=my_win, text="Mine 100 blocks", command=Mining2).place(x=832,y=530)

rand_1 = rd.randint(1, 9)
rand_2 = rd.randint(1, 9)
rand_3 = rd.randint(1, 9)
pass_code = str(rand_1 * rand_2 + rand_3)
tk.Label(my_win, text = str(rand_1)+' '+str(rand_2)+' '+str(rand_3)).place(x=460,y=535)
pass_entry = tk.StringVar()
tk.Entry(my_win, textvariable=pass_entry, width=3).place(x=500,y=535)

UpdateStatus()
my_win.mainloop()

