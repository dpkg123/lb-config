import sys
import os

os.system("apt-get -y install git live-build debian-archive-keyring gpg dosfstools genisoimage squashfs-tools xorriso grub-common grub-pc-bin grub-efi-amd64-bin nano")
os.system("git clone https://github.com/dpkg123/lb-config/ ci")
os.system("cd ci && lb config && lb build")
