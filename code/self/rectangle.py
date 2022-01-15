class Rectangle:
    '''
    矩形，由左下角的点和宽、高确定
    '''

    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height