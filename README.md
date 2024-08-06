# Data Analysis Interface with Streamlit and OpenAI's LLM

## Overview

This project leverages the Streamlit library to create an interactive web interface for data analysis. Users can upload data files in CSV format, which are then analyzed with the help of a Language Learning Model (LLM) from OpenAI. The analysis is facilitated by LangChain's Pandas DataFrame agent, providing insightful responses to predefined questions and enabling users to ask specific queries about their data.

## Features

- **Streamlit Interface**: A user-friendly web interface for uploading and analyzing CSV data files.
- **Predefined Questions**: The application begins with a set of predefined questions that offer a general overview of the data file.
- **Custom Queries**: Users can select specific columns and ask custom questions to the LLM for a more detailed analysis.
- **LangChain Integration**: Utilizes LangChain's Pandas DataFrame agent to interface with the data and generate insights.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Streamlit
- OpenAI API key
- LangChain

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/data-analysis-streamlit-llm.git
    cd data-analysis-streamlit-llm
    ```

2. **Install the required packages**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up OpenAI API Key**
    - Obtain your API key from [OpenAI](https://openai.com/api/).
    - Create a `.env` file in the project root and add your API key:
        ```plaintext
        OPENAI_API_KEY=your_openai_api_key
        ```

### Running the Application

1. **Start the Streamlit server**
    ```bash
    streamlit run EDA_with_langchain_streamlit.py
    ```

2. **Open your web browser**
    - Navigate to `http://localhost:8501` to access the application.

## Usage

### Uploading a CSV File

1. **Upload your CSV file**: Click on the "Browse files" button to select and upload your CSV file.

### Initial Analysis

2. **General Overview**: The application will provide answers to predefined questions that give a general overview of the data.

### Custom Analysis

3. **Select Data Column**: Choose a specific column from the dropdown menu for detailed analysis.
4. **Ask Questions**: Enter your custom questions regarding the selected column. The LLM will analyze the data and provide insightful responses.

## Project Structure

- **EDA_with_langchain_streamlit.py**: The main application file containing the Streamlit interface.
- **requirements.txt**: Lists the dependencies required for the project.

## Project Demo

Watch the demo video by clicking [here](path/to/your/video.mp4).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)
- [LangChain](https://github.com/langchain/langchain)
