import json
import matplotlib.pyplot as plt
import os

def plot_histograms_from_json(file_paths):
    num_files = len(file_paths)
    cols = 2  # Number of columns in the grid
    rows = (num_files + cols - 1) // cols  # Calculate rows needed for the grid
    fig, axes = plt.subplots(rows, cols, figsize=(12, 5 * rows))
    axes = axes.flatten()  # Flatten axes for easier indexing

    for i, file_path in enumerate(file_paths):
        with open(file_path, "r") as f:
            data = json.load(f)

        # Replace -1 with 0
        values = [0 if v == -1 else v for v in data.values()]

        # Plot histogram
        ax = axes[i]
        ax.hist(values, bins=range(0, 101), edgecolor='black', alpha=0.75)
        ax.set_title(os.path.basename(file_path))
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.set_xlim(0, 99)
        ax.grid(axis='y', linestyle='--', alpha=0.5)

    # Hide any unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

def compare_json_diffs(file_path1, file_path2):
    with open(file_path1, "r") as f1, open(file_path2, "r") as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    diffs = {}
    all_keys = set(data1.keys()).union(data2.keys())

    for key in all_keys:
        value1 = data1.get(key, None)
        value2 = data2.get(key, None)
        if value1 != value2:
            diffs[key] = {"file1": value1, "file2": value2}

    return diffs

def get_accuracy_from_gt(preds_json, gt_json):
    with open(preds_json, "r") as preds_file, open(gt_json, "r") as gt_file:
        preds_data = json.load(preds_file)
        gt_data = json.load(gt_file)

    correct = 0
    total = 0

    for key, gt_value in gt_data.items():
        pred_value = preds_data.get(key, None)
        if pred_value is not None:
            total += 1
            if pred_value == gt_value:
                correct += 1

    accuracy = correct / total if total > 0 else 0
    return round(accuracy,2)


file_paths = [
    r"C:/Users/syeda/OneDrive/Desktop/4th Year/COSC419/jersey-number-pipeline/data/SoccerNet/train/train_gt.json",
    r"C:/Users/syeda/OneDrive/Desktop/4th Year/COSC419/jersey-number-pipeline/data/SoccerNet/test/test_gt.json",
    "recurrent-nn/overfit_test_preds.json",
    "recurrent-nn/evaluation_epoch_2.json",
    "recurrent-nn/evaluation_epoch_4.json",
    "recurrent-nn/evaluation_epoch_8.json",
    "recurrent-nn/evaluation_epoch_16.json"
]

plot_histograms_from_json(file_paths)

# diffs = compare_json_diffs(file_paths[1], file_paths[6])
# for key, diff in diffs.items():
#     print(f"Key: {key}, File1: {diff['file1']}, File2: {diff['file2']}")

print(get_accuracy_from_gt(r"C:/Users/syeda/OneDrive/Desktop/4th Year/COSC419/jersey-number-pipeline/out2/SoccerNetResults/final_results_test_masked_formatted.json", r"C:/Users/syeda/OneDrive/Desktop/4th Year/COSC419/jersey-number-pipeline/data/SoccerNet/test/test_gt.json"))