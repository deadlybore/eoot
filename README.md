# EOOT: Easy Out-Of-Tree
This tool aim to ease the generation of Out-Of-Tree drivers packages.
It retrieves the drivers, compiles it and generates a debian binary package with
dkms.

# Requirements
* vagrant-sshfs

# With vagrant
Simply launch `vagrant up` and the drivers specified in
`host_vars/localhost/drivers.yml` will be built on a `debian/stretch64` box.

If you want to build against a different box simply override it with a `ENV`
environmental variable :
```bash
export ENV='debian/jessie64
```

# Add new drivers
Add the new driver in `host_vars/localhost/drivers.yml` like this :
```yaml
drivers:
  - name: driver_name
    url: where to download the driver
    version: the version of the driver
    custom_dkms_conf: | (optional)
      put
      custom
      conf
      here
      and dkms.conf.j2
      will
      be
      ignored
    custom_retrieval: driver.yml (optional)
```
For `custom_retrieval` add the tasks to execute in a 'role' in `custom_retrieval`.
See `megaraid_sas` for an example.

# Add new kernels
It's possible to build against multiple kernels from multiple distributions.
To do so add a `kernels.yml` file under `vars/DISTRIBUTION/RELEASE`.

Example `Debian/jessie/kernels.yml`:
```yaml
kernels:
  - version: 3.16.0-4
    arch: amd64
  - version: 3.16.0-5
    arch: amd64
  - version: 3.16.0-6
    arch: amd64
  - version: 4.9.0-0.bpo.7
    arch: amd64
```
