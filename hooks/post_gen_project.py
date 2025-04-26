import os
import shutil
import subprocess

project_slug = "{{ cookiecutter.project_slug }}"
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove(rel_filepath: str) -> None:
    filepath = os.path.join(PROJECT_DIRECTORY, rel_filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)
    if os.path.isdir(filepath):
        shutil.rmtree(filepath)

def move(src: str, target: str) -> None:
    srcpath = os.path.join(PROJECT_DIRECTORY, src)
    targetpath = os.path.join(PROJECT_DIRECTORY, target)   
    if os.path.isfile(srcpath):
        os.rename(srcpath, targetpath)
    if os.path.isdir(srcpath):
        shutil.move(srcpath, targetpath)

if "{{ cookiecutter.include_streamlit_config }}" != 'y':
    remove(os.path.join('.streamlit', 'config.toml'))

if "{{ cookiecutter.include_streamlit_secrets }}" != 'y':
    remove(os.path.join('.streamlit', '.secrets.toml'))

if "{{ cookiecutter.include_pages_folder_for_multi_page_app }}" != 'y':
    remove('pages')

if "{{ cookiecutter.include_tests }}" != 'y':
    remove('tests')

if "{{ cookiecutter.include_src_directory }}" != 'y':
    remove('src')

if "{{ cookiecutter.include_docker_file }}" != 'y':
    remove('Dockerfile')

if "{{ cookiecutter.include_devcontainer }}" != 'y':
    remove('.devcontainer')

LICENSES = {
    "Apache Software License 2.0" : "LICENSE_APACHE.txt",
    "GNU General Public License v3" : "LICENSE_GPL.txt",
    "MIT license" : "LICENSE_MIT.txt",
    "BSD license" : "LICENSE_BSD.txt",
    }

for license_name, license_file in LICENSES.items():
    if "{{cookiecutter.license}}" == license_name:
        move(license_file, "LICENSE.txt")
    else:
        remove(license_file)

# generate empty .env file
subprocess.call(['touch', '.env'])

# generate uv.lock
subprocess.call(['uv', 'lock'])

if __name__ == '__main__':
    print(f'Streamlit App successfully created at: {os.path.join(PROJECT_DIRECTORY)}')
    