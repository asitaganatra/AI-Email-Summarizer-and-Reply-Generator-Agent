# 📧 AI Email Summarizer and Reply Generator Agent

An intelligent AI-powered application that automatically summarizes emails and generates contextual replies in multiple tones using Google's Gemini API and Streamlit.

## Features

- **Email Summarization**: Automatically generate concise 3-point summaries of any email
- **Smart Reply Generation**: Create two distinct reply options (Accepting/Positive and Declining/Requesting More Info)
- **Customizable Tone**: Choose from multiple tone options:
  - Formal
  - Casual
  - Urgent
  - Friendly
- **Real-time Processing**: Instant analysis using Google Gemini 2.5 Flash model
- **User-Friendly Interface**: Clean and intuitive Streamlit UI

## Technologies Used

- **Frontend**: Streamlit
- **AI Model**: Google Gemini 2.5 Flash
- **Language**: Python 3.13
- **Key Libraries**:
  - google-genai (Gemini API client)
  - streamlit (Web UI)
  - python-dotenv (Environment variable management)

## Installation

### Prerequisites

- Python 3.13 or higher
- Google Gemini API key

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/asitaganatra/AI-Email-Summarizer-and-Reply-Generator-Agent.git
   cd AI-Email-Summarizer-and-Reply-Generator-Agent
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the project root directory
   - Add your Google Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

### Local Deployment

1. **Start the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   - The app will open in your default browser at `http://localhost:8501`

3. **Use the application**
   - Paste your email content in the text area
   - Select your preferred reply tone from the sidebar
   - Click "Analyze & Generate Replies 🚀" button
   - Review the generated summary and reply options

### Cloud Deployment

Deploy this application to Streamlit Cloud for free:

1. **Push code to GitHub** (already done ✓)
2. **Visit [Streamlit Cloud](https://streamlit.io/cloud)**
3. **Connect your GitHub account and deploy**
   - Select the repository: `AI-Email-Summarizer-and-Reply-Generator-Agent`
   - Set the main file path: `app.py`
   - Add your `GEMINI_API_KEY` in the Secrets section (equivalent to `.env`)
4. **Share your live app link** with others!

**Live Demo**: Coming soon after cloud deployment! 🚀

## Project Structure

```
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create this)
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## How It Works

1. **Input Processing**: User provides an email and selects a tone preference
2. **AI Analysis**: The Gemini API processes the email with a sophisticated system prompt
3. **Output Generation**: 
   - Generates a 3-point summary
   - Creates two distinct reply options in the selected tone
4. **Display**: Results are presented in a clean, easy-to-read format

## API Key Setup

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Add it to your `.env` file as `GEMINI_API_KEY`

## Requirements

See `requirements.txt` for complete dependencies list.

## Error Handling

The application includes robust error handling:
- Validates API key connectivity on startup
- Handles empty email inputs
- Catches and displays API errors gracefully

## Future Enhancements

- Support for multiple email formats (HTML, MIME)
- Email attachment preview
- Reply templates and customization
- Email history and favorites
- Batch processing for multiple emails
- Integration with email clients (Gmail, Outlook)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

**Asita Ganatra**
- GitHub: [@asitaganatra](https://github.com/asitaganatra)

## Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/asitaganatra/AI-Email-Summarizer-and-Reply-Generator-Agent).

---

**Note**: Ensure your `.env` file is added to `.gitignore` to keep your API key secure.
