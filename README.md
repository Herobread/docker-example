## Setup

install docker/podman for your os

https://podman.io/docs/installation

run this, and it will automatically install and run everything:

```sh
podman compose up
```

each folder has Dockerfile that tells what to install and how to run that folder - container

main `compose.yml` tells how to run those containers and how to combine them