import subprocess
import sys
import os
import signal

def run_script(script_name):
    """
    Starts a Python script as a subprocess.
    """
    return subprocess.Popen([sys.executable, script_name])


def main():
    try:
        print("Starting proctor.py and app.py...\n")

        # Start both scripts
        proctor_process = run_script("proctor.py")
        app_process = run_script("app.py")

        # Wait for both processes to complete
        proctor_process.wait()
        app_process.wait()

    except KeyboardInterrupt:
        print("\nShutting down both processes...")

        # Terminate both processes safely
        proctor_process.terminate()
        app_process.terminate()

        proctor_process.wait()
        app_process.wait()

        print("Processes terminated.")


if __name__ == "__main__":
    main()