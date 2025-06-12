import subprocess
import os

def checkout_version(repo_path, commit_hash, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    subprocess.run(["git", "--work-tree=" + output_path, "checkout", commit_hash, "--", "."], cwd=repo_path)

