# Simple Microservices Architecture
A simple microservices architecture consisting of three projects (FastAPI, NestJS, and Next.js) 


## Setting the environments variables

Create a new `.env` in the service root directory (`python_service/`) and copy the content of the `.env_sample` file, set the environment variables values accordingly

## Runing the project 

When you are ready with the `.env` file execute in the project root directory 

```{bash}
docker-compose up --build
```

You should see three service building and running `python_service`, `backend-service` and `frontend-dashboard`. 
- `python_service` is running on http://localhost:5000
- `backend-service` is running on http://localhost:4000
- `frontend-dashboard` is running on http://localhost:3000

## python_service

### Running unit tests
To run the unit tests attach to the backend container by executing in the service root directory:
```{bash}
docker-compose exec python_service bash
``` 

When you have successfully attached to the container inside execute  
```{bash}
./run_test.sh
```

### Requirements management

 
**uv** is an extremely fast Python package installer and resolver, written in Rust, and designed as a drop-in replacement for pip and pip-tools workflows. To install it you can run 
```{bash}
pip install uv 
``` 

or 

``` {bash}
curl -LsSf https://astral.sh/uv/install.sh | sh 
```
To setup a virtual environment (locally) with uv run

```{bash}
uv venv .venv
```

The requirements are managed using `uv pip compile`. To add a new package to the requirements:

- First add it to `requirements/core_packages.in`.
- Then regenerate `requirements.txt` using:

  ```{bash}
  uv pip compile requirements/core_packages.in -o requirements.txt
  ```
To install the generated requirements run:
```{bash}
uv pip install -r requirements.txt
```

#### Updating the requirements periodically:

It is important to update the requirements periodically to ensure that the project is using the latest versions of the packages. To do this, run the following command:

```{bash}
pip-compile -U requirements/core_packages.in -o requirements.txt
```

(Note the `-U` flag which updates the packages to the latest versions)
