# Complete the hourglassSum function below.
def hourglassSum(arr):
    """
    Takes in an array and returns the highest computed
    value from the hour glass
    """
    highest_val = None

    # Just define how the hour glass looks like,
    # arithmetically and loop through the 2d array (i.e. i and j)
    # while keeping in mind the edges
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            total = top + mid + bottom

            if highest_val is None:
                highest_val = total
                continue

            if total > highest_val:
                highest_val = total

    return highest_val
