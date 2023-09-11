def cross_product(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

# 示例
vector1 = (3, 4)
vector2 = (1, 2)
result = cross_product(vector1, vector2)
print("向量叉乘结果:", result)


#判断相交
def segments_intersect(segment1, segment2):
    p1, q1 = segment1
    p2, q2 = segment2

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # 共线
        return 1 if val > 0 else 2  # 顺时针或逆时针

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True  # 交叉

    if o1 == 0 and on_segment(p1, p2, q1):
        return True  # p2 在 p1q1 上
    if o2 == 0 and on_segment(p1, q2, q1):
        return True  # q2 在 p1q1 上
    if o3 == 0 and on_segment(p2, p1, q2):
        return True  # p1 在 p2q2 上
    if o4 == 0 and on_segment(p2, q1, q2):
        return True  # q1 在 p2q2 上

    return False

def on_segment(p, q, r):
    return min(p[0], q[0]) <= r[0] <= max(p[0], q[0]) and min(p[1], q[1]) <= r[1] <= max(p[1], q[1])

# 示例
segment1 = ((1, 1), (10, 1))
segment2 = ((1, 2), (10, 2))
result = segments_intersect(segment1, segment2)
print("线段相交结果:", result)


#求解凸包
def graham_scan(points):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # 共线
        return 1 if val > 0 else 2  # 顺时针或逆时针

    def find_p0(points):
        min_y = float('inf')
        min_idx = -1
        for i, (x, y) in enumerate(points):
            if y < min_y or (y == min_y and x < points[min_idx][0]):
                min_y = y
                min_idx = i
        return min_idx

    def compare(p1, p2):
        o = orientation(p0, p1, p2)
        if o == 0:
            return -1 if dist_sq(p0, p2) >= dist_sq(p0, p1) else 1
        return -1 if o == 2 else 1

    def dist_sq(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    if len(points) < 3:
        return []

    p0_idx = find_p0(points)
    p0 = points[p0_idx]
    sorted_points = sorted(points, key=lambda x: (atan2(x[1] - p0[1], x[0] - p0[0]), x))
    sorted_points = sorted_points[1:]  # 移除p0

    hull = [p0, sorted_points[0]]
    for i in range(1, len(sorted_points)):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])

    return hull

from math import atan2

# 示例
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 3), (3, 0)]
convex_hull = graham_scan(points)
print("凸包点集:", convex_hull)
