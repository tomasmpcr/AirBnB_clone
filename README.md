# AirBnB clone - The console

<image src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210706%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210706T134848Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a343ab8f8321ea1066b574d96cee1903d22d4717cde209968ddbeed976d90c6a">

_In this pre-project it is intended to clone an AirBnB only the console, it is expected to have a functional console that allows to add, delete and modify some records and these are saved in json allowing the information to be reloaded once the program is closed_

## Starting 🚀

_Next I will give you a series of instructions that will allow you to have a copy of the project on your local machine._

### Pre-requirements 📋

_Things to install before you can use the project, you will first have to install Python following the next steps_

_First we will see if you already have a pre-installed version of Python_

```
    python --version
```

_If the revision level is lower than 3.7.x, or if Python is not installed, continue to the next step._

#### Step 1: Update and Refresh Repository Lists_

```
    sudo apt update
```

#### Step 2: Install Supporting Software

```
    sudo apt install software-properties-common
```

#### Step 3: Add Deadsnakes PPA

```
    sudo add-apt-repository ppa:deadsnakes/ppa
```
_The system will prompt you to press enter to continue. Do so, and allow it to finish. Refresh the package lists again:_

```
    sudo apt update
```

#### Step 4: Install Python 3

```
    sudo apt install python3.8
```

### Installation 🔧

_To start you should make a copy of the project on your local machine using_

```
    git clone https://github.com/tshuna332/AirBnB_clone.git
```

_To run the AirBnB you just have to use the following command_

```
    ./console.py
```

## Commands available in the application 💻


### The 'help' command will show you a list of available commands

```
    (hbnb) help
```

### The 'create' command is used to create a new instance

```
    (hbnb) create <class name>
```

### The 'delete' command is used to delete a instance

```
    (hbnb) destroy <class name> <object id>
```

### The 'update' command is used to update an attribute of an instance

```
    (hbnb) update <class name> <object id> <attribute name> <attribute value>
```

### The 'all' command can be used alone and will show all instances or put the name of a class in specific to filter

```
    (hbnb) all
```

or

```
    (hbnb) all <class_name>
```

### You can use the 'show' command to view a specific instance

```
    (hbnb) show <class name> <object id>
```

## Authors ✒️

* **Gabriel Ferreira** - (2314@holbertonschool.com)
* **Tomás Martinez** - (2788@holbertonschool.com)

