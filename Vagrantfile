# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The  in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure('') do |config|

    config.vm.define droplet1 do |config|
        config.vm.provider :digital_ocean do |provider, override|
          override.ssh.private_key_path = '~/.ssh/id_rsa'
          override.vm.box = 'digital_ocean'
          override.vm.box_url = 'https://github.com/devopsgroup-io/vagrant-digitalocean/raw/master/box/digital_ocean.box'
          override.nfs.functional = false
          override.vm.allowed_synced_folder_types = :rsync
          provider.token = '5a39c31632e391defb4b1f7edef68cd168587b79ce4d4989a363bf1b84658b1f'
          provider.image = 'IMAGE'
          provider.region = 'REGION'
          provider.size = 'SIZE'
          provider.backups_enabled = false
          provider.private_networking = false
          provider.ipv6 = false
          provider.monitoring = false
        end
    end
    
    
    config.vm.define 'droplet2' do |config|
        config.vm.provider :digital_ocean do |provider, override|
          override.ssh.private_key_path = '~/.ssh/id_rsa'
          override.vm.box = 'digital_ocean'
          override.vm.box_url = 'https://github.com/devopsgroup-io/vagrant-digitalocean/raw/master/box/digital_ocean.box'
          override.nfs.functional = false
          override.vm.allowed_synced_folder_types = :rsync
          provider.token = '5a39c31632e391defb4b1f7edef68cd168587b79ce4d4989a363bf1b84658b1f'
          provider.image = 'IMAGE'
          provider.region = 'REGION'
          provider.size = 'SIZE'
          provider.backups_enabled = false
          provider.private_networking = false
          provider.ipv6 = false
          provider.monitoring = false
        end
    end

  end