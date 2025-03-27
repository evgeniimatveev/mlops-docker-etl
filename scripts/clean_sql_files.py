from pathlib import Path
import re

sql_dir = Path("sql/dql")

for file in sql_dir.glob("*.sql"):
    content = file.read_text()

    # ✅ Remove trailing spaces from each line
    lines = [line.rstrip() for line in content.splitlines()]

    # ✅ Force SELECT targets to be on a new line (if they are on the same line)
    if re.search(r"SELECT\s+\w+", lines[0], re.IGNORECASE):
        lines = re.sub(r"(?i)SELECT\s+", "SELECT\n    ", "\n".join(lines)).splitlines()

    # ✅ Add a single trailing newline at the end of the file
    cleaned = "\n".join(lines).rstrip() + "\n"

    file.write_text(cleaned)
    print(f"✅ Cleaned: {file.name}")