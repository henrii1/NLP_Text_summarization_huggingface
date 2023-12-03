---
title: Text Summarization
emoji: 🔥
colorFrom: yellow
colorTo: indigo
sdk: gradio
sdk_version: 4.7.1
app_file: app.py
pinned: false
license: mit
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference



# Text Summarization Application

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://huggingface.co/spaces/your-username/your-repo-name)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

This repository contains the source code for a Text Summarization Application that leverages a Hugging Face model and integrates with a Gradio web interface. Continuous integration is set up using Hugging Face Spaces. Additionally, it provides a command-line tool for text summarization and integrates with FastAPI through `main.py`.

## Features

- **Hugging Face Model:** Utilizes a pre-trained model from Hugging Face for text summarization.

- **Gradio Web Interface:** Provides an interactive web interface powered by Gradio for easy input and output interaction.

- **Continuous Integration:** Uses Hugging Face Spaces for continuous integration to ensure reliable and up-to-date deployments.

- **Command-Line Tool:** Includes a command-line tool for convenient text summarization from the terminal.

- **FastAPI Integration:** The `main.py` file integrates with FastAPI, allowing for RESTful API access to the summarization capabilities.

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/henrii1/NLP_Text_summarization_huggingface.git
    cd your-NLP_Text_smmarization_huggingface
    ```

2. **Install Dependencies, Lint, Format and Test:**
    ```bash
    make all
    ```

3. **Run the Application:**
    - For the Gradio web interface:
        ```bash
        python app.py
        ```
    - For the FastAPI integration:
        ```bash
        uvicorn main:app --reload
        ```

4. **Access the Application:**
    - Gradio web interface: Open your browser and go to `http://localhost:7860`.
    - FastAPI: Explore the API at `http://localhost:8000/docs` (Swagger UI) or `http://localhost:8000/redoc` (ReDoc).

## Command-Line Tool

To use the command-line tool for summarization, run:
```bash
python appCLI.py --text "Your input text goes here."
