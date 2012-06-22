# a list data structure can be used
in_stock = ['bananas', 'strawberies','apples','bread']
in_stock.sort()

always_in_stock = tuple(in_stock)
#always_in_stock[2]='yam'
#in_stock[2]='yam'
#for smtin in in_stock:
#    print smtin
for item in always_in_stock:
    print item,'Always in Stock'

# if the items do not change then Tupple data structures can be used
# convert list to tupple datastructure
