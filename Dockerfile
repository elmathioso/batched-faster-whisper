FROM nvidia/cuda:12.9.1-cudnn-runtime-ubuntu22.04

RUN apt update && apt install -y python3-pip

RUN python3 -m pip install faster-whisper

ENTRYPOINT ["python3", "/src/run.py", "--input_location","/transcripts/", "--output_location", "/results/"]
