# Functionality Summarizer using GenAI and AutoGen

## Overview

Functionality Summarizer is a Python-based code summarization tool that parses source files and generates human-readable summaries for each function and class using Large Language Models (LLMs). It leverages Microsoft's AutoGen framework to facilitate LLM-agent interaction, enabling automated and accurate code explanation.

---

## Key Features

- Parses Python code using the built-in `ast` module
- Utilizes OpenAI’s GPT models via AutoGen to generate concise function/class summaries
- Structured input and output folder system for batch summarization
- Stores per-file summaries in `.json` format for easy retrieval and documentation
- Designed for extensibility with support for additional LLMs (Gemini, CodeLlama, etc.)

---

## Project Structure

functionality_summarizer/
│
├── input_code/ # Python source files to be analyzed
├── output/ # Generated summaries in JSON format
├── main.py # Core logic that drives the summarization process
├── parser.py # Parses source code using Python AST
├── summarizer.py # AutoGen agent definitions and API configuration
├── requirements.txt # Project dependencies
├── .env # Stores your OpenAI API key (not tracked in Git)
└── .gitignore # Ignores secrets, outputs, and venv


## How to Use

### 1. Clone the Repository

``` 
git clone https://github.com/Saumya-A-coded/functionality_summarizer
cd functionality_summarizer
2. Set Up Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate  # Use source venv/bin/activate on Linux/macOS
3. Install Dependencies

pip install -r requirements.txt
4. Configure API Key
Create a .env file in the root directory:


OPENAI_API_KEY=your-openai-key-here
Ensure that .env is listed in your .gitignore.

5. Add Python Files to Be Summarized
Place any Python files you want summarized inside the input_code/ directory.

6. Run the Summarizer

python main.py
Summaries will be printed in the terminal and saved in the output/ folder.

Output Format (Sample)
Expected output in output/yourfile_summary.json:


[
  {
    "file": "calculator.py",
    "type": "class",
    "name": "Calculator",
    "summary": "This class implements basic arithmetic operations such as add, subtract, multiply, and divide."
  }
]
Known Issues
While summaries are correctly displayed in the terminal, the summary field in the output JSON file currently appears empty due to a serialization or access issue in the AutoGen response. This is being actively addressed.

Future Improvements
Fix the JSON output bug to correctly reflect summaries

Extend support for multi-file and multi-language projects

Export summaries to PDF and Markdown formats

Integrate PlantUML for automatic UML diagram generation

Add web interface using Flask or Streamlit

Author
Saumya Awasthi
