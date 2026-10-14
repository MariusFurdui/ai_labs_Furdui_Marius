# ex 1
price = {"apples" : 10, "milk" : 12, "bread": 5}
mylist = [("apples", 2), ("milk", 2)]

my_price = sum([price[item]*qty for item, qty in mylist])
print(my_price)


# ex 2

friends = set([("andrew", 10), ("george", 20), ("andrew", 5), ("ann", 10)])
print(friends)
#my_dict = dict(friends)
#print(my_dict.keys())
names = set([nume for nume, suma in friends])
print(names)

# ex 3
n = int(input("Introdu un numar: "))
if n % 2 == 0:
    rezultat = [x for x in range(n + 1)]
else:
    rezultat = [x**2 for x in range(n + 1)]
print(rezultat)

# ex 4
s_in = input("String: ")
num_in = int(input("Numar: "))
dictionar = {i: s_in[i] for i in range(num_in) if i < len(s_in)}

print(dictionar)

# ex 5
def next_letter_string(s):
    return "".join([chr(ord(c) + 1) for c in s])
print(next_letter_string("marius"))

# ex 6
with open("1.txt", "r") as f1, open("2.txt", "a") as f2:
    text = f1.read()
    text_modificat = text.title()
    f2.write("\n" + text_modificat)