
from pathlib import Path
import shutil

root = Path("/Users/charstiles/Music/samples/cs808")

kicks = [
    "cs_808_c1.wav",
    "cs_808_c1_short.wav",
    "cs_808_c1_short_2.wav",
    "cs_808_c1_long_2.wav",
    "cs_808_c2.wav",
    "cs_808_c2_short.wav",
    "cs_808_c2_short_2.wav",
    "cs_808_c2_long_2.wav",
]

bd = root / "cs808_bd"
hh = root / "cs808_hh"
bd.mkdir(exist_ok=True)
hh.mkdir(exist_ok=True)

for i, filename in enumerate(kicks, 1):
    src = root / filename
    if src.exists():
        dest = bd / f"{i:02d}_{filename.removeprefix('cs_808_')}"
        shutil.copy2(src, dest)

shutil.copy2(
    root / "cs_closed_hat_1.wav",
    hh / "01_closed_hat.wav"
)

