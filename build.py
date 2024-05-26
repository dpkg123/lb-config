import subprocess

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip().decode())
    return process.poll()

def main():
    run_command('git clone https://github.com/dpkg123/lb-config/ ci --depth=1')
    run_command('cd ci && lb config && lb build')

if __name__ == '__main__':
    main()
