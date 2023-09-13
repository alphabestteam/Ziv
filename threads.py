from decorators import timer
import requests
import os
import threading


def url_downloading(current_url: str, venv_file_path: str) -> None:
    """
    The function receives a url and a destination path
    the function downloads the file to the path given
    """
    http_response = requests.get(current_url)
    # The 200 code signifies that the request was received. This make sure the there is actually a response
    if http_response.status_code == 200:
        url_filename = os.path.basename(current_url)
        destination_path = os.path.join(venv_file_path, url_filename)
        with open(destination_path, "wb") as file:
            file.write(http_response.content)


@timer
def list_downloading(url_list: list, venv_file_path: str) -> None:
    """
    The function receives an array of urls
    The function inputs each onw into the url_downloading() function
    The function is also decorated with the timer decorator
    """
    for current_url in url_list:
        url_downloading(current_url, venv_file_path)


@timer
def url_threads(url_list: list, venv_file_path: str) -> None:
    """
    The function receives a list of urls and a destination path
    The function creates a thread for each url
    """
    threads_list = []
    for current_url in url_list:
        current_thread = threading.Thread(
            target=url_downloading, args=(current_url, venv_file_path)
        )
        threads_list.append(current_thread)
        current_thread.start()

    # Blocks one thread until another has finished
    for current_thread in threads_list:
        current_thread.join()


url_list = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
    "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png",
    "https://github.githubassets.com/images/modules/open_graph/github-mark.png",
    "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png",
    "https://www.meshek-milman.co.il/wp-content/uploads/2018/11/1200px-Intel-logo.svg_.png",
]


list_downloading(url_list, "file_path")
url_threads(url_list, "file_path")
