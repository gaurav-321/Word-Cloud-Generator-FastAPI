# 📌 Word Cloud Generator FastAPI

✨ **Description:**  
Word Cloud Generator FastAPI is a lightweight and efficient tool that allows users to generate visually appealing word clouds directly from their text inputs. Perfect for data visualization, reports, and more!

🚀 **Features:**
- **FastAPI Integration**: Utilizes the powerful FastAPI framework for building robust web APIs.
- **Real-Time Word Cloud Generation**: Generate word clouds in real-time with minimal latency.
- **Base64 Encoded Output**: Retrieve your word cloud as a base64 encoded image string, easily embeddable in web applications.

🛠️ **Installation:**  
To get started, ensure you have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install fastapi uvicorn jieba re
```

📦 **Usage:**  
Here’s how to use the Word Cloud Generator FastAPI:

1. Import the necessary modules:
    ```python
    from fastapi import FastAPI, HTTPException
    from word_gen import create_word_cloud
    import base64
    ```

2. Create an instance of the FastAPI app:
    ```python
    app = FastAPI()
    ```

3. Define a route to generate and return a word cloud:
    ```python
    @app.post("/generate-word-cloud/")
    async def read_user_me(query: str):
        try:
            # Generate word cloud image
            word_cloud_image = create_word_cloud(query)
            
            # Encode the image in base64
            encoded_image = base64.b64encode(word_cloud_image).decode('utf-8')
            
            return {"word_cloud": encoded_image}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    ```

🔧 **Configuration:**  
No additional configuration is required for this project. Simply ensure all dependencies are installed.

🧪 **Tests:**  
This project includes basic unit tests to ensure the word cloud generation works as expected. To run the tests:

```bash
pytest
```

📁 **Project Structure:**
```
Word-Cloud-Generator-FastAPI/
├── main.py
├── word_gen.py
└── requirements.txt
```

🙌 **Contributing:**  
We welcome contributions from the community! Please follow these guidelines to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Make your changes and commit them (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

📄 **License:**  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ by gag3301v**

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/gag3301v/Word-Cloud-Generator-FastAPI)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/gag3301v/Word-Cloud-Generator-FastAPI?style=social)](https://github.com/gag3301v/Word-Cloud-Generator-FastAPI)