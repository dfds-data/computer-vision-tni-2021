# Computer Vision T&I Conf 2021

Showcase computer vision capabilities

## Quickstart

### With Docker

Open a terminal and run

```shell
docker compose up
```

Now open your browser at http://localhost:5050/

If you don't want to wait for the docker image to build, you can download a pre-built image at 
https://hub.docker.com/repository/docker/klaurdfds/computervision

### Without Docker

Create a virtualenv, activate it.

Then install dependencies:
```shell
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

Install pre-commit
```shell
pre-commit install
```

Test installation
```shell
pre-commit run --all-files
pytest
```

Run the webapp
```shell
streamlit run src/webapp.py
```

Now open your browser at http://localhost:8501/


## People

- [Kasper Lauritzen](mailto:klaur@dfds.com) 
- [Dennis Hansen](mailto:dhans@dfds.com) 