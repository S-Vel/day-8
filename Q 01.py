#1----------------------------------------------------------------------------------------------------------------------
#program to merge to dictionaries


def Merge(dict1,dict2):
    s = {** dict1,** dict2}
    return s


dict1={"samvel":84,"senthil":56,"chandru":69,"sathya":87,"selvam":90}
dict2 = {"vithan":45,"ranjith":81,"prabha":23,"mani":54}
dict5 = Merge(dict1,dict2)
print(dict5)