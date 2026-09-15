from pathlib import Path
import argparse
import re
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tasks"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard"],
        default="medium",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "generated_tasks",
    )
    args = parser.parse_args()

    output = args.output
    if not output.is_absolute():
        output = ROOT / output

    if output.resolve() == SOURCE.resolve():
        raise SystemExit("Output directory cannot be the source tasks directory")

    if output.exists():
        shutil.rmtree(output)

    shutil.copytree(
        SOURCE,
        output,
        ignore=shutil.ignore_patterns(
            ".gitkeep",
            "__pycache__",
            "*.pyc",
        ),
    )

    for config in output.rglob("task.toml"):
        text = config.read_text(encoding="utf-8")
        text = re.sub(
            r'difficulty = "[^"]+"',
            f'difficulty = "{args.difficulty}"',
            text,
        )
        config.write_text(text, encoding="utf-8")

    task_count = len(list(output.glob("task_*")))
    print(f"Generated {task_count} tasks in {output}")


if __name__ == "__main__":
    main()
