
import csv

apartments = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('jurmala.csv', newline='', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='"')

    for row in file_reader:
        apartments.append(row)

# remove header row
apartments.pop(0)

# print(apartments)

while True:
    print("1. Get apartments by sequence number")
    print("2. Top 10 by highest price")
    print("3. Top 10 by lowest price")
    print("4. 20 items, cheaper than price")
    print("5. 20 items, expensive than price")
    print("6. -- Filter of your choice --")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        apartments_seq = int(input("Which apartment would you like to see?"))
        print(apartments[apartments_seq])
        # https://www.w3schools.com/python/python_lists_access.asp
        pass
    elif choice == '2':
        def sorting(apartment):
            return int(apartment[-1])
        apartments.sort(key = sorting , reverse = True)
        print(apartments[0:10])
        

        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        def sorting_2(apartmenter):
            return int(apartmenter[-1])
        apartments.sort(key = sorting_2)
        print(apartments[0:10])
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
            number = 0
            apartments_hah = int(input("Under which price range would you like to search by?"))
            def sorting_range(apartment_bro):
                return int(apartment_bro[-1])
            apartments.sort(key = sorting_range, reverse = True)
            for element in apartments:
                if int(element[-1])<=apartments_hah:
                    if number<=20:
                        print(element)
                        number = number+1
            

        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        
    elif choice == '5':
        numbers = 0
        apartments_funny = int(input("Over which price range would you like to search by?"))
        def sorting_apartment_high(apartment_omg):
            return int(apartment_omg[-1])
        apartments.sort(key = sorting_apartment_high)

        list = []
        for elements in apartments:
            if int(elements[-1])>=apartments_funny:
                list.append(elements)

        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/python_lists_access.asp - Range of Indexes
        for x in list[:20]:
            print(x)

    elif choice == '6':
        # 
        pass
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 7")

    print("===========================")
