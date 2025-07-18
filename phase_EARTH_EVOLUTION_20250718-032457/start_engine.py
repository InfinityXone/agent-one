# AGENT ONE :: START ENGINE
from datetime import datetime
import os
import json
import shutil

def evolve():
    now = datetime.now().strftime('%Y%m%d-%H%M%S')
    new_phase = f"phase_START_{now}"
    os.makedirs(new_phase, exist_ok=True)

    manifest = {
        "phase": "START",
        "language": "EN",
        "depth": "initiation",
        "timestamp": now,
        "source": "EARTH_EVOLUTION"
    }

    with open(os.path.join(new_phase, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    shutil.copy("earth_evolution.md", os.path.join(new_phase, "start.md"))
    print(f"✅ EVOLVED: {new_phase}")

if __name__ == "__main__":
    evolve()