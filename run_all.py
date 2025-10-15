import os
import sys
from project1 import run_all


def main():
    if len(sys.argv) < 3:
        print("Usage: python run_all.py <input_csv_path> <output_dir>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_dir = sys.argv[2]
    os.makedirs(output_dir, exist_ok=True)

    results = run_all(input_csv, output_dir)
    # Minimal confirmation output
    for key, rows in results.items():
        print(f"{key}: {len(rows)} rows")


if __name__ == "__main__":
    main()


