def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    def run(point: List[int]):
        return (sqrt(point[0]**2 + point[1]**2), point)

    sorted_points = list(map(lambda point: point[1], sorted(map(run, points), key= lambda point: point[0])))

    return sorted_points[:k]