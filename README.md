# BARTpho Corrector

BARTpho Corrector is a Vietnamese text correction tool, specifically fine-tuned on BARTpho for handling text errors.

---

## Table of Contents
- [Introduction](#introduction)
- [Run the App](#run-the-app)
- [Fine-tuning BARTpho](#fine-tuning-bartpho)
  - [Data](#data)
  - [Training](#training)
- [Data Generator](#data-generator)
- [Future Work](#future-work)
- [License](#license)

---

## Introduction

BARTpho Corrector is a Vietnamese text correction tool built upon the BARTpho model. It has been fine-tuned specifically to correct text errors, particularly in Vpop-related text, leveraging a custom dataset of song lyrics.

Key features include:

An interactive web application for real-time text correction.
A notebook for managing the training process, enabling easy fine-tuning of the model.
A notebook for generating and preprocessing data in the correct format.
This tool is versatile and can be extended or customized to suit other text correction use cases with additional training.

---

## Run the App

### 1. Clone the Repository
```bash
git clone https://github.com/HuyPham235711/BARTpho_Corrector.git
cd BARTpho_Corrector
```

### 2. Set Up the Environment
Create and activate a virtual environment:
```bash
python -m venv BARTpho_venv
BARTpho_venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the app by running:
```bash
python app.py
```

Once the app is running, you should see this message in the terminal:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### 4. Open in Browser
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to access the application.

### review
![BARTpho Corrector Web Interface](review/test_screen.png)
---

## Fine-tuning BARTpho

### Data
- The dataset for training was collected from various sources, primarily **Vpop song lyrics**.  
- This focus ensures the corrector performs particularly well with texts related to Vpop themes.
- Example of the data format:
  ```
  +---------------+---------+
  | Column Name   | Type    |
  +---------------+---------+
  | original      | str     |
  | error         | str     |
  +---------------+---------+
  ```

### Training
- The fine-tuning was performed on Google Colab using the Hugging Face `transformers` library.
- Key training parameters:
  - **Epochs**: 10
  - **Evaluation Steps**: Every 1500 steps
- The resulting model is optimized for correcting Vpop-related texts but can be further fine-tuned for other domains.

---

## Data Generator

You can create your own training data by following the format described above. For assistance, refer to the **`datagen.ipynb`** file in the repository. This notebook provides utilities to preprocess and structure your data into the required format.

---

## Future Work

Here are some potential enhancements for the project:
- Building a complete **pipeline** for automating the correction process.
- Expanding the dataset to include diverse domains beyond Vpop song lyrics.
- Optimizing the model for real-time correction in production environments.
- Deploying the application to cloud platforms for broader accessibility.

---

## License

MIT License

Copyright (c) 2021 VinAI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

