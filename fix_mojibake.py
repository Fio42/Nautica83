from pathlib import Path


SUSPICIOUS = ("Ã", "Â", "â", "ðŸ")


def fix_text(text: str) -> str:
    out = text
    for _ in range(3):
        if not any(marker in out for marker in SUSPICIOUS):
            break
        changed = False
        for enc in ("cp1252", "latin1"):
            try:
                candidate = out.encode(enc).decode("utf-8")
            except Exception:
                continue
            if candidate != out:
                out = candidate
                changed = True
                break
        if not changed:
            break
    return out


path = Path("index.html")
lines = path.read_text(encoding="utf-8").splitlines()
fixed_lines = []

for line in lines:
    if "base64," in line or "data-cfemail" in line:
        fixed_lines.append(line)
        continue
    fixed_lines.append(fix_text(line))

path.write_text("\n".join(fixed_lines) + "\n", encoding="utf-8")
