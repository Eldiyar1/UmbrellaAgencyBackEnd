#!/bin/bash

function tcp_dump(){
    local path='/var/log/log136/'
    local logfile="${path}136.log"

    if [ ! -d "$path" ]; then
        mkdir -p "$path"
    fi

    if [ -f "$logfile" ]; then
        rm "$logfile"
    fi

    tcpdump > "$logfile"
}

tcp_dump
