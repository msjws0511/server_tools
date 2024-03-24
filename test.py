import docker

def get_containers():
    client = docker.from_env()
    containers = client.containers.list()
    return containers

get_containers()