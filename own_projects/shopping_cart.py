# I will be making a shopping cart app which takes 3 inputs the number of items
# the item name and the price of the item and stores them in a list.
# the writing to file is not possible because the data would be inconsistent
# sorted in the order of price, number of items, and name of the item
# while item name is nothing --> ""
def shopping_cart():
    tot = 0
    lst = []
    cnt = 0
    # avarage=0
    item_names_break = False
    while not item_names_break:
        item = input("Enter an item name until "" (nothing) is entered: ")
        if item == "":
            break
        number_of_items = int(input("Enter the number of item(s): "))
        price_of_items = float(input("Enter te price of the item(s): "))
        if price_of_items>0.5:
            print("The price of item cannot be under $0,5, skipping this item")
            lst.append((item, number_of_items, price_of_items * number_of_items))
        tot += total(lst)
        print(f"The subtotal is: ${tot}")
        cnt += 1
    if len(lst) != 0:
        avarage = avg(tot, lst)
        lst = sorting(lst)
        return lst, tot, cnt, avarage
    else:
        return "Can not calculate from a list that has no items."


def total(lst):
    total = 0
    for price in lst:
        total += price[2]
    return total


def avg(total, lst):
    return total / len(lst)


def sorting(lst):
    lst2 = []
    for tup in sorted(lst, key=lambda x: (-x[2], -x[1], x[0])):
        lst2.append(tup)
    return lst2


# def write_to_file(lst,headers):
#     with open("shopping_cart.csv","w") as file:
#         for header in headers:
#             file.write(','.join(header))
#         for item in lst:
#             rows=""

print(shopping_cart())
headers=["Item name","Item count","Price of items","Total number of items","Total payable amount","The number of items (not individually)","Average Payable"]