input_list = input()
list = input_list.split()
for word in list:
    frequency = list.count(word)
    print(word, frequency)
