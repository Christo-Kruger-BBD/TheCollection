from urllib.parse import urlencode
from Client import Client

class Command:
    def __init__(self, client):
        self.client = client
        self.userId = None
        self.client_id = "d3627dbaee1703774ddd"
        self.loginHeaderMap = {"Content-Type": "application/json"}
        self.headerMap = {}
        self.shellHelper = ShellHelper()

    def login(self):
        response = self.client.postLogin({"client_id": self.client_id}, self.loginHeaderMap)
        responseMap = self.convertStringToMap(response)
        print(f"Please follow the link: https://github.com/login/device\nYour code is: {responseMap['user_code']}")
        
        while True:
            authMap = self.getAuthMap(responseMap['device_code'])
            if 'access_token' in authMap:
                self.headerMap["Authorization"] = f"Bearer {authMap['access_token']}"
                print("Login successful!")
                self.userId = self.client.getUserId(self.headerMap)
                break
            else:
                error = authMap.get('error', '')
                if error == "authorization_pending":
                    print("Awaiting authorization: please entered the provided code at https://github.com/login/device.")
                elif error == "expired_token":
                    print("Authorization code expired: please run the 'login' command again.")
                    break
                else:
                    print("Unspecified error: please run the 'login' command again.")

    def convertStringToMap(self, data):
        return dict(item.split("=") for item in data.split("&"))

    def getAuthMap(self, device_code):
        input("\n\nPress 'enter' to continue once you have authorised this application...")
        authResponse = {"client_id": self.client_id, "device_code": device_code, "grant_type": "urn:ietf:params:oauth:grant-type:device_code"}
        authStr = self.client.postAuth(authResponse, self.loginHeaderMap).split("&")[0]
        return self.convertStringToMap(authStr)

    def getErrorMessage(self, e):
        return self.shellHelper.getErrorMessage(
                "The specified user doesn't exist!" if e.split(" ")[0] == "404" else "Unspecified error: please try again!"
        )

    def isUserSignedIn(self):
        return "you are not logged in. Please log in to be able to use this command!" if self.userId is None else ""
        
class ShellHelper:
    def print(self, message):
        print(message)
        
    def printSuccess(self, message):
        print(f"Success: {message}")
        
    def printError(self, message):
        print(f"Error: {message}")
        
    def getInfoMessage(self, message):
        return f"Info: {message}"
        
    def getErrorMessage(self, message):
        return f"Error: {message}"


# Example usage:
client = Client()
command = Command(client)
command.login()
