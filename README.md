# Audiotize

This project implements two main services:
1. **Audio Transcription Service**: A service that transcribes audio files (with speaker diarization) using the Deepgram API.
2. **Blog Title Generator**: A service that generates SEO-friendly blog title suggestions based on the content provided.

Both services are built using Django and integrate third-party APIs (Gemini Pro for title generation and Deepgram for audio transcription).

## Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Clone the Repository](#1-clone-the-repository)
  - [Set Up the Virtual Environment](#2-set-up-the-virtual-environment)
  - [Install Dependencies](#3-install-dependencies)
  - [Configure API Keys](#4-configure-api-keys)
  - [Database Setup](#5-database-setup)
  - [Run the Django Development Server](#6-run-the-django-development-server)
- [API Endpoints](#api-endpoints)
  - [Audio Transcription with Speaker Diarization](#1-audio-transcription-with-speaker-diarization)
  - [Blog Title Generation](#2-blog-title-generation)
- [Conclusion](#conclusion)

## Features

- **Audio Transcription**: Accepts an audio file, transcribes the content, and includes speaker diarization to differentiate between speakers.
- **Blog Title Generator**: Accepts a blog content and generates multiple title suggestions.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python**: Version 3.7 or higher
- **Django**: Framework to run the project
- **pip**: Python package manager to install dependencies
- **Deepgram API Key**: For transcription service
- **Gemini API Key**: For title generation service

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Omkie-111/Auditize.git
```

### 2. Set Up the Virtual Environment

Create a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install all the required Python dependencies listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

Ensure you have the following dependencies in the `requirements.txt`:

```txt
Django>=3.0,<5.0
google-generativeai
deepgram-sdk
```

### 4. Configure API Keys

- **Gemini API Key**: Obtain your API key from Gemini and set it in the `settings.py` file.

- **Deepgram API Key**: Obtain your Deepgram API key and set it in the `settings.py` file.

In your `settings.py`, add:

```python
# API Keys for external services
API_KEY = "your-gemini-api-key"
DEEPGRAM_API_KEY = "your-deepgram-api-key"
```

### 5. Database Setup

If you're using a database, run the following command to create the necessary database tables:

```bash
python manage.py migrate
```

### 6. Run the Django Development Server

Start the Django development server to test the API endpoints.

```bash
python manage.py runserver
```

The server should now be running at `http://127.0.0.1:8000/`.

## API Endpoints

### 1. **Audio Transcription with Speaker Diarization**

**Endpoint**: `/api/audio-transcription/`

- **Method**: POST
- **Request Payload**: 
    - `audio_file` (file): The audio file (WAV format preferred) for transcription.

- **Response**:
    - JSON object with transcription text and speaker diarization details.

**Example Request**:

```bash
curl -X POST http://127.0.0.1:8000/api/audio-transcription/ \
-H "Content-Type: multipart/form-data" \
-F "audio_file=@/path/to/audio.wav"
```

**Example Response**:

```json
{
  "transcription": [
    {
      "speaker": "Speaker 1",
      "text": "Hello, how are you?"
    },
    {
      "speaker": "Speaker 2",
      "text": "I'm good, thanks for asking!"
    }
  ]
}
```

### 2. **Blog Title Generation**

**Endpoint**: `/api/title-suggestions/`

- **Method**: POST
- **Request Payload**:
    - `content` (string): The blog content for which the title needs to be generated.

- **Response**:
    - `titles` (array): An array of generated blog titles (up to 3 by default).

**Example Request**:

```bash
curl -X POST http://127.0.0.1:8000/api/title-suggestions/ -H "Content-Type: application/json" -d '{"content": "Python development tips to enhance your programming skills and write efficient code."}'
```

**Example Response**:

```json
{
  "titles": [
    "Building Web Applications with Django and Python",
    "Mastering Django for Web Development",
    "The Ultimate Guide to Django Web Development"
  ]
}
```

## Conclusion

This project provides an easy-to-use service for generating blog title suggestions and transcribing audio files with speaker diarization. It's a useful tool for content creators, bloggers, and anyone working with audio transcription.
