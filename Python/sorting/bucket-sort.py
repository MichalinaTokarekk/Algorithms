def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    bucket_count = 10
    min_value = min(arr)
    max_value = max(arr)
    bucket_range = (max_value - min_value) / bucket_count

    buckets = [[] for _ in range(bucket_count)]
    for i in range(len(arr)):
        diff = (arr[i] - min_value) / bucket_range - int((arr[i] - min_value) / bucket_range)
        if diff == 0 and arr[i] != min_value:
            buckets[int((arr[i] - min_value) / bucket_range) - 1].append(arr[i])
        else:
            buckets[int((arr[i] - min_value) / bucket_range)].append(arr[i])

    for i in range(bucket_count):
        buckets[i] = insertion_sort(buckets[i])

    sorted_arr = []
    for i in range(bucket_count):
        sorted_arr.extend(buckets[i])

    return sorted_arr

# Przykład użycia
arr = [0.89, 0.56, 0.78, 0.34, 0.12, 0.22, 0.11]
sorted_arr = bucket_sort(arr)
print("Bucket Sort:", sorted_arr)
