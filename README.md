# Fix JSON file names to match real data

This script updates the "File" field inside `labeled_data_*.json` files so that each entry exactly matches the actual filenames in the corresponding data folders (e.g., images or point clouds).

---

## What it does

- Reads each `labeled_data_*.json` file.
- Locates the real image or point cloud files from the matching `_label` folder.
- Replaces the `"File"` entry in the JSON with the closest matching real filename (based on timestamp).
- Saves the updated JSON if changes were made.

---

## Folder structure example

```
your_dataset/
├── bag1_label/
│   ├── fisheye_images_12/
    ├── fisheye_images_13/
    ├── fisheye_images_14/
│   ├── output_images/
│   └── lidar_points/
└── bag1_json_files/
    ├── labeled_data_fisheye_images_12.json
    ├── labeled_data_fisheye_images_13.json
    ├── labeled_data_fisheye_images_14.json
    ├── labeled_data_output_images.json
    └── labeled_data_lidar_points.json
├── correct_filenames.py
```

---

## How to use

1. Place this script in the **current folder** (the one containing your bag folders).
2. Run the script:

```bash
python3 correct_filenames.py
```
---

## Output

Your `labeled_data_*.json` files will now have `"File"` names that exactly match the real files on disk.
