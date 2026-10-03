from pathlib import Path
import csv
import re


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TASKS_DIR = PROJECT_ROOT / "data" / "prior_auth_um" / "tasks"
OUTPUT_DIR = PROJECT_ROOT / "analysis" / "data"
OUTPUT_FILE = OUTPUT_DIR / "pa_um_task_metadata.csv"


STAGES = [
    "intake_payer",
    "triage_payer",
    "nurse_review_payer",
    "mdreview_payer",
    "p2p_payer",
]


def extract_stage(task_id):
    for stage in STAGES:
        if stage in task_id:
            return stage
    return ""


def extract_instruction_title(text):
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return ""


def extract_condition(text):
    patterns = [
        r"with ([A-Z][^.;\n]+?)(?:,\s*(?:mild|moderate|severe|unspecified|not specified)|\.)",
        r"with ([A-Z][^.;\n]+?)(?:;|\.)",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            condition = match.group(1).strip()

            # Remove common trailing workflow text.
            condition = re.split(
                r"\b(?:David|MD queue|Case routed|Case escalated|Provider faxed)\b",
                condition,
                maxsplit=1,
            )[0].strip(" ,;:")

            if condition:
                return condition

    return ""


def extract_procedure(title):
    if "—" in title:
        return title.split("—", 1)[1].strip()

    return title


def count_files(directory):
    if not directory.exists():
        return 0

    return sum(
        1
        for path in directory.rglob("*")
        if path.is_file()
    )


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
        "verifier_timeout_sec": (
            verifier_match.group(1)
            if verifier_match
            else ""
        ),
        "agent_timeout_sec": (
            agent_match.group(1)
            if agent_match
            else ""
        ),
    }


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    rows = []

    task_dirs = sorted(
        path
        for path in TASKS_DIR.iterdir()
        if path.is_dir()
    )

    for task_dir in task_dirs:
        task_id = task_dir.name

        instruction_path = task_dir / "instruction.md"
        task_toml_path = task_dir / "task.toml"

        policy_dir = (
            task_dir
            / "fixtures"
            / "judge"
            / "policies"
        )

        request_dir = (
            task_dir
            / "fixtures"
            / "request"
        )

        instruction_text = instruction_path.read_text(
            encoding="utf-8",
            errors="replace",
        )

        title = extract_instruction_title(
            instruction_text
        )

        timeouts = extract_timeouts(
            task_toml_path
        )

        rows.append(
            {
                "task_id": task_id,
                "workflow_stage": extract_stage(task_id),
                "task_title": title,
                "procedure": extract_procedure(title),
                "condition": extract_condition(
                    instruction_text
                ),
                "request_document_count": count_files(
                    request_dir
                ),
                "policy_reference_count": count_files(
                    policy_dir
                ),
                "verifier_timeout_sec": timeouts[
                    "verifier_timeout_sec"
                ],
                "agent_timeout_sec": timeouts[
                    "agent_timeout_sec"
                ],
            }
        )

    fieldnames = [
        "task_id",
        "workflow_stage",
        "task_title",
        "procedure",
        "condition",
        "request_document_count",
        "policy_reference_count",
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

    print(f"PA-UM workflows extracted: {len(rows)}")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
