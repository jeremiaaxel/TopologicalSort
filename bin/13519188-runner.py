import os
from pathlib import Path

main_dir = Path(__file__).resolve().parent.parent
main_name = os.path.join(main_dir, "src", "13519188.py")
test_folder = os.path.join(main_dir, "test")
test_files = [name for name in os.listdir(test_folder) if name.endswith('.txt')] 

for test_file in test_files: 
    os.system(f"python3 {main_name} {test_file}") 

    print()