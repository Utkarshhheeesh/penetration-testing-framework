import os

def setup_directories():
    if not os.path.exists("output"):
        os.makedirs("output")
