import requests as rq
from bs4 import BeautifulSoup as bs
import os

path = r"Your-Patch-here\TextFolder"
os.chdir(path)


class Webscrip: #Class for web scriping
    def __init__(self, url):
        self.url = url
        self.response = rq.get(self.url)#Make a get request to the URL and store the response in an instance variable

    def get_headers(self):#get headers of the website and save it in a text file
        headers = self.response.headers
        with open("Header.txt", 'w', encoding="utf-8") as f:#Open the file in write mode to overwrite existing content
            for key, value in headers.items():
                f.write(f"{key}: {value}\n")

    def get_json_data(self):#get data from the URL in JSON format and save it in a json file
        try:#Some websites may not return JSON data, so we use a try-except block to handle this case
            json_data = self.response.json()
            with open("data.json", 'w', encoding="utf-8") as f:
                f.write(str(json_data))
        except:
            print("⚠ This website does not return JSON data.")

    def get_content(self):#get the content of the webpage and save it in a text file
        with open("contentData.txt", 'w', encoding="utf-8") as f:
            f.write(self.response.text)

#WebsiteTagsExtracker class inherits from Webscrip and is responsible for extracting specific HTML tags from the webpage and saving their content in a text file. It also calls the methods from the Webscrip class to save the webpage content, JSON data, and headers.
class WebsiteTagsExtracker(Webscrip):
    #Override the __init__ method to handle invalid URLs and print the status code of the response
    def __init__(self, url):
        try:
            super().__init__(url)
            print("Status Code:", self.response.status_code)
        except rq.exceptions.MissingSchema:
            print("❌ Invalid URL. Please include https://")
            exit()
    #The main method prompts the user to enter an HTML tag, checks if it's valid, and if so, extracts all occurrences of that tag from the webpage and saves them in a text file. It also calls the methods to save the webpage content, JSON data, and headers.
    def main(self):
        print("""
        GET ALL TAGS IN HTML
        Tags: title, p, a, div, article, body,
              head, main, nav, iframe, span,
              ul, ol, li, footer, table, video
        """)

        list_of_tags = [
            'title', 'p', 'a', 'div', 'article', 'body',
            'head', 'main', 'nav', 'iframe', 'span',
            'ul', 'ol', 'li', 'footer', 'table', 'video'
        ]
        #Prompt the user to enter an HTML tag and convert it to lowercase for case-insensitive comparison
        ask_for_tag = input("Enter HTML Tag: ").lower()

        if ask_for_tag in list_of_tags:
            soup = bs(self.response.text, 'html.parser')
            elements = soup.find_all(ask_for_tag)

            if elements:
                with open('Tags.txt', 'w', encoding="utf-8") as f:
                    for element in elements:
                        f.write(str(element) + "\n")
                print("✅ Tag content saved.")
            else:
                print("⚠ Tag not found in this webpage.")

            self.get_content()
            self.get_json_data()
            self.get_headers()
        else:
            print("❌ Tag is invalid.")


askUrl = input("Enter URL: ")
testcase2 = WebsiteTagsExtracker(askUrl)
testcase2.main()