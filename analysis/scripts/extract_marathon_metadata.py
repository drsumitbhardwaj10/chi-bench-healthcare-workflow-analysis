from pathlib import Path
import csv
import json
from collections import Counter


REPO_ROOT = Path(__file__).resolve().parents[2]
MARATHON_ROOT = REPO_ROOT / "data" / "marathon"
OUTPUT_FILE = REPO_ROOT / "analysis" / "data" / "marathon_task_metadata.csv"


def load_manifest(domain: str) -> dict:
    manifest_file = (
        MARATHON_ROOT
        / domain
        / "fixtures"
        / "session_manifest.json"
    )

    with manifest_file.open("r", encoding="utf-8") as file:
        return json.load(file)


def extract_metadata(domain: str) -> list[dict]:
    manifest = load_manifest(domain)

    rows = []

    for task in manifest["tasks"]:
        rows.append(
            {
                "session_id": manifest["session_id"],
                "domain": manifest["domain"],
                "world_id": manifest["world_id"],
                "task_id": task["task_id"],
                "initial_state": task["initial_state"] or "",
            }
        )

    return rows


def main():
    domains = [
        "prior_auth_provider",
        "prior_auth_um",
        "care_management",
    ]

    all_rows = []

    for domain in domains:
        all_rows.extend(extract_metadata(domain))

    fieldnames = [
        "session_id",
        "domain",
        "world_id",
        "task_id",
        "initial_state",
    ]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    session_counts = Counter(row["session_id"] for row in all_rows)
    domain_counts = Counter(row["domain"] for row in all_rows)
    initial_states = Counter(
        row["initial_state"]
        for row in all_rows
        if row["initial_state"]
    )

    print(f"Marathon task instances extracted: {len(all_rows)}")
    print()
    print("Session counts:")
    for session, count in session_counts.items():
        print(f"  {session}: {count}")

    print()
    print("Domain counts:")
    for domain, count in domain_counts.items():
        print(f"  {domain}: {count}")

    print()
    print("Explicit initial states:")
    for state, count in initial_states.items():
        print(f"  {state}: {count}")

    print()
    print(f"Output: {OUTPUT_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()