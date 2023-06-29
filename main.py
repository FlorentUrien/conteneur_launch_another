import docker
import subprocess


def test():
    cmd = 'whoami'
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)
    # cmd = 'sudo chmod 777 /var/run/docker.sock'
    # result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    # output = result.stdout.decode('utf-8')
    # print(output)
    cmd = 'ls -l /var/run/docker.sock'
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    print(output)

    try:
        client = docker.from_env()
        print(client)
    except Exception as e:
        print(e)

    print("Hello")


if __name__ == "__main__":
    test()
