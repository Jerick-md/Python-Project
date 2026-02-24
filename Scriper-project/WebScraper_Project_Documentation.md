# 🌐 WebScraper Project (OOP Version)

## 📌 Project Overview

This project is a simple **Object-Oriented Web Scraper** built using:

-   requests
-   BeautifulSoup
-   os
-   File handling
-   Inheritance (OOP)

It allows the user to:

-   Enter a website URL
-   Extract specific HTML tags
-   Save:
    -   Headers
    -   JSON data (if available)
    -   Full HTML content
    -   Selected tags

------------------------------------------------------------------------

# 🛠 Technologies Used

-   requests → Send HTTP requests\
-   BeautifulSoup → Parse HTML\
-   os → Change working directory\
-   OOP → Code organization

------------------------------------------------------------------------

# 📂 Project Structure

Scriper-project/ │ └── TextFolder/ ├── Header.txt ├── data.json ├──
contentData.txt ├── Tags.txt

------------------------------------------------------------------------

# 🧠 Class Structure

## 🔹 Class: Webscrip

### Constructor

Stores: - URL - Response object

### Methods

1.  get_headers()\
    Saves HTTP response headers into Header.txt

2.  get_json_data()\
    Attempts to extract JSON data and saves into data.json\
    If not JSON, prints warning message.

3.  get_content()\
    Saves full HTML page into contentData.txt

------------------------------------------------------------------------

## 🔹 Class: WebsiteTagsExtracker (Inherits from Webscrip)

### Features

-   Prints status code
-   Handles invalid URL errors
-   Allows user to choose HTML tag
-   Extracts tags using BeautifulSoup
-   Saves extracted tags into Tags.txt

------------------------------------------------------------------------

# 🏷 Supported HTML Tags

title, p, a, div, article, body,\
head, main, nav, iframe, span,\
ul, ol, li, footer, table, video

------------------------------------------------------------------------

# ⚙ How It Works (Flow)

User Input URL\
↓\
Send HTTP Request\
↓\
User Chooses Tag\
↓\
Extract Tags using BeautifulSoup\
↓\
Save Data to Files

------------------------------------------------------------------------

# 🎯 OOP Concepts Used

-   Class
-   Inheritance
-   super()
-   Encapsulation

------------------------------------------------------------------------

# 🛡 Error Handling

-   Invalid URL (MissingSchema)
-   JSON decoding errors
-   Invalid tag input

------------------------------------------------------------------------

# 🚀 Possible Improvements

-   Add connection error handling
-   Add logging system
-   Add CLI menu
-   Scrape all tags automatically
-   Convert to GUI version
-   Turn into API-based scraper

------------------------------------------------------------------------

# 📌 Summary

This project demonstrates:

-   Web scraping fundamentals
-   Object-Oriented Programming
-   File handling
-   Error handling
-   Clean project structure
