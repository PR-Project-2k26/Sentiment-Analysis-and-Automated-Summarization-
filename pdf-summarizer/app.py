from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pdf_utils import extract_text_from_pdf
from summariser import summarize_large_text

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/summarize/")
async def summarize(file: UploadFile = File(...)):
    text = extract_text_from_pdf(file)
    summary = summarize_large_text(text)
    return {"summary": summary}