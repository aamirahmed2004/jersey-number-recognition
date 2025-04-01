import json
import pandas as pd

# Load JSON files
with open("final_results.json") as f1, \
     open("final_results_test_sr.json") as f2, \
     open("test_gt.json") as f3:
    original = json.load(f1)
    enhanced = json.load(f2)
    ground_truth = json.load(f3)

# Normalize keys/values to strings
original = {str(k): str(v) for k, v in original.items()}
enhanced = {str(k): str(v) for k, v in enhanced.items()}
ground_truth = {str(k): str(v) for k, v in ground_truth.items()}

# Compare predictions with ground truth
mismatches = []

for key in ground_truth:
    key_str = str(key)
    gt = str(ground_truth[key])
    orig = original.get(key_str, "NA")
    enh = enhanced.get(key_str, "NA")

    if gt != orig or gt != enh:
        mismatches.append({
            "Image Index": key_str,
            "Ground Truth": gt,
            "Original Pipeline": orig,
            "Enhanced (SR 4x)": enh
        })

# Save results to CSV
df = pd.DataFrame(mismatches)
df.to_csv("label_mismatches.csv", index=False)
print(f"✅ Done. Found {len(df)} mismatches. Results saved to 'label_mismatches.csv'.")


import os
import shutil
import pandas as pd

# Load mismatches
df = pd.read_csv("label_mismatches.csv")

# Paths
image_folder = "dataset/test/HR"
output_folder = "mismatched_images"
image_extensions = ['.jpg', '.png', '.jpeg']  # Try multiple

# Create output directory
os.makedirs(output_folder, exist_ok=True)

# Copy matching images
for idx in df["Image Index"]:
    found = False
    for ext in image_extensions:
        filename = f"{idx}{ext}"
        src_path = os.path.join(image_folder, filename)
        if os.path.exists(src_path):
            shutil.copyfile(src_path, os.path.join(output_folder, filename))
            found = True
            break
    if not found:
        print(f"⚠️ Missing image for index {idx} (tried .jpg/.png/.jpeg)")

print(f"✅ Done. Attempted copy for {len(df)} images to '{output_folder}/'")
