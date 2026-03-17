# Batched and Containerized Faster Whisper

Makes [faster-whisper](https://github.com/SYSTRAN/faster-whisper) run in a batched, containerized fashion across multiple files.

## Installation

1. Ensure you have `docker` installed and GPU available.
2. Ensure you have `nvidia-runtime` installed.
3. Build the container with `./build.sh`.

## Execution

Any time you have files to process, execute `./run.sh`. 

This will read the list of files available in the read directory, create the transcript, and once successful move the file to the `processed` folder of choice.

## Leveraging Docker and Docker Compose

### Configuration of network volumes

Docker provides CIFS network access.

```
docker volume create --driver local --opt type=cifs --opt device=//<IP_ADDRESS>/<SHARE_NAME> --opt o=username=<USERNAME>,password=<PASSWORD> <VOLUME_NAME>
```

This allows you to save recordings from your main computer, push it on a network drive, and for this container to run on a schedule.

### Single run through docker-compose
Using `docker compose run` instead of `docker compose up` allows for single runs and termination on completion or error. This clears up the GPU and makes for a much more event-driven package.


