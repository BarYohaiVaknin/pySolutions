list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
results = []
def main (list1,list2):
    minCounter = len(list1) + len(list2)
    if len(list1) >= len(list2):
        for item in list1:
            if item in list2 and (list1.index(item) + list2.index(item) <= minCounter):
                minCounter = list1.index(item) + list2.index(item)
                results.append(item)
        return results
    else:
        for item in list2:
                if item in list1:
                    minCounter = list1.index(item) + list2.index(item)
                    results.append(item)
        return results
print(main(list1,list2))


