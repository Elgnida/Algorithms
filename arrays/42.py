def pitcraft(array: list[int]):
    max_height = 0
    water_count = 0
    now_m = 0
    for i in range(len(array)):
        if array[i] > array[max_height]:
            max_height = i

    for i in range(max_height):
        if array[i] > now_m:
            now_m = array[i]
        water_count += now_m - array[i]
    now_m = 0
    for i in range(len(array) - 1, max_height, -1):
        if array[i] > now_m:
            now_m = array[i]
        water_count += now_m - array[i]
    return water_count

print(pitcraft([4,2,0,3,2,5]))

