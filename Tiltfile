# -*- mode: Python -*

docker_compose('./docker-compose.yml')
docker_build(
    'vladimir/auth-service', 
    '../authentication-service', 
    dockerfile="../authentication-service/devDockerfile",
    live_update = [
        sync('../authentication-service/src', '/usr/src/app/src')
    ])
