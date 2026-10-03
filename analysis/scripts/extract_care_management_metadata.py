from pathlib import Path
import csv
import re

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TASKS_DIR = PROJECT_ROOT / "data" / "care_management" / "tasks"
OUTPUT_DIR = PROJECT_ROOT / "analysis" / "data"
OUTPUT_FILE = OUTPUT_DIR / "care_management_task_metadata.csv"


def extract_instruction_title(text):
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return ""


def parse_task_id(task_id):
    prefix = task_id.removeprefix("cm_")
    match = re.match(r"(.+?)_(hard_refuses|moderate_anxious|low_coop|moderate_tentative|low_tentative|moderate_reluctant)_(\d+)$", prefix)

    if not match:
        return {
            "condition": prefix,
            "engagement_pattern": "",
            "sequence": "",
        }

    return {
        "condition": match.group(1),
        "engagement_pattern": match.group(2),
        "sequence": match.group(3),
    }


def extract_timeouts(task_toml_path):
    text = task_toml_path.read_text(
        encoding="utf-8",
        errors="replace",
    )

    verifier_match = re.search(
        r"\[verifier\].*?timeout_sec\s*=\s*([0-9.]+)",
        text,
        flags=re.DOTALL,
    )

    agent_match = re.search(
        r"\[agent\].*?timeout_sec\s*=\s*([0-9.]+)",
        text,
        flags=re.DOTALL,
    )

    return {
        "verifier_timeout_sec": verifier_match.group(1) if verifier_match else "",
        "agent_timeout_sec": agent_match.group(1) if agent_match else "",
    }


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    rows = []

    task_dirs = sorted(
        path for path in TASKS_DIR.iterdir()
        if path.is_dir()
    )

    for task_dir in task_dirs:
        task_id = task_dir.name

        instruction_path = task_dir / "instruction.md"
        task_toml_path = task_dir / "task.toml"

        instruction_text = instruction_path.read_text(
            encoding="utf-8",
            errors="replace",
        )

        parsed = parse_task_id(task_id)
        timeouts = extract_timeouts(task_toml_path)

        rows.append(
            {
                "task_id": task_id,
                "condition": parsed["condition"],
                "engagement_pattern": parsed["engagement_pattern"],
                "sequence": parsed["sequence"],
                "task_title": extract_instruction_title(instruction_text),
                "verifier_timeout_sec": timeouts["verifier_timeout_sec"],
                "agent_timeout_sec": timeouts["agent_timeout_sec"],
            }
        )

    fieldnames = [
        "task_id",
        "condition",
        "engagement_pattern",
        "sequence",
        "task_title",
        "verifier_timeout_sec",
        "agent_timeout_sec",
    ]

    with OUTPUT_FILE.open(
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames,
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Care Management workflows extracted: {len(rows)}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
