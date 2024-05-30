# 🌐 Smart Web Scraper Q&A with Gemini LLM 🦙🦜

This project is a web-based application built with Streamlit that allows users to scrape text content from a URL and ask questions about the content using a custom LLM (Language Learning Model) based on Gemini. The application uses modern NLP techniques to process and retrieve relevant information from the scraped content.

## Features

- **Web Scraping**: Fetches and processes text content from a provided URL.
- **Question Answering**: Utilizes a custom LLM (Gemini) to answer user queries based on the scraped content.
- **User-Friendly Interface**: Simple and intuitive interface built with Streamlit.
- **Interactive Visuals**: Styled with custom CSS for a better user experience.

## Installation

To get started with the application, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/smart-web-scraper-qa.git
   cd smart-web-scraper-qa
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up Streamlit secrets**:
   Add your Gemini API key to the .streamlit/secrets.toml file:
   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```
4. **Run the application**:
   ```bash
   streamlit run streamlit_gemini.py
   ```
