
# QuickPark

**QuickPark** is a Django-based web application aimed at providing a smart solution for managing and detecting parking spaces in real-time. It uses computer vision to detect and identify occupied and empty parking spots in a given parking lot.

## Features
- Real-time parking spot detection using computer vision.
- Visual representation of parking spaces (empty and occupied) using a matrix (`'o'` for occupied and `'e'` for empty).
- Integration with Django for backend management.

## Tech Stack
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript (if applicable)
- **Computer Vision**: Custom model for parking spot detection

## Project Structure
- `home`: Django app handling the main functionalities.
- `QuickPark_backend`: Django project directory.
- `static`: Static files for frontend assets.
- `templates`: HTML templates for the web interface.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django 4.x
- OpenCV (for computer vision functionalities)
- Tesseract OCR (if integrated for text detection)

### Installation

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/Spartan1-1-7/QuickPark.git
   cd QuickPark
   \`\`\`

2. **Create a virtual environment** (optional but recommended):
   \`\`\`bash
   python3 -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   \`\`\`

3. **Install dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run migrations**:
   \`\`\`bash
   python manage.py migrate
   \`\`\`

5. **Start the development server**:
   \`\`\`bash
   python manage.py runserver
   \`\`\`

6. **Access the application**:
   Open a browser and go to `http://127.0.0.1:8000/`.

## How It Works
The system processes parking lot images or video streams and detects occupied and available spaces. The matrix output (`'o'` for occupied and `'e'` for empty spots) is generated and displayed on the web interface.

## Contribution
Feel free to contribute to this project by submitting a pull request or reporting issues in the GitHub repository.
