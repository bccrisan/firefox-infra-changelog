import json
import requests
import webbrowser

from pprint import pprint
from datetime import datetime


def load_repositories(json_file):
    repositories_list = []
    try:
        with open(json_file) as json_object_file:
            data = json.load(json_object_file)
            # pprint(data)
            for key, value in data.items():
                repositories_list.append(value)

            return repositories_list
    except IOError:
        print("Repository json file not found!")


def get_push(repository_name, push_type):
    request_url = repository_name + push_type
    push_response = requests.get(request_url)
    push_result = push_response.json()
    return push_result


def write_push():
    pass


def handle_timestamps(timestamp, timezone):
    """
    This function handles the timestamps so that all of the modifications to be traceable in time, and converts the unix
    timestamp to date-time format and returns it..

    Example :
        print(handle_timestamps("1499225169.0", "-43200"))
    Output:
        2017-07-05 15:26:09

    :param timestamp: Timestamp in unix systems (an unique time represented in how many seconds past a certain event)
    :param timezone: Timezone of the timestamp
    :return: Returns "YYYY-MM-DD HH:MM:SS"
    """
    if "-" in timezone:
        ts = int(timestamp[:-2]) - int(timezone)
    else:
        ts = int(timestamp[:-2]) + int(timezone)
    return datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


def write_html_output(message):
    """
    Write the HTML output file
    :return:
    """
    f = open("output_html.html", "w")

    if message == "":
        raise IOError
        print("Exiting...")
        exit(0)
    else:
        message_part1 = """
            <html>
            <head></head>
            <body><p>"""

        message_part2 = """
            </p></body>
            </html>
            """
    final_message = message_part1 + message + message_part2
    f.write(final_message)
    f.close()


def open_in_browser(name_of_the_html_file):
    """
    Opens the output webpage in the default os web browser
    :param name_of_the_html_file: HTML file name
    :return: None (except the opening of the HTML file in web browser)
    """
    webbrowser.open_new_tab(name_of_the_html_file)


if __name__ == "__main__":
    repository_list = load_repositories("../repositories/mercurial_repositories.json")

    # for i in range(len(repository_list)):
    #    print(repository_list[i])

    print(repository_list.pop(1))


    #for repo in repository_list:
    #    pprint(get_push(repo, "json-log"))

    temp = get_push("https://hg.mozilla.org/build/nagios-tools/", "json-log")
    # pprint(temp["changeset_count"])
    for i in range(temp["changeset_count"]):
        pprint(temp["changesets"][i])
    # pprint(temp)
    # write_push()
    # open_in_browser("Test")

