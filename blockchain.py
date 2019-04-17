############################################################
###  Project is mostly conceptual for learning purposes  ###
############################################################

# Initializing a genesis block
genesis_block = {"previous_hash": "",
                 "index": 0,
                 "transactions": []
                 }
# Initializing blockchain list and transaction list
blockchain = [genesis_block]
open_transactions = []

# Setting dummyvalue for owner
owner = "Max"
participants = {"Max"}

def hash_block(block):
    return "-".join([str(block[key]) for key in block])

# Function for getting last blockchain value
def get_last_blockchain_value():
    """ Finds the last element in list by finding the
        first value from the opposite direction (-1 as opposed to 1) """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# Function for adding a value to the blockchain
def add_transaction(recipient, sender=owner, amount=1.0):
    """
    Appends last transaction and new transaction amount to the blockchain list
    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount being transfered
    """
    transaction = {"sender": sender,
                   "recipient": recipient,
                   "amount": amount
                   }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


# Function for mining a block
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)

    block = {"previous_hash": hashed_block,
             "index": len(blockchain),
             "transactions": open_transactions
             }
    blockchain.append(block)

# Function for getting transaction amount as input
def get_transaction_amount():
    """ Returns input/transaction amount as float """
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Your amount for transaction: "))
    return (tx_recipient, tx_amount)


# Function for getting user choice/input
def get_user_choice():
    return input("Your choice: ")


# Function to print every element of blockchain list
def print_blockchain_elements():
    # Outputs blockchain list to console
    print("-" * 30)
    for block in blockchain:
        print("Outputting Block")
        print(block)
    print("-" * 30)


# Function to verify the chain
def verify_chain():
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True



def get_balance(participant):
    tx_sender = [[tx["amount"] for tx in block["transactions"] if tx["sender"] == participant] for block in blockchain]
    return tx_sender

waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction")
    print("2: Mine a new block")
    print("3: Output blockchain blocks")
    print("4: Output participants")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()

    if (user_choice == "1"):
        tx_data = get_transaction_amount()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)

    elif (user_choice == "2"):
        if mine_block():
            open_transactions = []

    elif (user_choice == "3"):
        print_blockchain_elements()

    elif (user_choice == "4"):
        print(participants)

    elif (user_choice == "q"):
        waiting_for_input = False

    elif (user_choice == "h"):
        if len(blockchain) >= 1:
            blockchain[0] = {"previous_hash": "",
                             "index": 0,
                             "transactions": [{"sender": "Chris", "recipient": "Max", "amount": 100.0}]
                             }

    else:
        print("-" * 30)
        print("Wrong input, try again!")
        print("-" * 30)
    if not verify_chain():
        print("Invalid blockchain")
        break
    print(get_balance("Max"))
    print(open_transactions)
    print(blockchain)
else:
    print("-" * 30)
    print("EXITING...")
    print("-" * 30)
