# 📝 Text Summarization CLI Tool

A simple and powerful command-line interface (CLI) tool for summarizing text from either a URL or a local text file. This tool uses a Hugging Face Transformer model (`t5-small`) under the hood and supports commands via the `click` library. Web content is extracted using BeautifulSoup.

---

## 🚀 Features

- 🔗 Summarize text directly from any webpage URL
- 📄 Summarize content from local `.txt` files
- 🤗 Uses Hugging Face's `t5-small` model for abstractive summarization
- 💻 Built with Python, `click`, `transformers`, and `beautifulsoup4`

---

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-summarization-cli.git
   cd text-summarization-cli
   
2. Install the dependencies and set up the CLI:
   ```bash
   python setup.py develop
   ```
## 🧪 Usage
  
  1.Check available commands
     ```bash 
    summarize --help
     ```
  2.Summarize text from a URL
  ```bash 
    summarize --url https://en.wikipedia.org/wiki/Ruby
  ```
  
  3.Summarize text from a file:
  ```bash 
    summarize --file filename
  ```
