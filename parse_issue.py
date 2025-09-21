import sys
import re
import os

body = sys.stdin.read()

source_lang = re.search(r'source_lang:\s*(.+)', body)
target_lang = re.search(r'target_lang:\s*(.+)', body)

github_env = os.environ.get('GITHUB_ENV')
if github_env:
    with open(github_env, 'a') as env_file:
        if source_lang:
            env_file.write(f'SOURCE_LANG={source_lang.group(1).strip()}\n')
        if target_lang:
            env_file.write(f'TARGET_LANG={target_lang.group(1).strip()}\n')

print("SOURCE_LANG=$SOURCE_LANG DEBUG")
print("TARGET_LANG=$TARGET_LANG DEBUG")
