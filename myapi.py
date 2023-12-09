import paralleldots

class API:
    def __init__(self):
        paralleldots.set_api_key("yqwTAXPCVgnv3UmEOjINhoO5dQFtAJB3xufx1kmLD78")

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment("text")
        return response