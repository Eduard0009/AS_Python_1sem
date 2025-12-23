def are_parallel(A1, B1, C1, A2, B2, C2):
    return A1 * B2 == A2 * B1



def point_on_line(x, y, A, B, C):
    return A * x + B * y + C == 0


def line_from_points(x1, y1, x2, y2):
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2
    return A, B, C
