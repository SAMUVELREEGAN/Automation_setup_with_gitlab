import os
import subprocess
import sys

def build_react():
    # Correct frontend folder for your setup
    frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))
    build_path = os.path.join(frontend_path, 'build')

    # Build only if index.html missing
    if not os.path.exists(os.path.join(build_path, 'index.html')):
        print("⚙️ Building React app...")
        subprocess.run(["npm", "install"], cwd=frontend_path, shell=True)
        result = subprocess.run(["npm", "run", "build"], cwd=frontend_path, shell=True)
        if result.returncode != 0:
            print("❌ React build failed")
            sys.exit(1)
        print("✅ React build completed!")
    else:
        print("✅ React build already exists.")

if __name__ == "__main__":
    build_react()
