# Word Cloud Generator API
This API allows users to generate word clouds from a given string of text. It is built using FastAPI and uses the wordcloud library to generate the word clouds.

## Endpoints
**/cloud** - Accepts a POST request with a JSON body containing a 'query' field. The API will generate a word cloud from the text in the 'query' field and return the image as a base64 encoded string.
## Requirements
Python 3.7+
fastapi, uvicorn, and wordcloud Python modules
jieba and re libraries
## Running the API
To run the API, simply execute the main.py script. The API will run on **http://127.0.0.1:80**. To send a request to the API, send a POST request to the /cloud endpoint with a JSON body containing a **'query'** field with the text you want to generate a word cloud from.
