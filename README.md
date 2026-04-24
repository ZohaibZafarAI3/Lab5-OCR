Lab 5: Document Intelligence - OCR Basics
Overview
Extract text from images using Tesseract and EasyOCR with OpenCV preprocessing.

Objectives
Extract text from receipts using Tesseract
Use EasyOCR as second engine
Apply grayscale, blur, and thresholding
Compare before/after preprocessing
Build receipt parser with regex
Technologies
Python, Tesseract, EasyOCR, OpenCV, PyTesseract, Pandas, Matplotlib

Results Table
Receipt Before After Gain

receipt1.jpg 245 389 +144 receipt2.jpg 312 456 +144 receipt3.jpg 278 412 +134 receipt4.jpg 298 435 +137 receipt5.jpg 334 478 +144

Key Findings
Adaptive threshold works better than binary
Preprocessing improved accuracy ~50%
EasyOCR provides confidence scores
Tesseract faster but less accurate on noisy images
Project Files
Lab5-OCR/ ├── lab5_ocr.py ├── requirements.txt ├── receipt_ocr_results.csv ├── receipts/ └── README.md

Installation
pip install pytesseract opencv-python pillow pandas easyocr matplotlib

Conclusion
OCR accuracy improves significantly with preprocessing. Adaptive thresholding best for varied lighting conditions.
