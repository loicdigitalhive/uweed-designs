"""Rebuild this repository from a fresh download of the uWeed Design System.

Usage: python3 -I .mirror/apply.py <repo> <downloaded project dir> <assets dir>

<downloaded project dir> holds the design system's published files with the
"project/" prefix removed (README.md, tokens.css, components/...).
<assets dir> holds the asset-store files, each named <asset id>.<ext>.

Everything in the repository is replaced except .git, .mirror and the notes
files, which notes.py regenerates. Previews are re-rendered by render.js.
"""
import json
import os
import re
import shutil
import sys

repo, src, assets = sys.argv[1], sys.argv[2], sys.argv[3]
KEEP = {'.git', '.mirror', '.github'}


def unescape(key):
    # The index may store a group or file key with bytes outside
    # [A-Za-z0-9_./-] written as ~ plus two hex digits ("Imagery~20examples").
    # The record's own "name" is the real one; this is only the fallback.
    return re.sub(r'~([0-9A-Fa-f]{2})', lambda m: chr(int(m.group(1), 16)), key)


def safe(path):
    # A group or file name must stay inside assets/<group>/.
    parts = path.replace('\\', '/').split('/')
    if path.startswith('/') or '\\' in path or any(p in ('', '.', '..') for p in parts):
        sys.exit('unsafe asset path in design-system.json: ' + repr(path) + '; nothing changed')
    return path


if not os.path.exists(os.path.join(src, 'design-system.json')):
    sys.exit('design-system.json missing from the download; nothing changed')

# Work out every image's place before touching the repository, so a bad name
# stops the run with the repository unchanged.
ds = json.load(open(os.path.join(src, 'design-system.json'), encoding='utf-8'))
plan = []
for key, spec in ds.get('assetGroups', {}).items():
    group = safe(spec.get('name') or unescape(key))
    for fkey, rec in spec.get('files', {}).items():
        plan.append((group, safe(rec.get('name') or unescape(fkey)), rec.get('blob')))

for name in os.listdir(repo):
    if name in KEEP:
        continue
    path = os.path.join(repo, name)
    shutil.rmtree(path) if os.path.isdir(path) and not os.path.islink(path) else os.remove(path)

count = 0
for root, _, files in os.walk(src):
    for f in files:
        rel = os.path.relpath(os.path.join(root, f), src)
        dest = os.path.join(repo, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(root, f), dest)
        count += 1

have = {f.split('.')[0]: f for f in os.listdir(assets)}
missing = []
for group, name, blob in plan:
    if blob not in have:
        missing.append(group + '/' + name)
        continue
    dest = os.path.join(repo, 'assets', group, name)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(os.path.join(assets, have[blob]), dest)

print(json.dumps({'files': count, 'missing_assets': missing}))
if missing:
    sys.exit(2)
