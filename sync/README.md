# Syncing Files

We'll be using the program rsync to sync the files on the server. All of the code we run has to be on the same location on each computer on the cluster, which in our case will be: `/home/pi/mpich3/code`. To do this, we will need to copy the code and data to the master computer, and then execute a script to sync the folder on that computer with the others.

The script that syncs the other slave computers can be uploaded to the master computer with this command:

`rsync -a sync_mpi.sh pi@130.56.32.189:mpich3`

## Uploading to the master computer

Once I have my code and data in the `code` directory on my computer, I can sync that to the master computer with this command:

`rsync -a ~/code pi@130.56.32.189:/home/pi/mpich3 --delete`

The nice thing about rysnc is that you can set it to delete and modify all elements in the directory so it mirrors exactly the one you upload.

## Uploading the slave computers

Once you have the `/home/pi/mpich3/code` directory on the server, you can run the script to sync this directory across all the computers in your cluster:

`bash sync_mpi.sh`

## Ready

Once this is complete, you should be ready to start running your MPI programs.
