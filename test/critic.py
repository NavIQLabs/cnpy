#!/usr/bin/env python3
"""
Verify that the generated matrices follow the rules:
- Shape: 100x100
- Data type: float32
- Count: 5 matrices in each format
"""

import numpy as np
import os
import sys


def check_npy_files():
    """Check individual .npy files for correct shape and dtype"""
    print("Checking .npy files...")
    all_ok = True

    for i in range(5):
        filename = f"matrix_{i}.npy"
        if not os.path.exists(filename):
            print(f"  ✗ {filename} not found")
            all_ok = False
            continue

        arr = np.load(filename)

        # Check shape
        if arr.shape != (100, 100):
            print(f"  ✗ {filename}: shape is {arr.shape}, expected (100, 100)")
            all_ok = False
        # Check dtype
        elif arr.dtype != np.float32:
            print(f"  ✗ {filename}: dtype is {arr.dtype}, expected float32")
            all_ok = False
        else:
            print(f"  ✓ {filename}: shape {arr.shape}, dtype {arr.dtype}")

    return all_ok


def check_npz_file():
    """Check .npz file for correct number, shape, and dtype of arrays"""
    print("Checking .npz file...")
    filename = "matrices.npz"

    if not os.path.exists(filename):
        print(f"  ✗ {filename} not found")
        return False

    data = np.load(filename)
    all_ok = True

    # Check number of arrays
    if len(data.files) != 5:
        print(f"  ✗ {filename}: contains {len(data.files)} arrays, expected 5")
        all_ok = False
    else:
        print(f"  ✓ {filename}: contains 5 arrays")

    # Check each array
    for i in range(5):
        varname = f"matrix_{i}"
        if varname not in data.files:
            print(f"  ✗ {varname} not found in {filename}")
            all_ok = False
            continue

        arr = data[varname]

        # Check shape
        if arr.shape != (100, 100):
            print(f"  ✗ {varname}: shape is {arr.shape}, expected (100, 100)")
            all_ok = False
        # Check dtype
        elif arr.dtype != np.float32:
            print(f"  ✗ {varname}: dtype is {arr.dtype}, expected float32")
            all_ok = False
        else:
            print(f"  ✓ {varname}: shape {arr.shape}, dtype {arr.dtype}")

    return all_ok


def main():
    print("=" * 60)
    print("Verifying matrix generation rules")
    print("=" * 60)
    print()

    npy_ok = check_npy_files()
    print()
    npz_ok = check_npz_file()

    print()
    print("=" * 60)
    if npy_ok and npz_ok:
        print("✓ All checks passed!")
        print("=" * 60)
        return 0
    else:
        print("✗ Some checks failed")
        print("=" * 60)
        return 1


if __name__ == "__main__":
    sys.exit(main())
