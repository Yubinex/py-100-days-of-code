import os
import platform
import art


PLATFORM = platform.system()
if PLATFORM == "Linux":
    def clear(): return os.system('clear')
elif PLATFORM == "Windows":
    def clear(): return os.system('cls')
else:
    print(f"{PLATFORM} is not supported...")
    def clear(): return os.system('cls')
    os.abort


print(art.logo)
auction_dict = {}


def find_highest_bidder(bidding_record):
    highest_bidder = ""
    highest_bid = 0
    for key, value in bidding_record.items():
        if value > highest_bid:
            highest_bid = value
            highest_bidder = key
    print(f"{highest_bidder} won the auction with a bid of ${highest_bid}")


while True:
    name = input("What is your name?: ").lower().strip()
    bid = float(input("What's your bid?: $"))

    auction_dict[name] = bid

    choice = input(
        "Are there any others who want to bid? (yes/no) ").lower().strip()
    if choice == "no":
        break
    clear()
find_highest_bidder(auction_dict)

"""
? First solution
    if choice == "yes":
        clear()
    elif choice == "no":
        highest_bidder = ""
        highest_bid = 0
        for key, value in auction_dict.items():
            if value > highest_bid:
                highest_bidder = key
                highest_bid = value
        print(f"{highest_bidder} won with a bid of ${highest_bid}")
        break
"""
