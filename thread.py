import threading
import subprocess

def run_fsb():
  try:
    subprocess.run(["python", "main.py"], cwd="fsb", check=True)
  except subprocess.CalledProcessError as e:
    print(f"An error occurred while running fsb: {e}")

def run_src():
  try:
    subprocess.run(["python", "-m", "main"], cwd="src", check=True)
  except subprocess.CalledProcessError as e:
    print(f"An error occurred while running src: {e}")

# thread1 = threading.Thread(target=run_fsb)
thread2 = threading.Thread(target=run_src)

try:
    # thread1.start()
    thread2.start()

    # thread1.join()
    thread2.join()

    print("Successfully ran both threads!")
except KeyboardInterrupt as e:
   print(f"Thread stopped due to an unexpected error: {e}")
