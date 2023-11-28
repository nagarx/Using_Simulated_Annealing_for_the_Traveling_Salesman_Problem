import pandas as pd

n = 10

next_city = []

city_node = 0
for i in range (n-1, 0, -1):
    for j in range(i):
        next_city.append(city_node)
    city_node += 1
    
prev_city = []

city_node = 1
for i in range (n-1, 0, -1):
    for j in range(city_node, 10):
        prev_city.append(j)
    city_node += 1
    
distance_arr = [3, 1, 9, 12, 6, 7, 11, 7, 9,
                7, 10, 7, 2, 8, 3, 4, 2, 
                5, 8, 4, 6, 10, 4, 9,
                8, 12, 2, 3, 5, 13, 
                8, 9, 1, 5, 10,
                5, 11, 8, 1,
                4, 5, 3,
                9, 2,
                6]

TSP_data = pd.DataFrame({'current_city': prev_city, 'next_city': next_city, 'distance':distance_arr})