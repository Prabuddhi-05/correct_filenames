# 📄 README – Fix JSON File Names to Match Real Data

This script updates the "File" field inside `labeled_data_*.json` files so that each entry exactly matches the actual filenames in the corresponding data folders (e.g., images or point clouds).

---

## 🧾 What It Does

- Reads each `labeled_data_*.json` file.
- Locates the real image or point cloud files from the matching `_label` folder.
- Replaces the `"File"` entry in the JSON with the closest matching real filename (based on timestamp).
- Saves the updated JSON if changes were made.

---

## 🗂️ Folder Structure Example

```
your_dataset/
├── footpath_session_label/
│   ├── fisheye_images_12/
│   ├── output_images/
│   └── lidar_points/
└── footpath_session_json_files/
    ├── labeled_data_fisheye_images_12.json
    ├── labeled_data_output_images.json
    └── labeled_data_lidar_points.json
```

---

## ▶️ How to Use

1. Place this script in the **top-level folder** (the one containing your bag folders).
2. Run the script:

```bash
python3 fix_json_filenames.py
```

That’s it! It will print out what it updates.

---

## ✅ Output

Your `labeled_data_*.json` files will now have `"File"` names that exactly match the real files on disk.
