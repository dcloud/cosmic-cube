# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "chef/ubuntu-14.04"

    config.vm.network :forwarded_port, guest: 8888, host: 8888

    config.vm.provider "virtualbox" do |vb|
      vb.gui = false
      vb.customize ["modifyvm", :id, "--memory", "2048"]
    end

    config.vm.provision "ansible" do |ansible|
      ansible.sudo = true
      ansible.verbose = 'vv'
      ansible.playbook = "provisioning/site.yaml"
    end

end
