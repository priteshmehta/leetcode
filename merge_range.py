def merge_range(intervals):
    intervals.sort(key=lambda x: x[0])
    #print(intervals)
    merged = []
    for interval in intervals:
        if not merged:
            merged.append(interval)
        elif interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged


def my_sort():
    pass

print(merge_range([[1, 3], [2, 6], [8, 10], [15, 18]]))