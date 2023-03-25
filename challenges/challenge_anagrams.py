def alphabetically_merge_sort(str):
    if len(str) <= 1:
        return str

    mid = len(str) // 2
    left = str[:mid]
    right = str[mid:]

    left = alphabetically_merge_sort(left)
    right = alphabetically_merge_sort(right)

    return alphabetically_merge(left, right)


def alphabetically_merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ("", "", False)

    sorted_str1 = ''.join(alphabetically_merge_sort(first_string.lower()))
    sorted_str2 = ''.join(alphabetically_merge_sort(second_string.lower()))

    return (
        sorted_str1,
        sorted_str2,
        sorted_str1 == sorted_str2
    )
