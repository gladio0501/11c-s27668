import math
class SquareGenerator:

    def generate_squares(self,start, end):
        if end < start:
            raise ValueError("End of the range must be greater than the start.")
        return [math.pow(x,2) for x in range(start, end+1)]