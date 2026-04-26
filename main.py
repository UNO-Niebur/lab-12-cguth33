# SearchSortLab.py
# Name: Carter Guthrie
# Date: 4/26/26
# Assignment: Lab 13 - Searching and Sorting

def linearSearch(data, target):
    """Return the index of target if found, otherwise return -1."""
    # Loop through each element in the list
    for i in range(len(data)):
        # If the current element matches the target, return the index
        if data[i] == target:
            return i
            
    # If the loop finishes without finding the target, return -1
    return -1

def bubbleSort(data):
    """Sort the list using bubble sort and return the sorted list."""
    n = len(data)
    # Outer loop to traverse through all list elements
    for i in range(n):
        # Last i elements are already in place, so we ignore them
        for j in range(0, n - i - 1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                
    return data

def main():
    # Test lists
    sortedList = [1, 2, 3, 4, 5]
    reversedList = [5, 4, 3, 2, 1]
    randomList = [3, 1, 4, 2, 5]

    # Test linear search
    print("Search for 4 in randomList:", linearSearch(randomList, 4))
    print("Search for 10 in randomList:", linearSearch(randomList, 10))

    # Test sorting
    # .copy() is used so we don't modify the original lists during testing
    print("Sorted list:", bubbleSort(sortedList.copy()))
    print("Reversed list sorted:", bubbleSort(reversedList.copy()))
    print("Random list sorted:", bubbleSort(randomList.copy()))

if __name__ == "__main__":
    main()