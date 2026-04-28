import csv
import math
import random
def get_distance(p1, p2, metric='euclidean'):
    if metric == 'manhattan':
        return sum(abs(a - b) for a, b in zip(p1, p2))
    return math.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))
def load_data(filename):
    dataset = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter='\t')
            next(reader)
            for row in reader:
                if not row or len(row) < 5: continue
                dataset.append([float(x) for x in row])
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None, None, None

    X_only = [r[:4] for r in dataset]
    mins = [min(col) for col in zip(*X_only)]
    maxs = [max(col) for col in zip(*X_only)]
    return dataset, mins, maxs
all_rows, mins, maxs = load_data('transfusion_data.csv')
if all_rows:
    print("--- Enter Unknown Data to Predict ---")
    u_r = float(input("Recency (months): "))
    u_f = float(input("Frequency (times): "))
    u_m = float(input("Monetary (c.c.): "))
    u_t = float(input("Time (months): "))
    u_raw = [u_r, u_f, u_m, u_t]
    k_val = int(input("\nEnter K value (e.g. 5): "))
    metric_choice = input("Enter Metric (euclidean / manhattan): ").strip().lower()

    # Normalize user input using
    u_norm = [(u_raw[i] - mins[i]) / (maxs[i] - mins[i]) for i in range(4)]

    # B. Choose 150 Random Data Points from the 750
    sample_150 = random.sample(all_rows, 150)
    
    print(f"\n--- Printing 150 Randomly Selected Records ---")
    print(f"{'No.':<5} | {'Raw Data (R, F, M, T)':<40} | {'Class'}")
    print("-" * 65)
    for idx, row in enumerate(sample_150):
        fmt_row = [f"{val:.2f}" for val in row[:4]]
        # Accessing the 5th column (index 4) for the class label
        label = int(row[4]) 
        print(f"{idx+1:<5} | {str(fmt_row):<40} | {label}")

    # C. Calculate Distances & Rank
    ranked_list = []
    for row in sample_150:
        row_norm = [(row[i] - mins[i]) / (maxs[i] - mins[i]) for i in range(4)]
        dist = get_distance(u_norm, row_norm, metric_choice)
        ranked_list.append({'dist': dist, 'raw': row[:4], 'label': int(row[4])})

    # Sort all 150 by distance to find the nearest ones
    ranked_list.sort(key=lambda x: x['dist'])

    # D. Top K Nearest Neighbors (from the sorted 150)
    print(f"\n--- Top {k_val} Nearest Neighbors (Ranked) ---")
    print(f"{'Rank':<5} | {'Dist':<10} | {'Raw Data (R, F, M, T)':<40} | {'Class'}")
    print("-" * 75)
    
    k_neighbors = ranked_list[:k_val]
    labels_in_k = [n['label'] for n in k_neighbors]
    
    for i, item in enumerate(k_neighbors):
        fmt_k_raw = [f"{val:.2f}" for val in item['raw']]
        print(f"{i+1:<5} | {item['dist']:<10.4f} | {str(fmt_k_raw):<40} | {item['label']}")

    # E. VOTING CALCULATION
    count_0 = labels_in_k.count(0)
    count_1 = labels_in_k.count(1)

    print("\n" + "="*50)
    print(f"VOTING CALCULATION FOR K={k_val}")
    print(f"Total Class 0 Neighbors: {count_0}")
    print(f"Total Class 1 Neighbors: {count_1}")
    print("-" * 50)

    # Weighted Calculation logic
    w_scores = {0: 0.0, 1: 0.0}
    for n in k_neighbors:
        dist_w = 1 / (n['dist'] + 1e-5)
        w_scores[n['label']] += dist_w

    print(f"Weighted Score Class 0: {w_scores[0]:.4f}")
    print(f"Weighted Score Class 1: {w_scores[1]:.4f}")
    print("-" * 50)
    
    # Final Predictions
    pred_unweighted = max(set(labels_in_k), key=labels_in_k.count)
    pred_weighted = 0 if w_scores[0] > w_scores[1] else 1

    print(f"FINAL PREDICTION (UNWEIGHTED): Class {pred_unweighted}")
    print(f"FINAL PREDICTION (WEIGHTED):   Class {pred_weighted}")
    print("="*50)

