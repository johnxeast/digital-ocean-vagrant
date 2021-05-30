# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure('2') do |config|

  config.vm.define "droplet1" do |config|
      config.vm.provider :digital_ocean do |provider, override|
        override.ssh.private_key_path = '~/.ssh/id_rsa'
        override.vm.box = 'digital_ocean'
        override.vm.box_url = "https://github.com/devopsgroup-io/vagrant-digitalocean/raw/master/box/digital_ocean.box"
        override.nfs.functional = false
        override.vm.allowed_synced_folder_types = :rsync
        provider.token = '380caa2a2cf938c649a91e936bab8946f5d354b628d2a7ee59d8501cec595f61'
        provider.image = 'ubuntu-18-04-x64'
        provider.region = 'nyc1'
        provider.size = 's-1vcpu-2gb-intel'
        provider.backups_enabled = false
        provider.private_networking = false
        provider.ipv6 = false
        provider.monitoring = false
        provider.setup = true
      end
  end

  config.vm.define "droplet2" do |config|

      config.vm.provider :digital_ocean do |provider, override|
        override.ssh.private_key_path = '~/.ssh/id_rsa'
        override.vm.box = 'digital_ocean'
        override.vm.box_url = "https://github.com/devopsgroup-io/vagrant-digitalocean/raw/master/box/digital_ocean.box"
        override.nfs.functional = false
        override.vm.allowed_synced_folder_types = :rsync
        provider.token = '380caa2a2cf938c649a91e936bab8946f5d354b628d2a7ee59d8501cec595f61'
        provider.image = 'ubuntu-18-04-x64'
        provider.region = 'nyc1'
        provider.size = 's-1vcpu-2gb-intel'
        provider.backups_enabled = false
        provider.private_networking = false
        provider.ipv6 = false
        provider.monitoring = false
        provider.setup = true
      end
  end 

end
