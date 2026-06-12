<div align="center">

# 🚀 Project Argus
## **Real-Time Visual Perception & Rapid On-Device Intelligence**

*A modular edge-AI framework integrating low-latency visual acquisition, OCR-driven information extraction, and on-device language model inference into a unified offline-first processing pipeline.*

![Python](https://img.shields.io/badge/Python-3.14+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-green.svg)
![OCR](https://img.shields.io/badge/OCR-EasyOCR-orange.svg)
![AI](https://img.shields.io/badge/LLM-Ollama-red.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

</div>

---

## 📖 Overview

**Project Argus** is a lightweight, offline-first visual intelligence framework designed to bridge the gap between computer vision and local AI inference. The system combines **high-frequency screen acquisition**, **OCR-based structured text extraction**, and **on-device large language model (LLM) integration** into a modular pipeline optimized for low-latency execution.

The architecture enables rapid transformation of visual information into structured digital knowledge while preserving complete local execution and user privacy. By integrating OCR, automated data organization, and local AI infrastructure, Project Argus demonstrates a practical implementation of an edge-AI information processing workflow.

---

## ✨ Key Features

- ⚡ **Low-Latency Visual Acquisition**
  - Automated high-frequency screen capture pipeline.
- 👁️ **Real-Time OCR Processing**
  - Optical Character Recognition powered by EasyOCR.
- 🧹 **Adaptive Text Cleaning**
  - Removes interface artifacts and structures extracted text.
- 🗂️ **Persistent Knowledge Generation**
  - Automatic creation of local text and JSON datasets.
- 🤖 **On-Device AI Integration**
  - Modular interface for local LLM runtimes (Ollama).
- 🔒 **Offline-First Architecture**
  - No dependency on cloud APIs or external inference services.
- 🏗️ **Modular & Extensible Design**
  - Independent pipeline components for future expansion.

---

## 🏛️ System Architecture

```text
                        ┌──────────────────────┐
                        │   Android Device     │
                        └──────────┬───────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │   scrcpy / ADB Link  │
                        └──────────┬───────────┘
                                   │
                                   ▼
                    ┌────────────────────────────┐
                    │  Visual Acquisition Engine │
                    │         (main.py)          │
                    └──────────┬─────────────────┘
                               │
                               ▼
                    ┌────────────────────────────┐
                    │  OCR Recognition Pipeline  │
                    │        (answer.py)         │
                    └──────────┬─────────────────┘
                               │
                  ┌────────────┴────────────┐
                  │                         │
                  ▼                         ▼
        latest_question.txt        Structured Context
                                            │
                                            ▼
                    ┌────────────────────────────┐
                    │  Knowledge Base Generator  │
                    │   (study_assistant.py)     │
                    └──────────┬─────────────────┘
                               │
                               ▼
                    ┌────────────────────────────┐
                    │ Local AI Integration Layer │
                    │    (Ollama Interface)      │
                    └──────────┬─────────────────┘
                               │
                               ▼
                 Intelligent Information Processing
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| **Programming Language** | Python 3 |
| **Screen Mirroring** | scrcpy + Android Debug Bridge (ADB) |
| **Screen Capture** | PyAutoGUI |
| **Window Management** | pywin32 |
| **OCR Engine** | EasyOCR |
| **Image Processing** | Pillow (PIL) |
| **Local AI Runtime** | Ollama |
| **Data Storage** | JSON / TXT / CSV |
| **Development Environment** | Visual Studio Code |

---

## 📂 Repository Structure

```text
project-argus/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── Project_Argus_Demonstration.ipynb
│
├── main.py
├── answer.py
├── study_assistant.py
├── ollama_client.py
│
├── docs/
│   ├── images/
│   └── demo.gif
│
├── capture.py
├── config.py
├── ocr.py
│
└── sample_data/
    ├── sample_question_bank.json
    └── sample_latest_question.txt
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Piyush2135/project-argus.git
cd project-argus
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate the Environment

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Launch the Pipeline

Open separate terminals for each module.

**Terminal 1 — Visual Acquisition**
```bash
py main.py
```

**Terminal 2 — OCR Pipeline**
```bash
py answer.py
```

**Terminal 3 — Knowledge Processing**
```bash
py study_assistant.py
```

---

## 🎥 Demonstration Workflow

The typical execution flow is:

1. Connect an Android device using ADB.
2. Launch `scrcpy` for low-latency screen mirroring.
3. Start the visual acquisition engine (`main.py`).
4. Extract and clean text using the OCR pipeline (`answer.py`).
5. Persist structured information locally (`study_assistant.py`).
6. Optionally interface with a local language model through the Ollama integration layer.

---


---

## 📊 Design Philosophy

Project Argus follows three core engineering principles:

- **Offline-First:** All critical processing is designed to execute locally without reliance on cloud infrastructure.
- **Low Latency:** Pipeline components are optimized for minimal overhead and rapid information flow.
- **Modularity:** Each stage of the architecture can be independently extended, replaced, or improved without affecting the overall system.

---

## 🔮 Future Work

- Desktop dashboard for real-time monitoring.
- Advanced OCR preprocessing and layout analysis.
- Improved local AI orchestration.
- Automated topic classification and indexing.
- Flashcard and revision-sheet generation.
- Extended multimodal document understanding.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request for enhancements, optimizations, or new features.

---

## 📜 License

This project is released under the **MIT License**. See the `LICENSE` file for additional information.

---

<div align="center">

### 🌟 Project Argus
### **Real-Time Visual Perception & Rapid On-Device Intelligence**

**Built with Python • Computer Vision • OCR • Local AI**

*An experimental edge-AI framework exploring the intersection of visual perception, structured information extraction, and on-device intelligence.*

</div>
