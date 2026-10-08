def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        # write if-else here
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

print(find_duplicates([1,2,3,1,3,4,3,2,5]))