"""Check all inline JavaScript blocks and the service worker using Node.js."""
from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
class Scripts(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.blocks = []
        self.current = None
    def handle_starttag(self, tag, attrs):
        if tag == 'script' and not dict(attrs).get('src'):
            self.current = []
    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)
    def handle_endtag(self, tag):
        if tag == 'script' and self.current is not None:
            self.blocks.append(''.join(self.current))
            self.current = None

parser = Scripts()
parser.feed((ROOT / 'windows95.html').read_text(encoding='utf-8'))
assert parser.blocks, 'No script blocks found'
with tempfile.TemporaryDirectory() as temp:
    for i, block in enumerate(parser.blocks):
        path = Path(temp) / f'inline-{i}.js'
        path.write_text(block, encoding='utf-8')
        subprocess.run(['node', '--check', str(path)], check=True)
subprocess.run(['node', '--check', str(ROOT / 'retro95-sw.js')], check=True)
manifest = json.loads((ROOT / 'retro95-manifest.json').read_text())
for file in [manifest['start_url'], *(i['src'] for i in manifest['icons'])]:
    assert (ROOT / file).is_file(), f'Missing asset: {file}'
print(f'Passed: {len(parser.blocks)} inline scripts, service worker, manifest assets.')
