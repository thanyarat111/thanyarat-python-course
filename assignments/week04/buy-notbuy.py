prices = []

print("Enter prices of 6 items:")

for i in range(6):
    price = int(input("Item " + str(i + 1) + ": "))
    prices.append(price)

budget = int(input("\nEnter total budget: "))

total = 0
bought_items = []

for i in range(6):
    price = prices[i]

    if total + price <= budget:
        print("\nItem", i + 1, "=", price, "-> buy")
        total += price
        bought_items.append(price)
    else:
        print("\nItem", i + 1, "=", price, "-> cannot buy")

    print("Current total =", total)

print("\nBought items:", bought_items)
print("Total spent:", total)
print("Remaining budget:", budget - total)