# Author: Jovane Cano
# Github Username: jovanecano
# Date: 05/29/2024
# Description:
"""The following script defines two classes,Point and LineSegment.
    The Point class two points, x and y coordinates. While the LineSegment class represents a line segment defined by the
    points from the Point class"""


class Point:
    """ creating a class to represent a 2-D plot with x and y coordinates"""

    def __init__(self, x_coord, y_coord): #init method that takes two args
        #initializing the private data memebers for x and y coordinates;
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord  # returns the x coordinate

    def get_y_coord(self):
        return self._y_coord  # returnts the y coord

    def distance_to(self, other_point):
        """ this method will calculate the distance between our x/y coordinates minus another point
            Returns the distance between the Point object the method is called on and the Point object passed as the argument."""
        dx = self._x_coord - other_point._x_coord
        dy = self._y_coord - other_point._y_coord
        return (dx ** 2 + dy ** 2) ** 0.5


class LineSegment:
    """this class is used to represent a line segment defined by two endpoints from our previous class's x/y coordinates
    contains two args endpoint_1 and endpoint_2."""

    def __init__(self, endpoint_1, endpoint_2):
        #initializing the LineSegment object with two endpoints
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        #get method, will return the first endpoint of the LineSegment
        return self._endpoint_1

    def get_endpoint_2(self):
        #get method, will return the 2nd endpoint of the LineSegment
        return self._endpoint_2

    def length(self):
        """method will calculate the distance between the two endpoints and returns the value"""
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """calculating the slope of the line seg, if veritcal it returns 'inf' short for infinite """
        x1 = self._endpoint_1.get_x_coord()
        y1 = self._endpoint_1.get_y_coord()
        x2 = self._endpoint_2.get_x_coord()
        y2 = self._endpoint_2.get_y_coord()
        return (y2 - y1) / (x2 - x1) #returns the slope of the line segment

    def is_parallel_to(self, other_line):
        # will check if the line segment is paralleel to another line object and will return true if so and false in not parrallel
        return abs(self.slope() - other_line.slope()) < 1e-7



""" 
used the given usage example from the assingment repo

if __name__ == "__main__":
    point_1 = Point(7, 4)
    point_2 = Point(-6, 18)
    print(point_1.distance_to(point_2))  # Should print the distance between point_1 and point_2

    line_seg_1 = LineSegment(point_1, point_2)
    print(line_seg_1.length())  # Should print the length of line_seg_1
    print(line_seg_1.slope())  # Should print the slope of line_seg_1

    point_3 = Point(-2, 2)
    point_4 = Point(24, 12)
    line_seg_2 = LineSegment(point_3, point_4)
    print(line_seg_1.is_parallel_to(line_seg_2))  # Should print True or False depending on whether the line segments are parallel
"""
