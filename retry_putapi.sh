#!/bin/bash

while true; do
    output=$(python3 putapi.py)
    # 2>&1)
    exit_code=$?

    if [ $exit_code -eq 0 ]; then
        echo "Success $(date +'%Y-%m-%d %H:%M:%S')" >> /home/user1/230727docker/log.txt
        break
    else
        echo "Failure $(date +'%Y-%m-%d %H:%M:%S') - Error: $output" >> /home/user1/230727docker/log.txt
        sleep 5
    fi
done

