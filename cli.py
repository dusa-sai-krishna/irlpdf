import sys
import os

# Add current directory to sys.path so 'irlpdf' can be imported
sys.path.append(os.path.dirname(__file__))

from irlpdf.main import app

if __name__ == "__main__":
    app()
