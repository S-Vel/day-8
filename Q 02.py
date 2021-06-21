#program to sort value from decending to asending and convert it into set


lst = ["samvel","senthil","chandru","sathya","selvam"]
lst.sort(reverse=True)
print("sorted list from descending to ascending:\n",lst)
k = set(lst)
print("converting list into set:\n",k)