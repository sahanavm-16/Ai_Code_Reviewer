# AI Code Reviewer

A Streamlit app that uses Google's Gemini 2.5 Flash model to review code and provide feedback on strengths, bugs, improvement suggestions, and security or optimization tips. It supports multiple programming languages and includes a dark mode toggle.

## Requirements

- Python 3.9 or later
- A Google AI API key

## Setup

1. Clone the repository and open its directory:

   ```powershell
   git clone https://github.com/sahanavm-16/Ai_Code_Reviewer.git
   cd Ai_Code_Reviewer
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

4. Set your Google AI API key in the current PowerShell session:

   ```powershell
   $env:GOOGLE_API_KEY = "your-api-key"
   ```

   Keep your API key private; do not commit it to the repository.

## Run

From the project directory, with the virtual environment activated and API key set, run:

```powershell
streamlit run app.py
```

Open the local URL printed by Streamlit. Select a language (or use **Auto Detect**), paste code, and choose **Review My Code** to generate a review.
