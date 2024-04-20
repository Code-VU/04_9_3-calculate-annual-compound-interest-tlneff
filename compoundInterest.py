def calculateCompoundInterest():
    # This first 3 lines are provided for you
    client_one_principal = float(input("Principal (amount): "))
    client_one_time = float(input("Time:               "))
    client_one_rate = float(input("Rate:               "))
    client_one_interest = compoundIt(client_one_principal, client_one_rate,
                                     client_one_time) - client_one_principal
    print("Compound Interest:", round(client_one_interest, 2))
    print("---")
    client_two_principal = float(input("Principal (amount): "))
    client_two_time = float(input("Time:               "))
    client_two_rate = float(input("Rate:               "))
    client_two_interest = compoundIt(client_two_principal, client_two_rate,
                                     client_two_time) - client_two_principal
    print("Compound Interest:", round(client_two_interest, 2))
    print("---")
    client_three_principal = float(input("Principal (amount): "))
    client_three_time = float(input("Time:               "))
    client_three_rate = float(input("Rate:               "))
    client_three_interest = compoundIt(client_three_principal, client_three_rate,
                                       client_three_time) - client_three_principal
    print("Compound Interest:", round(client_three_interest, 2))


def compoundIt(principal, rate, time):
    return principal * (1 + rate/100) ** time


# end assignment

# If you want to test locally run > python compoundInterest.py


if __name__ == "__main__":
    calculateCompoundInterest()
