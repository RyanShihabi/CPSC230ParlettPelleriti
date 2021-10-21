def MMM():
    user_list = []
    max = 0
    sum = 0
    val = int(input("Enter a positive integer: "))
    # calculating max value while numbers are entered in
    # getting the sum of entries for mean
    # appending positive values to list

    while val > 0:
        sum += val
        if val > max:
            max = val
        user_list.append(val)
        val = int(input("Enter a positive integer: "))

    # calculating mean with sum and length of array
    mean = sum/len(user_list)

    # median formula: calculating median based on whether array has a center value
    median = user_list[int(len(user_list)/2)] if len(user_list) % 2 != 0 else (user_list[len(user_list)//2-1] + user_list[len(user_list)//2])/2

    # Displaying calculations
    print(f"Mean: {mean}\nMedian: {median}\nMax: {max}")

def main():
    MMM()

if __name__ == "__main__":
    main()
