from SolveLinear3 import solve_linear_3
FIRST_FOUR_POINTS = 4


def is_point_inside_triangle(point, v1, v2, v3):
    """
    this method finds whether a point is inside a triangle. the triangle is
    represented by three point. each point is a tuple of two values. this
    method uses solve_linear_3 method which returns a tuple of 3 coefficients
    if one of these coefficients is negative the point is out of the triangle.
    in any case this method returns a tuple with a boolean value at first place
    and a tuple of coefficients at second place in the tuple.
    :param point: a tuple of two float numbers referred as the point
    :param v1: tuple of two floats represents the first vertex of the triangle
    :param v2: tuple of two floats represents the second vertex of the triangle
    :param v3: tuple of two floats represents the third vertex of the triangle
    :return: a tuple of true if the point is inside the triangle otherwise
    false, and the coefficients tuple
    """
    # calling the function solve_linear_3
    ans_tuple = solve_linear_3([[v1[0], v2[0], v3[0]], [v1[1], v2[1], v3[1]],
                        [1, 1, 1]], [point[0], point[1], 1])
    # run over the tuple returned by solve_linear_3
    for cor in ans_tuple:
        # if one value is negative return the tuple with false and coefficients
        if cor < 0:
            return (False, ans_tuple)
    # if no value is negative return the tuple with true and coefficients
    return (True, ans_tuple)


def create_triangles(list_of_points):
    """
    this method creates a list of triangles out of a given list of points.
    the first two triangles are made out of the fist 4 point, each additional
    point after the firs 4, is checked in which triangle it is located,
    then 3 new triangles are created by the new point, they replace the
    triangle in which the point was found in in the triangle list.
    each triangle in the triangle list is represented by a tuple of 3 tuples
    each inner tuple is a vertex of the triangle which is a tuple of two values
    :param list_of_points: a list of tuples of two values
    :return: a list of tuples containing 3 inner tuples which contain two
    values of coordinates
    """
    # create the first two triangle using the create_two_init_triangles with
    # the first 4 points in the given list
    tri_list = create_two_init_triangles(list_of_points[0:FIRST_FOUR_POINTS])
    # run over the point list from the 5th point and on
    for i in range(FIRST_FOUR_POINTS, len(list_of_points)):
        # run on the existing triangles
        for j in range(0, len(tri_list)):
            # check if the point is inside the current triangle
            if is_point_inside_triangle(list_of_points[i], tri_list[j][0],
                                        tri_list[j][1], tri_list[j][2])[0]:
                # if the point is inside the current triangle, create 3 new
                # triangles using the old triangle vertexes and the new point
                # adding them to the triangle list instead of the triangle the
                # point was in
                tri_list[j:j+1] = create_inner_tri(list_of_points[i],
                                                   tri_list[j][0],
                                                   tri_list[j][1],
                                                   tri_list[j][2])
                break
    return tri_list


def create_two_init_triangles(points):
    """
    this method creates two triangles out of 4 given points,
    this method must get a list of at least 4 tuples otherwise it will not
    work
    :param points: a list of four points
    :return: a list of 2 tuples with 3 inner tuples containing the points
    coordinates
    """
    return [(points[0], points[1], points[2]),
            (points[0], points[2], points[3])]


def create_inner_tri(point, v1, v2, v3):
    """
    this method returns a list of 3 tuples creating 3 different triangles made
    out of 4 points, where the parameter 'point' is a vertex at all new
    triangles. each tuple is made out of 3 tuples of 2 values
    :param point: the joint point of all new triangles
    :param v1: the first old triangle vertex. a tuple of 2 values
    :param v2: the second old triangle vertex. a tuple of 2 values
    :param v3: the third old triangle vertex. a tuple of 2 values
    :return: a list of 3 tuples each represents a new triangle out of the new
    point that was added
    """
    return [(point, v1, v2), (point, v1, v3), (point, v2, v3)]


def do_triangle_lists_match(list_of_points1, list_of_points2):
    """
    this method creates two lists of triangles using the method
    create_triangles with the two given lists. it then checks if the points at
    the same index in both list points are located in the same indexed
    triangles at the triangles lists create by those points lists if all points
    of the same index appear in the same indexed triangles then method returns
    true, otherwise returns false
    :param list_of_points1: the first list of points which are tuples
    of 2 values
    :param list_of_points2: the second list of points which are tuples
    of 2 values
    :return: if all points
    of the same index appear in the same indexed triangles then method returns
    true, otherwise returns false
    """
    # create two lists of triangles using the lists of points
    triangles_list1 = create_triangles(list_of_points1)
    triangles_list2 = create_triangles(list_of_points2)

    # run over the points lists
    for i in range(0, len(list_of_points1)):

        point_i_1 = list_of_points1[i]  # point to compare from list 1
        point_i_2 = list_of_points2[i]  # point to compare from list 2

        # run over the triangles lists
        for j in range(0, len(triangles_list1)):
            # if the current point 1 is inside the current triangle list 1
            # check if the current point 2 is inside the same index triangle
            # list 2
            if is_point_inside_triangle(point_i_1, triangles_list1[j][0],
                                        triangles_list1[j][1],
                                        triangles_list1[j][2])[0]:
                # if point 2 is not in the current triangle return false
                if not is_point_inside_triangle(point_i_2,
                                                triangles_list2[j][0],
                                                triangles_list2[j][1],
                                                triangles_list2[j][2])[0]:
                    return False
    # return true if all indexed points match with indexed triangles
    return True


def get_point_in_segment(p1, p2, alpha):
    """
    this method returns a new point between p1 and p2 such that it is located
    at 'alpha' times the distance between the two points from p1,
    and 1-'alpha' the distance between the two points from p2
    :param p1: a tuple of two values representing the first point
    :param p2: a tuple of two values representing the second point
    :param alpha: a value between 1 and 0 including both
    :return: a tuple of two values representing the new point between p1 and p2
    """
    return ((1-alpha)*p1[0]+alpha*p2[0], (1-alpha)*p1[1]+alpha*p2[1])


def get_intermediate_triangles(source_triangles_list, target_triangles_list,
                               alpha):
    """
    this method creates a list of triangles made out of intermediate vertexes.
    out of two triangles lists, each intermediate triangle of the new list is
    made with the the intermediate vertexes of the source triangles and the
    target triangles intermediate vertexes. this method calls the method
    create_intermediate_triangle which creates the intermediate triangle out of
    the source and target triangle
    :param source_triangles_list: a list of tuples representing the source
    triangles vertexes
    :param target_triangles_list: a list of tuples representing the target
    triangles vertexes
    :param alpha: a value range between 1 and zero including both
    :return: a list of tuples representing the intermediate triangles
    """
    # initiate the intermediate triangles list
    intermediate_tri_list = []
    # run over the lists of source triangles and target triangles
    for i in range(0, len(source_triangles_list)):
        # add to the list the intermediate triangle made with the method
        # create_intermediate_triangle
        intermediate_tri_list.append(create_intermediate_triangle
                                     (source_triangles_list[i],
                                      target_triangles_list[i], alpha))
    return intermediate_tri_list


def create_intermediate_triangle(source_tri, target_tri, alpha):
    """
    this method creates a new triangle made out of the source triangle vertexes
    and the target triangle vertexes this method calls get_point_in_segment
    which returns the intermediate point of the source vertex and target
    the vertex
    :param source_tri: a tuple of 3 tuples representing the source vertexes
    :param target_tri: a tuple of 3 tuples representing the target vertexes
    :param alpha: a value between 1 and 0 including both
    :return: a tuple of 3 tuples which contain the 3 vertexes of the
    intermediate triangle
    """
    return ((get_point_in_segment(source_tri[0], target_tri[0], alpha)),
            (get_point_in_segment(source_tri[1], target_tri[1], alpha)),
            (get_point_in_segment(source_tri[2], target_tri[2], alpha)))


def get_array_of_matching_points(size, triangles_list,
                                 intermediate_triangles_list):
    """
    this method returns a 2D array according to a given size, such that in each
    point(x,y) of the 2D array will be a point that is calculated as so -
    it finds in which intermediate triangle the point(x,y) is, it saves the
    coefficients of it using the method is_point_inside_triangle.
    it then takes the triangle in the same index as the intermediate triangle
    from triangles_list and sends it to alternative_point with the coefficients
    and gets back a new set of coordinates and puts them where the point was
    :param size: a tuple with the size of the image(max_x,max_y)
    :param triangles_list: a list of the source/target triangles
    :param intermediate_triangles_list: a list of the intermediate triangles
    :return: a 2D array of the new coordinates
    """

    # initiate the 2D array
    matching_points_list = [[] for _ in range(size[1])]
    # run over each coordinate in the 2D array by the given size

    for i in range(0, size[1]):
        for j in range(0, size[0]):
            # search for the right intermediate triangle
            for k in range(0,len(intermediate_triangles_list)):
                # the current intermediate triangle
                inter_tri = intermediate_triangles_list[k]
                # the tuple containing if the point is inside and its
                # coefficients
                point_tuple = is_point_inside_triangle((j, i), inter_tri[0],
                                                       inter_tri[1],
                                                       inter_tri[2])
                if point_tuple[0]:
                    # if the current point is inside the current intermediate
                    # triangle append the converted point to the list
                    matching_points_list[i].\
                        append(convert_point(triangles_list[k],point_tuple[1]))
                    break
    return matching_points_list


def convert_point(triangle, coefficients):
    """
    this method takes the "X" values of the vertexes of the given triangle and
    the multiply them by the given coefficients ands them up to be the returned
    x value. it does the same to the "Y" values.
    :param triangle: a tuple of 3 tuples with x and y values of the triangle
    vertexes
    :param coefficients: a tuple containing the 3 values of the coefficients
    found by the method is_point_inside_triangle.
    :return: a tuple containing two values - the new "X" and "Y" values
    """
    return (triangle[0][0]*coefficients[0] + triangle[1][0]*coefficients[1] +
            triangle[2][0]*coefficients[2], triangle[0][1]*coefficients[0] +
            triangle[1][1]*coefficients[1] + triangle[2][1]*coefficients[2])


def create_intermediate_image(alpha, size, source_image, target_image,
                              source_triangles_list, target_triangles_list):
    """
    this method creates an intermediate image.
    it takes the intermediate triangles created by the call to
    get_intermediate_triangles and also gets the 2D array of matching points
    for the source and target triangles, it then creates a 2D array by the
    given size with the new intermediate pixels. it takes each pixel of the
    source and target images by the matching point array that was created
    before. the new pixel is created by the method intermediate_pixel with
    the given alpha value
    :param alpha: a value between 1 and 0 including
    :param size: a tuple of the image size (max_x,max_y)
    :param source_image: the source image
    :param target_image: the target image
    :param source_triangles_list: a list of tuples of 3 of the target
    triangles vertexes which are also tuples of two values - the x and y
    values of the vertexes
    :param target_triangles_list: a list of tuples of 3 of the source image
    triangles vertexes which are also tuples of two values - the x and y
    values of the vertexes
    :return: a 2D array of the intermediate pixels map each place in the 2D
    array contains a tuple of 3 values the RGB values of the pixel
    """
    # create the intermediate triangles list
    intermediate_triangles_list = get_intermediate_triangles\
        (source_triangles_list, target_triangles_list, alpha)
    # create the source image array of matching points
    array_source = get_array_of_matching_points(size, source_triangles_list,
                                                intermediate_triangles_list)
    # create the target image array of matching points
    array_target = get_array_of_matching_points(size, target_triangles_list,
                                                intermediate_triangles_list)
    # initiate the intermediate pixel image by the given size
    intermediate_image = [[]for _ in range(size[1])]
    # run on each place in the new intermediate image by the given size
    for i in range(0, size[1]):
        for j in range(0, size[0]):
            # get the current source and target matching point
            source_match_point = array_source[i][j]
            target_match_point = array_target[i][j]
            # get the source and target RGB values at the current matching
            # point according as a tuple of 3 values (Red,Green,Blue)
            source_RGB = source_image[source_match_point[0],
                                      source_match_point[1]]
            target_RGB = target_image[target_match_point[0],
                                      target_match_point[1]]
            # add to the intermediate image the intermediate pixel create by
            # the method intermediate_pixel (each RGB value is set by this
            # method)
            intermediate_image[i].append(
                (intermediate_pixel(alpha, source_RGB[0], target_RGB[0]),
                 intermediate_pixel(alpha, source_RGB[1], target_RGB[1]),
                 intermediate_pixel(alpha, source_RGB[2], target_RGB[2])))
    return intermediate_image


def intermediate_pixel(alpha, source_RGB, target_RGB):
    """
    this method calculate the intermediates value of a single Red, Green or
    Blue by the given alpha value and the source_RGB and target_RGB value
    :param alpha: a value between 1 and 0 including
    :param source_RGB: a value between 0 and 255 including of the source pixel
    :param target_RGB: a value between 0 and 255 including of the target pixel
    :return: a new value of the pixels Red, Green or Blue part
    """
    return int((1-alpha)*source_RGB+alpha*target_RGB)


def create_sequence_of_images(size, source_image, target_image, 
                source_triangles_list, target_triangles_list, num_frames):
    """
    this method returns a list of intermediate images created by the method
    create_intermediate_image at each iteration the alpha changes according
    to the current place of iteration thus enabling the image to morph from
    the source (alpha being 0 is the source and being 1 is the target image).
    the number of images is decided by the value num_frames which is the list's
    length
    :param size: a tuple of two values representing the image size
    :param source_image: the source image path
    :param target_image: the target image path
    :param source_triangles_list: a list of tuples containing tuples of the
    triangles vertexes of the source image (each inner tuple contains the x
    and y values of one vertex)
    :param target_triangles_list: a list of tuples containing tuples of the
    triangles vertexes of the target image (each inner tuple contains the x
    and y values of one vertex)
    :param num_frames: the number of intermediate image to create
    :return: a list the size of num_frames with a 2D array of pixels
    representing the intermediate images
    """
    # initiate the list of intermediate images
    images_list = []
    # run over the num_frames value to create the intermediate images
    for i in range(0,num_frames):
        # add to the list the current intermediate image create by
        # create_intermediate_image with the current alpha value
        images_list.append(create_intermediate_image(i/(num_frames-1),
                                                     size,source_image,
                                                     target_image,
                                                     source_triangles_list,
                                                     target_triangles_list))
    return images_list