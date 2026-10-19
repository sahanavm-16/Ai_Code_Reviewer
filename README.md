# AI Code Reviewer

AI Code Reviewer is a small web app built with Streamlit. Paste in a code snippet, choose its programming language, and ask Google's Gemini 2.5 Flash model to review it.

The review is organized into four areas:

- **Strengths** — what the code does well
- **Issues and bugs** — possible mistakes or problems
- **Suggestions** — ideas for improving readability and maintainability
- **Security and optimization tips** — potential safety, performance, or scalability considerations

The app also provides a dark mode toggle and displays the submitted code alongside the review.

> **Note:** AI-generated feedback can be incomplete or incorrect. Verify suggestions and test any code changes before using them.

## How it works

1. Choose a programming language, or leave **Auto Detect** selected.
2. Paste code into the text area.
3. Select **Review My Code**.
4. Read the generated report and the displayed original code.

The language selector includes Python, C, C++, Java, JavaScript, HTML/CSS, SQL, Go, PHP, Rust, Swift, and Other.

## Requirements

- Python installed on your computer
- A Google AI API key with access to Gemini
- Internet access while requesting a review

The Python packages used by the app are listed in [`requirements.txt`](./requirements.txt).

## Installation

Clone the project and move into its directory:

```shell
git clone https://github.com/sahanavm-16/Ai_Code_Reviewer.git
cd Ai_Code_Reviewer
```

Create and activate a virtual environment. On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```shell
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```shell
python -m pip install -r requirements.txt
```

## Configure your API key

The app reads the `GOOGLE_API_KEY` environment variable. Choose one of these methods.

### Option 1: Set it in your terminal

Windows PowerShell:

```powershell
$env:GOOGLE_API_KEY = "your-api-key"
```

macOS or Linux:

```shell
export GOOGLE_API_KEY="your-api-key"
```

Keep this terminal open when you start the app.

### Option 2: Use a local `.env` file

Create a file named `.env` in the project directory with this line:

```text
GOOGLE_API_KEY=your-api-key
```

The app loads this file automatically. `.env` files are excluded from Git by `.gitignore`; never commit or share your API key.

## Start the app

With the virtual environment activated and the API key configured, run:

```shell
streamlit run app.py
```

Streamlit will print a local address in the terminal, usually `http://localhost:8501`. Open it in your browser to use the app.

## Troubleshooting

- **The app cannot find the API key:** Confirm `GOOGLE_API_KEY` is set in the same terminal session, or that `.env` is in the project directory and contains the correct variable name.
- **A package is missing:** Activate the virtual environment and run `python -m pip install -r requirements.txt` again.
- **A review request fails:** Check your internet connection and API key, then try again. Google AI API access or quota restrictions may also prevent a request.
- **The app does not start:** Check that your virtual environment is active and run the command from the project directory.

## Project files

```text
Ai_Code_Reviewer/
├── app.py             # Streamlit application
├── requirements.txt   # Python dependencies
├── .gitignore         # Excludes local files and secrets
└── README.md          # Project documentation
```
