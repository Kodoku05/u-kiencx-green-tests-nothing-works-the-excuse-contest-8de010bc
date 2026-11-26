from pathlib import Path

output = Path("/output")
output.mkdir(exist_ok=True)
(output / "entry.txt").write_text(
    "All tests pass: I made the apology page the homepage, so customers can skip straight to the part we actually support.",
    encoding="utf-8",
)
