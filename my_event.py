class Event:
    def __init__(self, time, ball_a, ball_b, paddle):
        self.time = time
        self.a = ball_a
        self.b = ball_b
        self.paddle = paddle

        if ball_a is not None:
            self.count_a = ball_a.count
        else:
            self.count_a = -1
        if ball_b is not None:
            self.count_b = ball_b.count
        else:
            self.count_b = -1

    def __lt__(self, that):
        return self.time < that.time

    def is_valid(self):
        if (self.a is not None) and (self.a.count != self.count_a):
            return False
        if (self.b is not None) and (self.b.count != self.count_b):
            return False
        return True