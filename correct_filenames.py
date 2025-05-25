#!/usr/bin/env python3
"""
Fix the “File” field in every labeled_data_*.json so that it exactly matches
the real filenames in the corresponding *_label folders.

Run this from the top-level directory that contains the bag folders.
"""

from __future__ import annotations
import json, os, glob
from pathlib import Path
from typing import Dict, Tuple, List

# ---------- helpers ---------------------------------------------------------

def ts_from_real(fname: str) -> float:
    """timestamp from real file '1731409262_076409304.png' or '.pcd'"""
    stem = Path(fname).stem          # 1731409262_076409304
    sec, usec = stem.split('_')
    return float(sec) + float(f'0.{usec}')

def ts_from_json(fname: str) -> float:
    """timestamp from json entry '1731409262.076409.png'"""
    stem = Path(fname).stem          # 1731409262.076409
    sec, usec = stem.split('.')
    return float(sec) + float(f'0.{usec}')

def closest(real_files: List[Path], target_ts: float) -> str:
    """return basename of real file whose ts is closest to target_ts"""
    return min(real_files, key=lambda f: abs(ts_from_real(f.name) - target_ts)).name

# ---------- main logic ------------------------------------------------------

def process_json(json_path: Path) -> None:
    print(f'• {json_path.relative_to(start)}')

    # 1) find the matching label folder automatically
    bag_root = json_path.parent                    # …/footpath…_json_files
    suffix    = json_path.stem.replace('labeled_data_', '') \
                              .replace('_json', '').replace('_files', '')
    label_dir = bag_root.parent / f'{bag_root.name.replace("_json_files","_label")}' / suffix

    if not label_dir.exists():
        print(f'  ⚠  No label folder found: {label_dir}')
        return

    # 2) collect real files (png or pcd)
    ext = '.pcd' if suffix == 'lidar_points' else '.png'
    real_files = list(label_dir.glob(f'*{ext}'))
    if not real_files:
        print(f'  ⚠  No "*{ext}" files in {label_dir}')
        return

    # 3) load & patch JSON
    with json_path.open() as f:
        data = json.load(f)

    changed = False
    for item in data:
        if 'File' not in item: continue
        tgt_ts   = ts_from_json(item['File'])
        new_name = closest(real_files, tgt_ts)
        if item['File'] != new_name:
            item['File'] = new_name
            changed = True

    # 4) write back if modified
    if changed:
        with json_path.open('w') as f:
            json.dump(data, f, indent=2)
        print('  ✓ filenames updated')
    else:
        print('  – already correct')

# ---------- walk and fix ----------------------------------------------------

start = Path.cwd()
for json_path in start.rglob('labeled_data_*.json'):
    process_json(json_path)

print('\nDone.')

