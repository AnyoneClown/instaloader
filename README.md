# Django Project

## Setup

The first thing to do is to clone the repository:

```sh
 git clone https://github.com/AnyoneClown/instaloader.git
 cd library
```

Create a virtual environment to install dependencies in and activate it:

```sh
 python -m venv env
 env\Scirpts\activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```


## How to use

### Prepare ur account:

- Login to Instagram in Firefox,
- Execute the snippet, e.g. with python 615_import_firefox_session.py,
- Then use this command in your terminal:

```sh
instaloader -l USERNAME
```

### Change account in main.py

- Change "L.load_session_from_file("USERNAME")" with your username