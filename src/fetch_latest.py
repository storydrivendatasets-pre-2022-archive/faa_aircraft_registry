#!/usr/bin/env python
from datetime import date
from pathlib import Path
import requests
DEST_DIR = Path('data', 'latest_snapshots')
DEST_DIR.mkdir(exist_ok=True, parents=True)

SRC_URL = 'http://registry.faa.gov/database/ReleasableAircraft.zip'

datetag = date.today().isoformat()
dest_path = DEST_DIR.joinpath(f'ReleasableAircraft-{datetag}.zip')

if not dest_path.exists():
    print("Downloading", SRC_URL)
    resp = requests.get(SRC_URL)
    if resp.status_code == 200:
        print(f"Saving {len(resp.content)} bytes to:", dest_path)
        with open(dest_path, 'wb') as w:
            w.write(resp.content)
