from experiment1Insert import *
from AVLTree import *

# Experiment function
def experiment(AVLtree, i_values, trials=20):
    results = []

    for i in i_values:
        n = 111 * (2 ** i)
        sorted_array, reversed_array, random_array, nearly_sorted_array = generate_arrays(n)

        experiment_data = {
            "i": i,
            "n": n,
            "sorted": [],
            "reversed": [],
            "random": [],
            "nearly_sorted": []
        }

        # Perform 20 trials for random cases
        for _ in range(trials):
            for array_type, array in zip(
                    ["sorted", "reversed", "random", "nearly_sorted"],
                    [sorted_array, reversed_array, random_array, nearly_sorted_array]
            ):
                tree = AVLTree()
                costs = 0
                for value in array:
                    node, path, promotes = tree.finger_insert(value, value)
                    costs += path

                experiment_data[array_type].append(costs)

        # Take averages for random cases
        for array_type in ["sorted", "reversed", "random", "nearly_sorted"]:
            experiment_data[array_type] = sum(experiment_data[array_type]) / trials

        results.append(experiment_data)

    return results


# Main execution
def main():
    i_values = range(1, 11)  # i = 1 to 10
    results = experiment(AVLTree, i_values)

    # Print or save results
    print("i\tn\tSorted\tReversed\tRandom\tNearly Sorted")
    for result in results:
        print(
            f"{result['i']}\t{result['n']}\t{result['sorted']}\t{result['reversed']}\t{result['random']}\t{result['nearly_sorted']}")


if __name__ == "__main__":
    main()