from point import Point
from rectangle import Rectangle


class Circle:
    '''
    圆，由圆心和半径确定
    '''

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def distance_of_point(point1, point2):
    '''
    返回两个点的距离
    '''
    return ((point1.x-point2.x)**2+(point1.y-point2.y)**2)**0.5


def point_in_circle(circle, point):
    '''
    判断点是否在圆中
    '''
    return distance_of_point(point, circle.center) <= circle.radius


def rect_in_circle(circle, rect):
    '''
    判断矩形是否在圆中
    '''
    left_bottom = rect.corner
    right_bottom = Point(rect.corner.x+rect.width, rect.corner.y)
    left_top = Point(rect.corner.x, rect.corner.y+rect.height)
    right_top = Point(rect.corner.x+rect.width, rect.corner.y+rect.height)

    print((left_bottom.x, left_bottom.y), (right_bottom.x, right_bottom.y),
          (left_top.x, left_top.y), (right_top.x, right_top.y))
    return (distance_of_point(left_bottom, circle.center) <= circle.radius and distance_of_point(right_bottom, circle.center) <= circle.radius and distance_of_point(left_top, circle.center) <= circle.radius and distance_of_point(right_top, circle.center) <= circle.radius)


if __name__ == '__main__':
    center = Point(0, 0)
    radius = 2
    c = Circle(center, radius)
    cornet = Point(0, 0)
    r = Rectangle(cornet, 1, 1)
    print(rect_in_circle(c, r))
    print(point_in_circle(c, Point(0, 2)))
