import math
class SquareGenerator:

    def generate_squares(self,start, end):
        return [math.pow(x,2) for x in range(start, end+1)]