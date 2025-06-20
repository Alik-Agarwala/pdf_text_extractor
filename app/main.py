from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import PyPDF2
from io import BytesIO
import uvicorn

app = FastAPI()

# Endpoint to upload the PDF and extract its text
@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    try:
        # Read the uploaded file
        pdf_file = await file.read()
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_file))
        
        text = ""
        # Extract text from each page
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

        # Return the extracted text as a JSON response
        return JSONResponse(content={"extracted_text": text})

    except Exception as e:
        # Return an error response in case of an exception
        return JSONResponse(content={"error": str(e)}, status_code=400)

# Start the app when the script is executed
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3009)
