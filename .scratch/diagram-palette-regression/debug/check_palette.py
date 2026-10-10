"""Differential check of previously assigned category paints; no private fixtures."""
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {'s': 'http://www.w3.org/2000/svg'}
def paint(root, el):
    css = '\n'.join(e.text or '' for e in root.findall('.//s:style', NS))
    result = {k: el.get(k) for k in ('fill', 'stroke') if el.get(k)}
    for selector, body in re.findall(r'([^{}]+)\{([^{}]+)\}', css):
        if any(s.strip().startswith('.') and s.strip()[1:] in el.get('class','').split() for s in selector.split(',')):
            result.update(dict((k.strip(),v.strip()) for k,v in re.findall(r'([\w-]+)\s*:\s*([^;]+)',body)))
    result.update(dict((k.strip(),v.strip()) for k,v in re.findall(r'([\w-]+)\s*:\s*([^;]+)', el.get('style',''))))
    return tuple(result.get(k) for k in ('fill','stroke'))

def check(before, after, node=None):
    old, new = ET.parse(before).getroot(), ET.parse(after).getroot()
    actual = {e.get('id'):e for e in new.iter() if e.get('id')}
    checked=0; failures=[]
    for el in old.iter():
        if not re.search(r'\bcategory-[1-5]\b', el.get('class','')) or (node and el.get('id')!=node): continue
        checked+=1; peer=actual.get(el.get('id')); expected=paint(old, el)
        found=paint(new, peer) if peer is not None else ('MISSING','MISSING')
        if expected!=found: failures.append((el.get('id'),expected,found))
    return checked, failures

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--workspace',type=Path,required=True); ap.add_argument('--node'); ap.add_argument('--figure'); a=ap.parse_args()
    total=0; errors=0
    for path in json.loads((a.workspace/'files.json').read_text()):
        p=Path(path)
        if a.figure and p.stem!=a.figure: continue
        n,bad=check(a.workspace/'original'/p.name,p,a.node); total+=n; errors+=len(bad)
        print(f'{"FAIL" if bad else "PASS"} {p.stem}: {len(bad)}/{n} assigned category paints changed')
        if a.node:
            for node,expected,actual in bad: print(f'  {node}: expected fill/stroke={expected}; actual={actual}')
    print(f'{"FAIL" if errors or not total else "PASS"}: {errors}/{total} assigned category paints changed')
    return int(bool(errors) or not total)
if __name__=='__main__': sys.exit(main())
