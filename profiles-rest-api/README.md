## Vagrant Setup

To create the Vagrant file for the project, follow these steps:

1. Run the command `vagrant init ubuntu/bionic64` to initialize the Vagrant file.
2. Start the Vagrant server using `vagrant up`.

## Vagrant Server

To access and manage the Vagrant server, use the following commands:

- To create an SSH connection to the Vagrant server, run `vagrant ssh`. To exit the SSH session, type `exit`.
- Change to the Vagrant project directory with `cd /vagrant`.

To stop and destroy the Vagrant server, execute the command:

```
vagrant destroy
```

To gracefully exit the Vagrant server, use the command:

```
vagrant halt
```

## Running Python Files

To run Python files within the Vagrant server, simply execute the following command:

```
python filename.py
```

## Python Virtual Environment

To create a Python virtual environment within the Vagrant server, follow these steps:

1. Inside the project directory, run `vagrant ssh` to access the Vagrant server.
2. Change to the `/vagrant/` directory using `cd /vagrant/`.
3. Run the command below to create the virtual environment in the Vagrant server:

```
python -m venv ~/env
```

Note: `~/env` refers to the path where the virtual environment will be created.

To activate the virtual environment, use the following command:

```
source ~/env/bin/activate
```

To deactivate the virtual environment, run:

```
deactivate
```
