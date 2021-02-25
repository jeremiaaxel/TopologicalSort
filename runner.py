import os

current_dir = os.getcwd()
main_name = os.path.join(current_dir, "src", "main.py")
test_folder = os.path.join(current_dir, "test")
test_files = [name for name in os.listdir(test_folder) if name.endswith('.txt')] 

for test_file in test_files: 
    os.system(f"python3 {main_name} {test_file}") 

    print()