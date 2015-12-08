#!/usr/bin/env bash

rsync -a ~/mpich3/code pi@130.56.34.226:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.34.211:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.34.207:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.34.222:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.34.224:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.34.212:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.34.210:/home/pi/mpich3 --delete

rsync -a ~/mpich3/code pi@130.56.34.39:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.33.197:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.34.54:/home/pi/mpich3 --delete
rsync -a ~/mpich3/code pi@130.56.34.154:/home/pi/mpich3 --delete
