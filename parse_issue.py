import sys
import re
import os

body = sys.stdin.read()

source_lang = re.search(r'source_lang:\s*(.+)', body)
target_lang = re.search(r'target_lang:\s*(.+)', body)

github_env = os.environ.get('GITHUB_ENV')
if github_env:
    with open(github_env, 'a') as env_file:
        print("Ran in GitHub Actions environment, writing to GITHUB_ENV")
        # if source_lang:
        #     print(f'SOURCE_LANG={source_lang.group(1).strip()}')
        env_file.write(f'source_language={source_lang.group(1).strip()}\n')
        if target_lang:
            print(f'target_language={target_lang.group(1).strip()}')
            env_file.write(f'target_language={target_lang.group(1).strip()}\n')