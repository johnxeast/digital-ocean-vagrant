import os
import sys


digital_ocean_TOKEN = input("Paste token here: ")

with open("Vagrantfile") as f:
    newToken=f.read().replace("TOKEN", "{}".format(digital_ocean_TOKEN))

with open("Vagrantfile", "w") as f:
    f.write(newToken)

cmd_run_vagrant_list_IMAGES = str("vagrant digitalocean-list images {}".format(digital_ocean_TOKEN))
os.system(cmd_run_vagrant_list_IMAGES)
print("\nPlease choose from the above Images to use for your vagrant machines\n")

print("Ex. ubuntu-18-04-x64, centos-8-x64")
digital_ocean_IMAGE = input("Paste Image here: ")

with open("Vagrantfile") as f:
    newImage=f.read().replace("IMAGE", "{}".format(digital_ocean_IMAGE))

with open("Vagrantfile", "w") as f:
    f.write(newImage)


cmd_run_vagrant_list_REGIONS = str("vagrant digitalocean-list regions {}".format(digital_ocean_TOKEN))
os.system(cmd_run_vagrant_list_REGIONS)
print("\nPlease choose a Region\n")

print("Ex. nyc1, sfo1")
digital_ocean_REGION = input("Paste Region here: ")

with open("Vagrantfile") as f:
    newRegion=f.read().replace("REGION", "{}".format(digital_ocean_REGION))

with open("Vagrantfile", "w") as f:
    f.write(newRegion)

cmd_run_vagrant_list_SIZES = str("vagrant digitalocean-list sizes {}".format(digital_ocean_TOKEN))
os.system(cmd_run_vagrant_list_SIZES)
print("\nPlease choose a size\n")

print("Ex. s-1vcpu-1gb, s-2vcpu-4gb-intel")
digital_ocean_SIZE = input("Paste Size here: ")

with open("Vagrantfile") as f:
    newSize=f.read().replace("SIZE", "{}".format(digital_ocean_SIZE))

with open("Vagrantfile", "w") as f:
    f.write(newSize)

if os.path.exists("output"):
    os.remove("output")
else:
    None