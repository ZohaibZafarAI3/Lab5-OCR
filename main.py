from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import pytesseract
from PIL import Image
import io
import re
import uvicorn

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI(title="Document Intelligence API", version="1.0.0")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== HELPER FUNCTIONS ==========
def extract_dates(text):
    patterns = [
        r'\d{1,2}/\d{1,2}/\d{4}',
        r'\d{1,2}-\d{1,2}-\d{4}',
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}',
        r'\d{4}-\d{2}-\d{2}'
    ]
    dates = []
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        dates.extend(matches)
    return dates

def extract_amounts(text):
    pattern = r'\$?\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    amounts = re.findall(pattern, text)
    cleaned = []
    for amount in amounts:
        clean = amount.replace('$', '').replace(',', '')
        try:
            cleaned.append(float(clean))
        except:
            pass
    return cleaned

def extract_invoice_number(text):
    patterns = [
        r'INV-\d{4}-\d{3}',
        r'#\d{5,}',
        r'ORDER-[A-Z0-9]+',
        r'Invoice (?:Number|#):?\s*([A-Z0-9-]+)'
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1) if match.groups() else match.group(0)
    return None

# ========== API ENDPOINTS ==========
@app.get("/")
async def root():
    return {"api": "Document Intelligence System", "version": "1.0.0", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/classify")
async def classify(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)
        
        text_lower = text.lower()
        if "invoice" in text_lower or "inv-" in text_lower:
            doc_type = "invoice"
            confidence = 85.0
        elif "receipt" in text_lower:
            doc_type = "receipt"
            confidence = 85.0
        elif "contract" in text_lower or "agreement" in text_lower:
            doc_type = "contract"
            confidence = 85.0
        else:
            doc_type = "unknown"
            confidence = 50.0
        
        return {"document_type": doc_type, "confidence": confidence, "extracted_text_preview": text[:300]}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/extract")
async def extract(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)
        
        result = {
            "invoice_number": extract_invoice_number(text),
            "dates": extract_dates(text),
            "amounts": extract_amounts(text),
            "full_text_preview": text[:500]
        }
        
        if result["amounts"]:
            result["total_amount"] = max(result["amounts"])
        if result["dates"]:
            result["first_date"] = result["dates"][0]
        
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.post("/process")
async def process(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)
        
        text_lower = text.lower()
        if "invoice" in text_lower:
            doc_type = "invoice"
        elif "receipt" in text_lower:
            doc_type = "receipt"
        elif "contract" in text_lower:
            doc_type = "contract"
        else:
            doc_type = "unknown"
        
        result = {
            "document_type": doc_type,
            "invoice_number": extract_invoice_number(text),
            "dates": extract_dates(text),
            "amounts": extract_amounts(text),
            "processing_summary": {
                "text_length": len(text),
                "dates_found": len(extract_dates(text)),
                "amounts_found": len(extract_amounts(text))
            }
        }
        
        if result["amounts"]:
            result["total_amount"] = max(result["amounts"])
        if result["dates"]:
            result["invoice_date"] = result["dates"][0]
        
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# ========== RUN SERVER ==========
if __name__ == "__main__":
    print("=" * 50)
    print(" API Ready!")
    print("Swagger Docs: http://127.0.0.1:8000/docs")
    print("=" * 50)
    uvicorn.run(app, host="127.0.0.1", port=8000)