# Cluster Setup

SSH RSA Key

Master Pi

Public and private keys

Public key can be shared with anyone - it is placed in the machine the user wants to connect to in the authorized_keys file

Private key is kept secure by the user on their local machien in the .ssh directory.

When a user wishes to connect to the server, the private key generates a signature that can only be authenticated by the server if the public key is present. Thus the login to a machine can be restricted only to the user whose public key is in the authorized_keys list and whose machine contains the private key.

ssh-keygen -t rsa -C "pi@raspberrypi"

You will then be prompted for a file to store your SSH key in:
~/.ssh/id_rsa

(don't bother with a pass-phrase, just press enter)

Now I need to add the public key to the authorized key list on the pi:

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

Second Pi

Eject original pi sd card, use win32 disk image to read and save card as .img file and then write to new sd card for other pi's. Log on and find out ip address.

log into master pi and then ssh into slave pi:

ssh -A pi@192.168.2.3

now we need to remove the public and private keys located on the slave machine. These are the keys copied from the master machine.

cd ~/.ssh
ls -al
rm id_rsa id_rsa.pub
exit # exit ssh

For the master pi to be able to log onto the slaves, we need to add the public key to the authorized_keys file.

cat ~/.ssh/id_rsa.pub | ssh pi@192.168.2.3 "cat >> .ssh/authorized_keys"

update the hostname of slave:

ssh pi@192.168.2.3 'sudo echo "raspberrypi2" | sudo tee /etc/hostname; sudo shutdown -r now'
ssh pi@192.168.2.3 'sudo echo "odroid2" | sudo tee /etc/hostname; sudo shutdown -r now'

Add the ip address of the slave pi to the pifile.

test out mpi:

mpiexec -f pifile -n 8 ~/mpich3/build/examples/cpi

cd ~/mpich3/code
# write test program called hello_rpi.c
mpicc -g -o hello_rpi hello_rpi.c
# need to copy to slave pis
scp hello_rpi pi@192.168.2.3:~/mpich3/code
# now can run program

mpiexec -f pifile -n 8 ~/mpich3/code/hello_rpi

cat ~/.ssh/id_rsa.pub | ssh pi@192.168.2.3 "mkdir .ssh; cat >> .ssh/authorized_keys"

## Next Note

rsync -a sync_mpi.sh pi@130.56.32.189:mpich3

sudo pip uninstall mpi4py && sudo apt-get remove libopenmpi-dev openmpi-bin libhdf5-openmpi-dev

homedir=~
echo PATH="$PATH:$homedir/mpich3/install/bin" >> ~/.profile
source ~/.profile

sudo env MPICC=/home/pi/mpich3/install/bin/mpicc pip install mpi4py

mpiexec -f /home/pi/mpich3/nodes -np 10 python ~/mpich3/code/learn/intro_mpi.py

mpiexec --version

## ssh

# SSH RSA Key

Master Pi

Public and private keys

Public key can be shared with anyone - it is placed in the machine the user wants to connect to in the authorized_keys file. Private key is kept secure by the user on their local machien in the .ssh directory.

When a user wishes to connect to the server, the private key generates a signature that can only be authenticated by the server if the public key is present. Thus the login to a machine can be restricted only to the user whose public key is in the authorized_keys list and whose machine contains the private key.

ssh-keygen -t rsa -C "pi@pisces"

You will then be prompted for a file to store your SSH key in:
~/.ssh/id_rsa

(don't bother with a pass-phrase, just press enter)

Now I need to add the public key to the authorized key list on the pi:

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

Second Pi

Eject original pi sd card, use win32 disk image to read and save card as .img file and then write to new sd card for other pi's. Log on and find out ip address.

log into master pi and then ssh into slave pi:

ssh -A pi@192.168.2.3

now we need to remove the public and private keys located on the slave machine. These are the keys copied from the master machine.

cd ~/.ssh
ls -al
rm id_rsa id_rsa.pub
exit # exit ssh

For the master pi to be able to log onto the slaves, we need to add the public key to the authorized_keys file.

cat ~/.ssh/id_rsa.pub | ssh pi@192.168.2.3 "cat >> .ssh/authorized_keys"

update the hostname of slave:

ssh pi@192.168.2.3 'sudo echo "raspberrypi2" | sudo tee /etc/hostname; sudo shutdown -r now'
ssh pi@192.168.2.3 'sudo echo "odroid2" | sudo tee /etc/hostname; sudo shutdown -r now'

Add the ip address of the slave pi to the pifile.

test out mpi:

mpiexec -f pifile -n 8 ~/mpich3/build/examples/cpi

cd ~/mpich3/code
# write test program called hello_rpi.c
mpicc -g -o hello_rpi hello_rpi.c
# need to copy to slave pis
scp hello_rpi pi@192.168.2.3:~/mpich3/code
# now can run program

mpiexec -f pifile -n 8 ~/mpich3/code/hello_rpi

cat ~/.ssh/id_rsa.pub | ssh pi@192.168.2.17 "mkdir .ssh; cat >> .ssh/authorized_keys"
ssh pi@192.168.2.17 'sudo echo "pi7" | sudo tee /etc/hostname; sudo shutdown -r now'

## Updating Raspberry Pi Mac Address

Issue with Raspeberry Pi’s getting the assigned IP address based on their MAC address, to resolve, do this:

Modify:
/etc/dhcpcd.conf

Change to this:
clientid
#duid
