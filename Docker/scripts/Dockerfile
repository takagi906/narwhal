# Dictates whether the underlying node should be built as a dev or
# production binary. If empty, then the development mode will be built.
# If passed as BUILD_MODE=--release, then the production will be built.

# 命令：docker build -f Dockerfile ./ --tag narwhal-benchmark:latest
# 命令：docker run --rm -it narwhal-benchmark:latest /bin/bash
FROM ubuntu:22.04

WORKDIR "/narwhal"

COPY docker_benchmark.py /narwhal/

COPY benchmark_client /narwhal/

RUN apt-get update && apt-get install -y python3 python3-pip

RUN mkdir "logs"
