import typer, subprocess
import os, os.path

def main(
    # default binding foler is current folder
    workspace_dir: str = typer.Option(
        ..., "--workspace", "-w", help="The absolute path of your workspace"),
    first_time: bool = typer.Option(
        False, "--first", "-f", help="First time to build the development environment"),
):
    """
    Set your workspace directory, please give the absolute path, the path you give will bind to the container's working directory(medical folder)

    If --first is used, the program will help you build the docker image, please make sure the Dockerfile and requirements.txt exists.
    """
    if first_time:
        # check the Dockerfile and requirements.txt exists or not
        package_list = os.path.isfile(os.path.join(os.getcwd(),'requirements.txt'))
        docker_file = os.path.isfile(os.path.join(os.getcwd(),'Dockerfile'))

        if (package_list and docker_file):
            # build docker image
            subprocess.run(['docker', 'build', '--tag', 'medical', '.'])
            # new a docker container, and bind workspace path to container's work_dir(medical folder)
            subprocess.run(['docker', 'run', '-it', '--rm', '-v', '{}:/medical'.format(workspace_dir), 'medical'])
        else:
            print("Please check your requirements.txt and Dockerfile")
    else:
        # new a docker container, and bind workspace path to container's work_dir(medical folder)
        subprocess.run(['docker', 'run', '-it', '--rm', '-v', '{}:/medical'.format(workspace_dir), 'medical'])


if __name__ == "__main__":
    typer.run(main)