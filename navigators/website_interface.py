import json

import requests


class Website:
    def __init__(self, user_agent):
        self.base = "https://base_website.com"
        self.user_agent_header = {"user-agent": f"{user_agent}"}

    def meta_property(self, url, kwargs, page=False):
        if page:
            kwargs["pageType"] = 3
        return self.meta_request(
            "api/home/details/" + url, {"accessLevel": 1, **kwargs}
        )

    def meta_request(self, url, kwargs):
        response = requests.get(
            self.base + url, params=kwargs, headers=self.user_agent_header
        )
        response.raise_for_status()
        return json.loads(response.text[4:])
