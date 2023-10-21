import requests, json

def get_selenium_status(remote_url: str):
    """
    The function retrieves the status of a Selenium server located at a specified remote URL.
    
    :param remote_url: The URL of the Selenium server to which the client is connected
    :type remote_url: str
    :return: a dictionary object that contains the status information of the Selenium server running at
    the specified remote URL. The dictionary may contain information such as the Selenium version, the
    number of active sessions, and the status of the server.
    """

    url = f"{remote_url}/wd/hub/status"
    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)


def get_node_available(remote_url: str) -> int:
    """
    Get number of selenium grid node available

    Parameters:
        remote_url (str): Selenium grid remote url

    Returns:
        no_of_nodes_available (int): Number of nodes available in selenium grid  # noqa E501

    """
    result = 0
    try:
        res = get_selenium_status(remote_url)
        ready = res["value"]["ready"]
        if ready:
            nodes = res["value"]["nodes"]
            nodes_available = [
                node for node in nodes if not node["slots"][0]["session"]
            ]
            result = len(nodes_available)
        else:
            print("Selenium hub is not ready")
            result = 0
        
    except Exception as e:
        print(f"selenium hub error => {e}")
    finally:
        print(f"Numbers of node available in default selenium grid - {result}")
        return result