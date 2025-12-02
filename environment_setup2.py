# fix 2 
import os
import sys

def patch_long_type():
    # 1. Locate pyfasta directory
    package_dir = None
    for p in sys.path:
        potential_path = os.path.join(p, 'pyfasta')
        if os.path.exists(potential_path) and os.path.isdir(potential_path):
            package_dir = potential_path
            break
            
    if not package_dir:
        print("Error: Could not find pyfasta directory.")
        return

    print(f"Patching 'long' type in: {package_dir}")
    
    # 2. Files known to use 'long'
    files_to_check = ['records.py', 'fasta.py']
    
    for fname in files_to_check:
        fpath = os.path.join(package_dir, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r') as f:
                content = f.read()
            
            # Replace (int, long) with (int) which is valid in Python 3
            # Also replace just 'long' if it stands alone as a type check
            new_content = content.replace("(int, long)", "(int)")
            new_content = new_content.replace("isinstance(key, long)", "isinstance(key, int)")
            
            # General safe replacement for this specific library's usage
            # (We check if content actually changed to avoid unnecessary writes)
            if content != new_content:
                with open(fpath, 'w') as f:
                    f.write(new_content)
                print(f"Fixed 'long' -> 'int' in {fname}")
            else:
                print(f"No usage of 'long' found in {fname}")

patch_long_type()