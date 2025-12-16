def line_from_points(x1, y1, x2, y2):
    if x1 == x2:
        return ('vertical', x1)
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return (k, b)

def are_parallel(line1, line2):
    if line1[0] == 'vertical' and line2[0] == 'vertical':
        return True
    if line1[0] == 'vertical' or line2[0] == 'vertical':
        return False
    return line1[0] == line2[0]

def is_point_on_line(x, y, line):
    if line[0] == 'vertical':
        return x == line[1]
    k, b = line
    return y == k * x + b
