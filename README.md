# ansible-arch-linux

Ansible playbook to setup my Arch Linux machines (i.e., meant to be run against localhost)

## Explanation

* This is meant for _my machine_. You can use it as a guide, but please don't blindly run it on your machine (it will break things).
* This is meant to be run in the [Post-installation](https://wiki.archlinux.org/title/installation_guide#Post-installation) section of the [Installation guide](https://wiki.archlinux.org/title/installation_guide) (i.e., after your partitions are setup, user account is created, fstab is setup, chroot, etc...)

## Requirements

1. Install the necessary packages
   ```
   sudo pacman -S git python
   ```
1. Clone this repo
   ```
   ...
   ```
1. Install Ansible
   ```
   uv sync
   ```
1. Install the Ansible requirements
   ```
   uv run ansible-galaxy install -r requirements.yml
   ```
1. (Optional) Edit the variables in `group_vars`
1. (Optional) Run the playbook in check mode to view potential changes
   ```
   uv run ansible-playbook main.yml --ask-become-pass --check
   ```
1. Run the playbook (enter your user's password when prompted)
   ```
   uv run ansible-playbook main.yml --ask-become-pass
   ```

## Update

To update **everything** (Python packages + Ansible roles) to the latest versions:
```bash
uv lock --upgrade && uv run ansible-galaxy install -r requirements.yml --force
```