list1 = ["Shogun","Piatti","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
results = []
def main (list1,list2):
    minIndex = len(list1) + len(list2)
    for item in list1:
        if item in list2 and (list1.index(item) + list2.index(item) <= minIndex):
            if list1.index(item) + list2.index(item) < minIndex:
                minIndex = list1.index(item) + list2.index(item)
                results.clear()
                results.append(item)
            else:
                results.append(item)
    return results
print(main(list1,list2))


