import math

from experiment1Insert import *

# Experiment function
def experiment(i_values, trials=20):
    """
    Conducts an experiment to measure the number of inversions
    in different types of arrays for varying input sizes.

    Args:
        i_values: A list or iterable of integer values
                 used to calculate the array size (n = 111 * 2^i).
        trials: The number of trials to run for each array type
                and input size.

    Returns:
        A list of dictionaries, where each dictionary contains
        the following keys:
            - 'i': The input value used to calculate the array size.
            - 'n': The array size (n = 111 * 2^i).
            - 'sorted': Average number of inversions in sorted arrays.
            - 'reversed': Average number of inversions in reversed arrays.
            - 'random': Average number of inversions in random arrays.
            - 'nearly_sorted': Average number of inversions in nearly sorted arrays.
    """

    results = []

    for i in i_values:
        n = 111 * (2 ** i)
        sorted_array, reversed_array, random_array, nearly_sorted_array = generate_arrays(n)

        experiment_data = {
            "i": i,
            "n": n,
            "upper_bound": math.comb(n, 2),
            "sorted": 0,
            "reversed": 0,
            "random": 0,
            "nearly_sorted": 0
        }

        for _ in range(trials):
            for array_type, array in zip(
                    ["sorted", "reversed", "random", "nearly_sorted"],
                    [sorted_array, reversed_array, random_array, nearly_sorted_array]
            ):
                experiment_data[array_type] += count_inversions(array)

        for array_type in ["sorted", "reversed", "random", "nearly_sorted"]:
            experiment_data[array_type] /= trials

        results.append(experiment_data)

    return results

# Helper function to count inversions
def count_inversions(arr):
    """
    Counts the number of inversions in a given array.

    An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].

    Args:
        arr: The input array.

    Returns:
        The number of inversions in the array.
    """
    result = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                result += 1
    return result

# Main execution
def main():
    i_values = range(1, 6)  # i = 1 to 5
    results = experiment(i_values)

    # Print results
    print("i\tn\tupper_bound\tSorted\tReversed\tRandom\tNearly Sorted")
    for result in results:
        print(
            f"{result['i']}\t{result['n']}\t{result['upper_bound']}\t{result['sorted']}\t{result['reversed']}\t{result['random']}\t{result['nearly_sorted']}")


if __name__ == "__main__":
    main()