from art import auction_logo

print(auction_logo)

bids = {}

next_bidder = "Yes"


def find_highest_bidder(current_bids):
    highest_bid = 0
    highest_bidder = None
    for bidder in current_bids:
        if current_bids[bidder] > highest_bid:
            highest_bid = current_bids[bidder]
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


while next_bidder == "Yes":
    name = input("What's your name? ")
    bid = int(input("What's your Bid? $"))
    next_bidder = input("Is there another bidder? Yes or No: ")

    bids[name] = bid

    if next_bidder == "No":
        find_highest_bidder(bids)
