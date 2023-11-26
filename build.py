import sys
import os

os.system("git clone https://github.com/dpkg123/lb-config/ ci --depth=1")
os.system("cd ci && lb config && lb build")
