import os
import sys
#### dont forget to replace Vagrantfile with Vagrantfile


## Droplet number 1-4
Add = "ADD1"


Vagrant_file_add = """
    config.vm.define 'NAME2' do |config|
        config.vm.provider :digital_ocean do |provider, override|
          override.ssh.private_key_path = '~/.ssh/id_rsa'
          override.vm.box = 'digital_ocean'
          override.vm.box_url = 'https://github.com/devopsgroup-io/vagrant-digitalocean/raw/master/box/digital_ocean.box'
          override.nfs.functional = false
          override.vm.allowed_synced_folder_types = :rsync
          provider.token = 'TOKEN'
          provider.image = 'IMAGE'
          provider.region = 'REGION'
          provider.size = 'SIZE'
          provider.backups_enabled = false
          provider.private_networking = false
          provider.ipv6 = false
          provider.monitoring = false
        end
    end"""
striped = Vagrant_file_add.replace('"',"")


droplet_number = int(input("How many Droplets do you want?[1, 2, 3 or 4]: "))
if droplet_number == 1:
    with open("Vagrantfile") as f:
        addNEWdroplet=f.read().replace(Add , striped)


    with open("Vagrantfile", "w") as f:
        f.write(addNEWdroplet.replace('"', ""))


## Droplet1 name change

with open("Vagrantfile") as f:
    droplet_1_Change=f.read().replace("NAME2", "droplet2")

with open("Vagrantfile", "w") as f:
    f.write(droplet_1_Change)

## TOKEN

digital_ocean_TOKEN = input("Paste token here: ")

with open("Vagrantfile") as f:
    newToken=f.read().replace("TOKEN", "{}".format(digital_ocean_TOKEN))

with open("Vagrantfile", "w") as f:
    f.write(newToken)

## Choosing Image

cmd_run_vagrant_list_IMAGES = str("vagrant digitalocean-list images {}".format(digital_ocean_TOKEN))
os.system(cmd_run_vagrant_list_IMAGES)
print("\nPlease choose from the above Images to use for your vagrant machines\n")

print("Ex. ubuntu-18-04-x64, centos-8-x64")
digital_ocean_IMAGE = input("Paste Image here: ")

with open("Vagrantfile") as f:
    newImage=f.read().replace("IMAGE", "{}".format(digital_ocean_IMAGE))

with open("Vagrantfile", "w") as f:
    f.write(newImage)

## Choosing Region

cmd_run_vagrant_list_REGIONS = str("vagrant digitalocean-list regions {}".format(digital_ocean_TOKEN))
os.system(cmd_run_vagrant_list_REGIONS)
print("\nPlease choose a Region\n")

print("Ex. nyc1, sfo1")
digital_ocean_REGION = input("Paste Region here: ")

with open("Vagrantfile") as f:
    newRegion=f.read().replace("REGION", "{}".format(digital_ocean_REGION))

with open("Vagrantfile", "w") as f:
    f.write(newRegion)

## Choosing Size

cmd_run_vagrant_list_SIZES = str("vagrant digitalocean-list sizes {}".format(digital_ocean_TOKEN))
os.system(cmd_run_vagrant_list_SIZES)
print("\nPlease choose a size\n")

print("Ex. s-1vcpu-1gb, s-2vcpu-4gb-intel")
digital_ocean_SIZE = input("Paste Size here: ")

with open("Vagrantfile") as f:
    newSize=f.read().replace("SIZE", "{}".format(digital_ocean_SIZE))

with open("Vagrantfile", "w") as f:
    f.write(newSize)

## Deleting outpute file if it exists

if os.path.exists("output"):
    os.remove("output")
else:
    None

## Change SSH Key location

ssh_key_ans = input("Do you want to specify /.ssh location?[y/n]: ")
if ssh_key_ans == str.casefold("y"):
    ssh_key_loc = input("What is the path?: ")

    with open("Vagrantfile") as f:
        newSSH=f.read().replace("~/.ssh/id_rsa", "{}".format(ssh_key_loc))

    with open("Vagrantfile", "w") as f:
        f.write(newSSH)
    
else:
    print("Leaving default location (~/.ssh/id_rsa)!")





            

