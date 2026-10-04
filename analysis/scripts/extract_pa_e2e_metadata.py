from pathlib import Path
import csv
import re


REPO_ROOT = Path(__file__).resolve().parents[2]
TASKS_ROOT = REPO_ROOT / "data" / "prior_auth_e2e" / "tasks"
OUTPUT_FILE = REPO_ROOT / "analysis" / "data" / "pa_e2e_task_metadata.csv"


def extract_condition(instruction_text: str) -> str:
    """Extract the condition from the first Markdown heading."""
    for line in instruction_text.splitlines():
        line = line.strip()

        if not line.startswith("#"):
            continue

        heading = re.sub(r"^#+\s*", "", line).strip()

        if "—" in heading:
            condition = heading.split("—", 1)[1].strip()
            if condition:
                return condition

        if "-" in heading:
            parts = heading.split("-", 1)
            if len(parts) == 2 and parts[1].strip():
                return parts[1].strip()

    return ""


def extract_task_metadata(task_dir: Path) -> dict:
    instruction_file = task_dir / "instruction.md"
    task_file = task_dir / "task.toml"

    instruction_text = instruction_file.read_text(encoding="utf-8")
    task_text = task_file.read_text(encoding="utf-8")

    condition = extract_condition(instruction_text)

    verifier_timeout = ""
    agent_timeout = ""

    verifier_match = re.search(
        r"\[verifier\]\s*timeout_sec\s*=\s*([0-9.]+)",
        task_text,
        re.MULTILINE,
    )

    agent_match = re.search(
        r"\[agent\]\s*timeout_sec\s*=\s*([0-9.]+)",
        task_text,
        re.MULTILINE,
    )

    if verifier_match:
        verifier_timeout = verifier_match.group(1)

    if agent_match:
        agent_timeout = agent_match.group(1)

    return {
        "task_id": task_dir.name,
        "condition": condition,
        "task_kind": "provider_to_payer_e2e",
        "task_actor": "provider_and_payer",
        "verifier_timeout_sec": verifier_timeout,
        "agent_timeout_sec": agent_timeout,
        "provider_mcp": True,
        "payer_mcp": True,
    }


def main():
    task_dirs = sorted(
        path
        for path in TASKS_ROOT.iterdir()
        if path.is_dir() and path.name.endswith("_e2e")
    )

    rows = [extract_task_metadata(task_dir) for task_dir in task_dirs]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "task_id",
        "condition",
        "task_kind",
        "task_actor",
        "verifier_timeout_sec",
        "agent_timeout_sec",
        "provider_mcp",
        "payer_mcp",
    ]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"E2E workflows extracted: {len(rows)}")
    print(f"Output: {OUTPUT_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()