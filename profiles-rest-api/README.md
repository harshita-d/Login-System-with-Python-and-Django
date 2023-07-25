## Vagrant Setup

### Prerequisites

1. VirtualBox: Ensure that VirtualBox is installed on your system. If not, download and install it from the official website: [VirtualBox](https://www.virtualbox.org/).

### Creating the Vagrant Environment

1. Run the command `vagrant init ubuntu/bionic64` to initialize the Vagrantfile for the project.

2. Start the Vagrant server using `vagrant up`.

### Managing the Vagrant Server

- To create an SSH connection to the Vagrant server, run `vagrant ssh`. To exit the SSH session, type `exit`.

- Change to the Vagrant project directory with `cd /vagrant`.

- To stop and destroy the Vagrant server, execute the command: `vagrant destroy`.

- To gracefully exit the Vagrant server, use the command: `vagrant halt`.

### Running Python Files

To run Python files within the Vagrant server, simply execute the following command:

```
python filename.py
```

### Python Virtual Environment

1. Inside the project directory, run `vagrant ssh` to access the Vagrant server.

2. Change to the `/vagrant/` directory using `cd /vagrant/`.

3. Create the Python virtual environment in the Vagrant server:

```
python -m venv ~/env
```

Note: `~/env` refers to the path where the virtual environment will be created.

4. Activate the virtual environment:

```
source ~/env/bin/activate
```

To deactivate the virtual environment, run:

```
deactivate
```

## Setting up VirtualBox and Running a Server

### Prerequisites

1. VirtualBox: Ensure that VirtualBox is installed on your system. If not, download and install it from the official website: [VirtualBox](https://www.virtualbox.org/).

### Steps

1. Clone the Project:

   ```
   git clone <project_repository_url>
   cd <project_folder>
   ```

2. Start Virtual Machine:

   ```
   vagrant up
   ```

3. SSH into the Virtual Machine:

   ```
   vagrant ssh
   ```

4. Change Directory:

   ```
   cd /vagrant
   ```

5. Activate the Virtual Environment:

   ```
   source ~/env/bin/activate
   ```

6. Run the Server:

   ```
   python manage.py runserver 0.0.0.0:8000
   ```

   The Django development server will now be running at `http://127.0.0.1:8000/`.

## Creating Migration Files

To create migration files for the Django app, follow these steps:

1. Navigate to the project code directory:

   ```
   cd source/...... (Replace the ellipsis with the path to the 'profiles-rest-api' folder)
   ```

2. SSH into the Virtual Machine:

   ```
   vagrant ssh
   ```

3. Change Directory:

   ```
   cd /vagrant
   ```

4. Activate the Virtual Environment:

   ```
   source ~/env/bin/activate
   ```

5. Create Migration Files:

   ```
   python manage.py makemigrations profiles_api
   ```

   Replace `profiles_api` with the name of the app for which you want to create migration files.

## Running Migration Files

To apply the migration files to the database, follow these steps:

1. Navigate to the project code directory:

   ```
   cd source/...... (Replace the ellipsis with the path to the 'profiles-rest-api' folder)
   ```

2. SSH into the Virtual Machine:

   ```
   vagrant ssh
   ```

3. Change Directory:

   ```
   cd /vagrant
   ```

4. Activate the Virtual Environment:

   ```
   source ~/env/bin/activate
   ```

5. Run Migrations:

   ```
   python manage.py migrate
   ```

That's it! The Django server should now be up and running, and the database should be up-to-date with the migrations.

## Creating Superuser

To create a superuser, follow these steps:

1. Navigate to the project code directory:

   ```
   cd source/...... (Replace the ellipsis with the path to the 'profiles-rest-api' folder)
   ```

2. SSH into the Virtual Machine:

   ```
   vagrant ssh
   ```

3. Change Directory:

   ```
   cd /vagrant
   ```

4. Activate the Virtual Environment:

   ```
   source ~/env/bin/activate
   ```

5. Create Superuser:

   ```
   python manage.py createsuperuser
   ```

Follow the prompts to set the username, email, and password for the superuser.
