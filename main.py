def create_dict():
    dictionary = dict()
    with open('movies.txt', 'r') as file:
        gen = (i.rstrip('\n').split(", ") for i in file)

        for i in gen:
            dictionary[i[0]] = set(i[1:])
    
    return dictionary

def find_actors(movie1, movie2):
    dictionary = create_dict()
    set1 = set()
    set2 = set()
    for i in dictionary:
        if movie1 in dictionary[i]:
            set1.add(i)
        if movie2 in dictionary[i]:
            set2.add(i)
    
    return set1, set2

def find_all_actors(movie1, movie2):
    set1, set2 = find_actors(movie1, movie2)

    return set1.union(set2)

def find_common_actors(movie1, movie2):
    set1, set2 = find_actors(movie1, movie2)

    return set1.intersection(set2)

def find_symmetric_diff(movie1, movie2):
    set1, set2 = find_actors(movie1, movie2)

    return set1.symmetric_difference(set2)

def find_co_actors(actor):
    dictionary = create_dict()
    co_set = set()
    for movie in dictionary[actor]:
        for i in dictionary:
            if movie in dictionary[i] and i != actor:
                co_set.add(i)
    
    return co_set
    
while True:
    print('\n1. Find actors based on movie')
    print('2. Find co-actors')
    print('q. For quit')
    choise = input('Make your choise [1/2]: ')

    if choise == '1':
        movie1 = input("Name of first movie: ")
        movie2 = input("Name of second movie: ")
        print("\nAll actors:")
        print(', '.join(find_all_actors(movie1, movie2)))
        print("\nCommon actors:")
        print(', '.join(find_common_actors(movie1, movie2)))
        print("\nSymmetric actors:")
        print(', '.join(find_symmetric_diff(movie1, movie2)))
    elif choise == '2':
        name = input('Actor name: ')
        print('\n' + ', '.join(find_co_actors(name)))
    elif choise == 'q':
        exit()
    else:
        print("Wrong choise!")
        continue

