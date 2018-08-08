import json
import time

import requests
from pprint import pprint


def load_repositories(json_file):
    repositories_list = []
    try:
        with open(json_file) as json_object_file:
            data = json.load(json_object_file)
            pprint(data)
            for key, value in data.items():
                repositories_list.append(value)

            return repositories_list
    except IOError:
        print("Repository json file not found!")


def get_push(repository_name, push_type):
    request_url = repository_name+push_type
    push_response = requests.get(request_url)
    push_result = push_response.json()
    return push_result


def write_push():
    pass


if __name__ == "__main__":
    lista = load_repositories("../repositories/mercurial_repositories.json")
    for repo in lista:
        pprint(get_push(repo, "json-log"))
        time.sleep(1)
    #temp = get_push("https://hg.mozilla.org/hgcustom/version-control-tools/", "json-log")
    #pprint(temp)
    write_push()
