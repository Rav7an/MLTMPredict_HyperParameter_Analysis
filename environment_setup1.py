# fix 1
import os
import sys

def patch_cstringio():
    # 1. Locate pyfasta
    package_dir = None
    for p in sys.path:
        potential_path = os.path.join(p, 'pyfasta')
        if os.path.exists(potential_path) and os.path.isdir(potential_path):
            package_dir = potential_path
            break
            
    if not package_dir:
        print("Error: Could not find pyfasta directory.")
        return

    print(f"Patching cStringIO in: {package_dir}")
    
    # 2. Define the replacement
    # In Python 3, cStringIO is gone. We use 'io' module instead.
    # We alias it as cStringIO so the rest of the code doesn't break.
    replacements = {
        "import cStringIO": "import io as cStringIO", 
        "from cStringIO import StringIO": "from io import StringIO"
    }
    
    # 3. Apply to all files
    files_to_check = ['records.py', 'fasta.py', 'split_fasta.py', '__init__.py']
    
    for fname in files_to_check:
        fpath = os.path.join(package_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r') as f:
                content = f.read()
            
            new_content = content
            changed = False
            for old, new in replacements.items():
                if old in new_content:
                    new_content = new_content.replace(old, new)
                    changed = True
            
            if changed:
                with open(fpath, 'w') as f:
                    f.write(new_content)
                print(f"Patched cStringIO in {fname}")
            else:
                print(f"No cStringIO found in {fname}")

patch_cstringio()