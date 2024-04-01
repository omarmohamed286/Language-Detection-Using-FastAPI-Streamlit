# language-detection

 This project is a simple web app made using streamlit app that calls fastapi app which serves an ML model trained to detect languages.

 # Usage

To run the api just run:

```uvicorn router:app```

To test the api you can deal with the swagger documentation at:  http://localhost:8000/docs

To run the web app:
```streamlit run streamlit/streamlit.py```

This will open a web page in your default browser at: http://localhost:8501
 
