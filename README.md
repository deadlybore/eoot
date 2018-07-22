# EOOT: Easy Out-Of-Tree
This tools aim to ease the generation of Out-Of-Tree drivers

# Requirements
* vagrant-sshfs

# With vagrant
Simply launch `vagrant up` and the drivers specified in
`host_vars/localhost/drivers.yml` will be build on a `debian/stretch64` box

# Add new drivers
Add the new driver in `host_vars/localhost/drivers.yml` like this :
```yaml
drivers:
  - name: driver_name
    url: where to download the driver
    version: the version of the driver
    custom_dkms_conf: |
      put
      custom
      conf
      here
      and dkms.conf.j2
      will
      be
      ignored
    custom_retrieval: driver.yml
```
For `custom_retrieval` add the tasks to execute in a 'role' in `custom_retrieval`. See `megaraid_sas` for an example.
