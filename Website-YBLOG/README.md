# Project Setup
To set up and prepare the project for execution, follow these steps:
### Step 1: Clone the Project
```sh
git clone [projectRepositoryUrl]
cd app
```
### Step 2: Create a Virtual Environment
```sh
python3 -m venv env
```
### Step 3: Activate the Virtual Environment
```sh
source env/bin/activate
```
### Step 4: Install Dependencies
```sh
pip3 install -r requirements.txt
```


# Running the Project
To run the project, execute the following command in your command-line terminal:
```sh
python3 run.py
```
# Note
If you want to remove the elements of the database.
```sh
sqlite3 database.db
VACUUM
```

<!-- # Game Project

Para correr el juego debes seguir las siguientes instrucciones en la terminal:

```sh
cd game
python3 main.py
```


# App Project

```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
``` -->