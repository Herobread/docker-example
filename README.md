## Quick Start

1. copy .env.example, rename to .env and put real values(if there are any)

2. install docker/podman for your os

https://podman.io/docs/installation

3. run this command, and it will automatically install and run everything:

```sh
podman compose up
```

---

each folder has Dockerfile that tells what to install and how to run that folder - container

main `compose.yml` tells how to run those containers and how to combine them

## Developing stuff

treach each folder as a container and as a separate instance - no shared libraries or variables, etc

if you need to do something with your container - cd into your folder

try to not change anything outside of your container/folder