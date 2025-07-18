from datetime import datetime
import os, json, shutil

def evolve():
    now = datetime.now().strftime('%Y%m%d-%H%M%S')
    new_phase = f\"phase_{os.path.basename(r'START')}_{now}\"
    os.makedirs(new_phase, exist_ok=True)

    manifest = {
        \"phase\": \"START\",
        \"language\": \"EN\",
        \"depth\": \"initiation\",
        \"timestamp\": now,
        \"source\": \"START\"
    }
    with open(os.path.join(new_phase, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    src = os.path.join(os.getcwd(), "phase_START_20250717-235134", "start.md")
    dest = os.path.join(new_phase, "start.md")
    if os.path.exists(src):
        shutil.copy(src, dest)
    else:
        with open(dest, "w", encoding="utf-8") as f:
            f.write("# fallback start.md — missing original")

    shutil.copy(__file__, os.path.join(new_phase, os.path.basename(__file__)))
    print(f"✅ EVOLVED: {new_phase}")

if __name__ == "__main__":
    evolve()
