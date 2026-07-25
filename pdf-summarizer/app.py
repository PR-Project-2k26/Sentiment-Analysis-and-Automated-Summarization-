from fastapi import FastAPI, UploadFile, File, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pdf_utils import extract_text_from_pdf
from summariser import summarize_large_text

app = FastAPI(
    title="AI PDF Summarizer",
    description="Extract text from a PDF and generate an AI-powered summary using Groq.",
    version="1.0.0"
)

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/summarize/")
async def summarize(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    try:
        text = extract_text_from_pdf(file)

        if not text.strip():
            raise HTTPException(
                status_code=400,
                detail="No readable text found in the uploaded PDF."
            )

        summary = summarize_large_text(text)

        return {
            "filename": file.filename,
            "characters": len(text),
            "summary": summary
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )