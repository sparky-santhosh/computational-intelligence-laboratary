import csv
from collections import Counter
import math
import random
def read_data(filename, sample_size=None):
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.DictReader(file)
            data = list(csv_reader)
        if sample_size and len(data) > sample_size:
            print(f"\nTotal rows in file: {len(data)}")
            data = random.sample(data, sample_size)
            print(f"Randomly selected {sample_size} rows for analysis")
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
def print_sampled_data(data):
    if not data: return
    columns = list(data[0].keys())
    col_widths = {col: max(len(col), max(len(str(row[col])) for row in data)) for col in columns}
    print("\n" + "="*100 + "\nRANDOMLY SELECTED DATA\n" + "="*100)
    header = " | ".join(col.ljust(col_widths[col]) for col in columns)
    print(header + "\n" + "-" * len(header))
    for row in data:
        print(" | ".join(str(row[col]).ljust(col_widths[col]) for col in columns))
    print("="*100 + f"\nTotal rows displayed: {len(data)}\n")
def get_column_values(data, column):
    return [row[column] for row in data]
def get_unique_values(data, column):
    return list(set(get_column_values(data, column)))
def filter_data(data, column, value):
    return [row for row in data if row[column] == value]
def entropy_before_split(data, target_column):
    target_values = get_column_values(data, target_column)
    total_count = len(target_values)
    value_counts = Counter(target_values)
    entropy = 0.0
    calculation_steps = []
    print(f"\nEntropy Before Split (for {target_column}):")
    print(f"Total samples: {total_count}")
    for value, count in value_counts.items():
        prob = count / total_count
        log_val = math.log2(prob) if prob > 0 else 0
        entropy -= prob * log_val
        calculation_steps.append(f"({count}/{total_count} * {log_val:.4f})")
        print(f"  Class '{value}': {count} samples, probability = {count}/{total_count} ({prob:.4f}), log2({prob:.4f}) = {log_val:.4f}")
    calc_str = " + ".join(calculation_steps)
    print(f"Total Entropy Calculation: -[{calc_str}]")
    print(f"Total Entropy = {entropy:.4f}")
    return entropy
def entropy_after_split(data, attribute, target_column):
    total_count = len(data)
    attribute_values = get_unique_values(data, attribute)
    weighted_entropy = 0.0
    weighted_calc_steps = []
    print(f"\nEntropy After Split on '{attribute}':")
    for value in attribute_values:
        subset = filter_data(data, attribute, value)
        sub_count = len(subset)
        weight = sub_count / total_count
        
        print(f"\n  Value '{value}': {sub_count} samples (weight = {sub_count}/{total_count} = {weight:.4f})")
        sub_entropy = entropy_before_split(subset, target_column)
        weighted_entropy += weight * sub_entropy
        weighted_calc_steps.append(f"({sub_count}/{total_count} * {sub_entropy:.4f})")
    weighted_str = " + ".join(weighted_calc_steps)
    print(f"\nWeighted Entropy Calculation for '{attribute}': {weighted_str}")
    print(f"Weighted Entropy for '{attribute}' = {weighted_entropy:.4f}")
    return weighted_entropy
def information_gain(data, attribute, target_column):
    print(f"\n{'='*60}\nCalculating Information Gain for Attribute: '{attribute}'\n{'='*60}")
    ent_parent = entropy_before_split(data, target_column)
    ent_children = entropy_after_split(data, attribute, target_column)
    gain = ent_parent - ent_children
    print(f"\nInformation Gain for '{attribute}' = {ent_parent:.4f} - {ent_children:.4f} = {gain:.4f}")
    print(f"{'='*60}\n")
    return gain
def build_tree(data, target_column, attributes):
    target_values = get_column_values(data, target_column)
    if len(set(target_values)) == 1: return target_values[0]
    if not attributes: return Counter(target_values).most_common(1)[0][0]
    gains = {attr: information_gain(data, attr, target_column) for attr in attributes}
    best_attr = max(gains, key=gains.get)
    tree = {best_attr: {}}
    remaining = [a for a in attributes if a != best_attr]
    for val in get_unique_values(data, best_attr):
        subset = filter_data(data, best_attr, val)
        tree[best_attr][val] = build_tree(subset, target_column, remaining)
    return tree
def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(f" -> {tree}")
        return
    for attr, branches in tree.items():
        print(f"\n{indent}[{attr}]")
        for val, subtree in branches.items():
            print(f"{indent}  |-- {val}", end="")
            print_tree(subtree, indent + "  |   ")
def main():
    filename = input("Enter the input CSV filename: ").strip() or "data.csv"
    sample_input = input("Enter sample data size: ").strip()
    sample_size = int(sample_input) if sample_input.isdigit() else None
    data = read_data(filename, sample_size)
    if not data: return
    print_sampled_data(data)
    target_column = input("Enter target column name: ").strip()
    if target_column not in data[0]: return
    attributes = [col for col in data[0].keys() if col != target_column]
    attributes=attributes[1:]
    print("\n" + "*"*70 + "\nGENERATING ENTIRE DECISION TREE STRUCTURE\n" + "*"*70)
    full_tree = build_tree(data, target_column, attributes)
    print("\n" + "="*70 + "\nFINAL DECISION TREE\n" + "="*70)
    print_tree(full_tree)
    print("\n" + "="*70)
if __name__ == "__main__":
    main()
