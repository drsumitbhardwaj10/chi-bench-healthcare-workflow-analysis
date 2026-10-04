from pathlib import Path
import csv
from collections import Counter

import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = REPO_ROOT / "analysis" / "data" / "pa_e2e_task_metadata.csv"
OUTPUT_FILE = REPO_ROOT / "analysis" / "figures" / "pa_e2e_condition_coverage.png"


def main():
    conditions = []

    with INPUT_FILE.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            conditions.append(row["condition"].strip())

    counts = Counter(conditions)

    # Sort by frequency, then alphabetically.
    ranked = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0]),
    )

    labels = [item[0] for item in ranked]
    values = [item[1] for item in ranked]

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.barh(labels[::-1], values[::-1])

    ax.set_title("CHI-Bench Prior Authorization E2E Condition Coverage")
    ax.set_xlabel("Number of workflows")
    ax.set_ylabel("Condition")

    ax.set_xticks(range(0, max(values) + 1))

    for index, value in enumerate(values[::-1]):
        ax.text(value + 0.03, index, str(value), va="center")

    fig.tight_layout()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_FILE, dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"Visualization created: {OUTPUT_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()