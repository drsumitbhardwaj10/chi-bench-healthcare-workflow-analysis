from pathlib import Path
import csv
from collections import Counter

import matplotlib.pyplot as plt


REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = REPO_ROOT / "analysis" / "data" / "marathon_task_metadata.csv"
OUTPUT_FILE = REPO_ROOT / "analysis" / "figures" / "marathon_session_coverage.png"


def load_data():
    with DATA_FILE.open("r", encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def main():
    rows = load_data()

    session_counts = Counter(row["domain"] for row in rows)

    labels = [
        "Prior Authorization\nProvider",
        "Prior Authorization\nUM",
        "Care Management",
    ]

    domains = [
        "prior_auth_provider",
        "prior_auth_um",
        "care_management",
    ]

    values = [session_counts[domain] for domain in domains]

    fig, ax = plt.subplots(figsize=(9, 5))

    bars = ax.bar(labels, values)

    ax.set_title("CHI-Bench Marathon Session Coverage")
    ax.set_ylabel("Underlying task instances")
    ax.set_ylim(0, 28)

    for bar, value in zip(bars, values):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.5,
            str(value),
            ha="center",
            va="bottom",
        )

    ax.text(
        0.5,
        -0.22,
        "Three long-horizon sessions; 25 underlying workflows per session",
        transform=ax.transAxes,
        ha="center",
    )

    fig.tight_layout()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_FILE, dpi=200, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved: {OUTPUT_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()