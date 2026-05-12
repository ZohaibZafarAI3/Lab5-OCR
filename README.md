# 📄 Document Intelligence System - Project 2

## 🎯 Project Overview
A complete end-to-end document processing pipeline that extracts text from images, classifies document types, and extracts structured information using OCR, Machine Learning, and Natural Language Processing.

---

## 📊 What I Built in 3 Weeks

### Week 6: Advanced OCR with CNN (99.24% Accuracy)
- Built a Convolutional Neural Network from scratch
- Trained on MNIST dataset (70,000 handwritten digits)
- Achieved **99.24% test accuracy**
- Learned how deep learning powers modern OCR systems

**Technologies:** TensorFlow, Keras, CNN, MaxPooling, Dropout

### Week 7: Information Extraction with Regex & NER
- Extracted dates in multiple formats (MM/DD/YYYY, Month DD, YYYY)
- Extracted currency amounts with $ handling
- Extracted invoice/order numbers using patterns
- Used spaCy for Named Entity Recognition (People, Organizations, Locations)
- Visualized entities with displaCy

**Technologies:** Regular Expressions, spaCy, displaCy

### Week 8: Document Classification & REST API
- Trained document classifier (invoice/receipt/contract)
- Used TF-IDF vectorization with 1000 features
- Achieved **100% accuracy** on test set
- Built production-ready REST API with FastAPI
- Created interactive Swagger documentation

**Technologies:** FastAPI, scikit-learn, Joblib, Uvicorn

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🔍 OCR Pipeline | Extracts text from images using Tesseract |
| 📝 Digit Recognition | CNN model with 99.24% accuracy |
| 📅 Date Extraction | Supports multiple date formats |
| 💰 Amount Extraction | Handles $1,250.50, 1250.50, $1250 |
| 🏢 NER | Extracts People, Organizations, Locations |
| 📄 Classification | Identifies invoices, receipts, contracts |
| 🔌 REST API | FastAPI with 4 endpoints |
| 📚 Documentation | Interactive Swagger UI |

---

## 🛠️ Technologies Used
 Python 3.14 │
├─────────────────────────────────────────────────────────┤
│ 🔬 Machine Learning: scikit-learn, TensorFlow/Keras │
│ 🖼️ Image Processing: OpenCV, PIL, Tesseract OCR │
│ 📊 NLP: spaCy, Regular Expressions │
│ 🌐 API: FastAPI, Uvicorn │
│ 📦 Utilities: Joblib, NumPy, Matplotlib │
