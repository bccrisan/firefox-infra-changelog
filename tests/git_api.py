import json
import requests


def create_link(repository, project_name):
    """
    Takes two parameters (repository and project name) and creates the api link for the json.
    :param repository:
    :param project_name:
    :return: GitHub Api link
    """
    beginning_url = "https://api.github.com/repos/"
    separator_url = "/"
    end_url = "/commits"

    base_url = beginning_url+repository+separator_url+project_name+end_url
    return base_url


def get_commits(link):
    """
    Makes the json request and return the request result as a list.
    :param link:
    :return: json list
    """
    commits_response = requests.get(link)
    commits_result = commits_response.json()
    return commits_result


def write_commits(commit_content, file_name):
    """
    Writes commit content to a provided file.
    :param commit_content:
    :param file_name:
    :return: none
    """
    with open(file_name, "w") as json_file:
        json.dump(commit_content, json_file)


if __name__ == "__main__":
    """
    Main function of the script, currently is used for testing and will suffer severe modifications in the future.
    """
    commits = get_commits(create_link("bccrisan", "fresh-install-programs"))
    commits1 = get_commits(create_link("mozilla-releng", "ship-it"))

    write_commits(commits, "github_changelog.json")

    print(commits)
    print(commits1)
    exit(0)
