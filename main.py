# Author: Lasith Manujitha
# Github: @z1nc0r3
# Description: A simple plugin to shorten URLs using cleanuri.com
# Date: 2024-02-04

import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
import webbrowser
import requests
import pyperclip

class HelloWorld(FlowLauncher):

    def query(self, query):
        output=[]
        if len(query.strip()) == 0:
                output.append({
                    "Title": "Enter a URL to shorten",
                    "IcoPath": "Images/app.png"})
        
        else:
            url = "https://cleanuri.com/api/v1/shorten"
            payload = {'url': {query}}

            response = requests.request("POST", url, data=payload)

            print(response.text)
            tiny = response.json()['result_url']
                       
            output.append({
                    "Title": "Click to copy",
                    "IcoPath": "Images/shorten.png",
                    "JsonRPCAction": {"method": "copy", "parameters":[{tiny}]  }
                    })
            
            output.append({
                    "Title": "Click to open in browser",
                    "IcoPath": "Images/shorten.png",
                    "JsonRPCAction": {"method": "open_url", "parameters":[{tiny}]  }
                    })
            
        return output

    def context_menu(self, data):
        return [
            {
                "Title": "Hello World Python's Context menu",
                "SubTitle": "Press enter to open Flow the plugin's repo in GitHub",
                "IcoPath": "Images/app.png",
                "JsonRPCAction": {
                    "method": "open_url",
                    "parameters": ["https://github.com/Flow-Launcher/Flow.Launcher.Plugin.HelloWorldPython"]
                }
            }
        ]
        
    def copy(self, tiny):
        pyperclip.copy(tiny)

    def open_url(self, url):
        webbrowser.open(url)

if __name__ == "__main__":
    HelloWorld()
