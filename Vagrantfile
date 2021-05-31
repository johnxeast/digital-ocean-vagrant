# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The  in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure('ADDME') do |config|

    config.vm.define 'droplet1' do |config|
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
    end
    
    "ADDME"
    
  end