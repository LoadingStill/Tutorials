import subprocess

folder_path = "Tutorials/Programming/Python 3/"

# Get commit count for the specific folder
cmd = f'git rev-list --count HEAD -- "{folder_path}"'
commit_count = subprocess.check_output(cmd, shell=True).decode().strip()

# Write the commit count to a file
with open('commit_count.txt', 'w') as f:
    f.write(commit_count)
