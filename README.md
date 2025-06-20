
# PDF Text Extractor API

This is a FastAPI-based web application that allows users to upload PDF files and extract text from them. The API uses the `PyPDF2` library to read and extract text from PDF documents.

## Features
- Upload a PDF file via an HTTP POST request.
- Extracts text from all the pages of the PDF.
- Returns the extracted text in a JSON format.

## Requirements
Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- FastAPI
- Uvicorn (for running the FastAPI server)
- PyPDF2 (for PDF text extraction)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/pdf-text-extractor.git
   cd pdf-text-extractor
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Requirements file**:
   `requirements.txt` should contain:
   ```
   fastapi
   uvicorn
   PyPDF2
   ```

## Running the Application

1. **Start the FastAPI server**:
   ```bash
   uvicorn app.main:app --reload
   ```

   The server will be running at `http://127.0.0.1:8000`.

2. **API Documentation**:
   FastAPI automatically generates API documentation. You can access it by visiting:
   ```
   http://127.0.0.1:8000/docs
   ```
   This documentation provides a UI to test the API by uploading a PDF file and getting the extracted text.

## API Endpoints

### POST `/extract-text/`
This endpoint allows you to upload a PDF file and extracts its text.

#### Request
- **Method**: `POST`
- **Endpoint**: `/extract-text/`
- **Request Body**: A multipart form-data containing a PDF file.

Example using `curl`:
```bash
curl -X 'POST'   'http://127.0.0.1:8000/extract-text/'   -H 'accept: application/json'   -H 'Content-Type: multipart/form-data'   -F 'file=@path_to_your_pdf_file.pdf'
```

#### Response
- **Status**: 200 OK
- **Response Body**:
  ```json
  {
    "extracted_text": "This is the extracted text from the PDF."
  }
  ```

If an error occurs (e.g., invalid PDF format), the response will contain an error message:
```json
{
  "error": "Some error message"
}
```

## Testing the API

### Via Browser:
1. Visit `http://127.0.0.1:8000/docs` in your browser.
2. Use the interactive UI to upload a PDF file and extract its text.

### Via `curl`:
Use the following `curl` command to upload a PDF and receive the extracted text:

```bash
curl -X 'POST'   'http://127.0.0.1:8000/extract-text/'   -H 'accept: application/json'   -H 'Content-Type: multipart/form-data'   -F 'file=@path_to_your_pdf_file.pdf'
```

### Via Postman:
1. Open Postman and select `POST` as the HTTP method.
2. Set the URL to `http://127.0.0.1:8000/extract-text/`.
3. In the "Body" tab, select `form-data`, and choose a file to upload under the key `file`.
4. Click "Send" to get the response.
