# A Cookiecutter Streamlit Template
This cookiecutter template will initiate a Streamlit project with tools for development, testing and deployment. It supports the following features:

- Uses [uv](https://docs.astral.sh/uv/) for dependency management
- Containerization with [Docker](https://www.docker.com/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

---
## Quickstart
On your local machine, navigate to the directory in which you want to create a project directory, and run the following command:

```bash
uvx cookiecutter https://github.com/rajivnarayan/cookiecutter-streamlit.git
```

or if you don't have uv installed yet:

```bash
pip install cookiecutter
cookiecutter https://github.com/rajivnarayan/cookiecutter-streamlit.git
```

Follow the prompts to configure your project. Once completed, a new directory containing your project will be created. Then navigate into your newly created project directory and follow the instructions in the README.md to complete the setup of your project.

---
## Credits
This project is partially based on the following templates:
- [cookiecutter-andymcdgeo](https://github.com/andymcdgeo/cookiecutter-streamlit)
- [cookiecutter-uv](https://github.com/fpgmaas/cookiecutter-uv)