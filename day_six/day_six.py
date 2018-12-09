

example = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

# distance += abs(x_value - x_goal) + abs(y_value - y_goal)
set_of_coordinates = [] # array of original coordinates

# for each coordinate, they can search north south east west
# add a proximity value to each proximal coordinate until
# hitting another of the original set_of_coordinates

coordinates = example.splitlines()

coord_by_identifier = {}

counter = 0
max_x = 0
max_y = 0
min_x = 0
min_y = 0

for coordinate in coordinates:
    x = int(coordinate[0])
    y = int(coordinate[3])

    if counter == 0:
        max_x = x
        max_y = y
        min_x = x
        min_y = y
    else:
        if max_x < x:
            max_x = x
        if min_x > x:
            min_x = x
        if max_y < y:
            max_y = y
        if min_y > y:
            min_y = y

    coord_by_identifier[counter] = (x, y)
    counter += 1

# corner_top_left = (min_x, min_y)
# corner_btm_right = (max_x, max_y)

Matrix = {}
Meta_Matrix = {}

for key, value in coord_by_identifier.items():
    Matrix = {}
    #print (key, value)
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            target_x = value[0]
            target_y = value[1]
            distance = abs(x - target_x) + abs(y - target_y)
            #print (distance)
            Matrix[(x,y)] = distance
    Meta_Matrix[key] = Matrix

outcome_matrix = {}

# A given point in our outcome matrix could be closest to a particlar root
# cooridinate from the input list, or it may be not closer to any one point

for root_point_index, dists_for_coords in Meta_Matrix.items():
    # print ("Root Point Reference: ", root_point_index)
    # print (dists_for_coords)
    for coordinate, dist_val in dists_for_coords.items():
        # print ("")
        # print (coordinate, dist_val)
        # print ("")

        if coordinate in outcome_matrix.keys():
            if dist_val > outcome_matrix[coordinate][1]:
                outcome_matrix[coordinate] = (root_point_index, dist_val)
            elif dist_val == outcome_matrix[coordinate][1]:
                outcome_matrix[coordinate] = (-1, -1)

        else:
            outcome_matrix[coordinate] = (root_point_index, dist_val)

        #if 'key1' in dict.keys():
        # if (key, value) in outcome_matrix.keys():
        #     # print (outcome_matrix[(key, value)])
        # else:
        #     print (k)
        #     print (v)
        #     # outcome_matrix[(k, v)] = value

# print (outcome_matrix)
this = {}
for element in outcome_matrix:
    print (element)
    print (outcome_matrix[element][0])
    if outcome_matrix[element][0] in this.keys():
        this[outcome_matrix[element][0]] += 1
    else:
        this[outcome_matrix[element][0]] = 1
    # print ("")

print (this)
# for p,q in outcome_matrix:
#     print (p, q)


# counter = 0
# for coordinate in coordinates:
    # create an instance of the matrix for each core coordinate
    # go through all the point in the matrix checking the distance from
    # the core coordinate and storing the value in the 2d array index in
    # a dictionary for that coordinate
