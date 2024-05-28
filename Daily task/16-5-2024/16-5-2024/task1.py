def main():
    # Take input for the first list and convert to set
    list1 = set(map(int, input("Enter numbers for the first list (separated by spaces): ").split()))

    # Take input for the second list and convert to set
    list2 = set(map(int, input("Enter numbers for the second list (separated by spaces): ").split()))

    # Find intersection, union, and difference
    intersection = list1 & list2
    union = list1 | list2
    difference1 = list1 - list2
    difference2 = list2 - list1
    
    # Print results
    print("Intersection:", intersection)
    print("Union:", union)
    print("Difference (list1 - list2):", difference1)
    print("Difference (list2 - list1):", difference2)

if __name__ == "__main__":
    main()