# Initializing blockchain list
blockchain = []


# Function for getting last blockchain value
def get_last_blockchain_value():
    """ Finds the last element in list by finding the
        first value from the opposite direction (-1 as opposed to 1) """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


# Function for adding a value to the blockchain
def add_transaction(transaction_amount, last_transaction=[1]):
    """ Appends last transaction and new transaction amount to the blockchain list """
    if (last_transaction == None):
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


# Function for getting transaction amount as input
def get_transaction_amount():
    """ Returns input/transaction amount as float """
    return float(input("Your amount for transaction: "))


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
    is_valid = True
    for block_index in range(len(blockchain)):
        if (block_index == 0):
            continue
        elif (blockchain[block_index][0] == blockchain[block_index - 1]):
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid


waiting_for_input = True

while (waiting_for_input):
    print("Please choose")
    print("1: Add a new transaction")
    print("2: Output blockchain blocks")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()

    if (user_choice == "1"):
        tx_amount = get_transaction_amount()
        add_transaction(tx_amount, get_last_blockchain_value())

    elif (user_choice == "2"):
        print_blockchain_elements()

    elif (user_choice == "q"):
        waiting_for_input = False

    elif (user_choice == "h"):
        if len(blockchain) >= 1:
            blockchain[0] = [2]

    else:
        print("-" * 30)
        print("Wrong input, try again!")
        print("-" * 30)
    if not verify_chain():
        print("Invalid blockchain")
        break
else:
    print("-" * 30)
    print("EXITING...")
    print("-" * 30)
