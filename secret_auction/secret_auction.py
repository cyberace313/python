from art import logo
print(logo)

auction = {}
def add_bidders(name, bid):
    auction[name] = bid


print("Welcome to the secret auction program.")

continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")
    add_bidders(name=name, bid=bid)
    print("\n" * 100)

    if other_bidder == "no":
        continue_bidding = False
        highest = 0
        for key in auction:
            if int(auction[key]) > highest:
                current_bidder = key
                highest = int(auction[key])
        print(f"The highest bidder is {current_bidder} with a bid of {highest}")


