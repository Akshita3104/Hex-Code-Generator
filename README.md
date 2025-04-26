# Hex-Code-Generator

[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-1.1.2-green)](https://flask.palletsprojects.com/)

---

## Overview

**Color Shades Generator** is a sleek, modern web application that allows users to generate beautiful color palettes including shades, tints, or both from any base color. Built with a Python Flask backend and a responsive, interactive frontend, this tool is perfect for designers, developers, and artists looking to create harmonious color schemes effortlessly.

---

## Features

- Generate customizable shades, tints, or both from any color input (name or hex).
- Interactive UI with real-time color preview.
- Copy hex color codes to clipboard with a single click.
- Maintains a history of recent colors for quick access.
- Responsive design optimized for all devices.
- Robust backend API for color shade generation.

---

## Technology Stack

- **Backend:** Python, Flask, Flask-CORS, Matplotlib (for color manipulation)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Others:** LocalStorage for recent color history

---

## Installation & Setup

### Prerequisites

Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone <repository-url>
cd Pragati
```

### Install Dependencies

Use pip to install the required packages:

```bash
pip install flask flask-cors matplotlib
```

### Run the Application

Start the Flask development server:

```bash
python app.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## Usage

1. Enter a color name (e.g., "blue") or hex code (e.g., "#3498db") in the input field.
2. Choose the mode: Shades, Tints, or Both.
3. Select the number of color variants to generate.
4. Click "Generate Shades" to see the palette.
5. Click any color block to copy its hex code to your clipboard.
6. Recent colors are saved and can be quickly reselected.

---

### Screenshots

![Color Shades Generator Homepage](https://github.com/Akshita3104/Hex-Code-Generator/blob/main/screenshots/Screenshot%202025-04-26%20191907.png)

![Color and Shades](https://github.com/Akshita3104/Hex-Code-Generator/blob/main/screenshots/Screenshot%202025-04-26%20191947.png)


### Tips

- Store screenshots in a dedicated folder like `screenshots` for organization.
- Use relative paths to ensure images display correctly on GitHub or other platforms.
- Provide meaningful alt text for accessibility and SEO.

---

## Project Structure

```
Pragati/
├── app.py              # Flask backend application
├── static/             # Frontend static files (HTML, CSS, JS)
│   └── index.html      # Main frontend page
├── screenshots/        # (Optional) Folder to store screenshots
└── README.md           # Project documentation
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements, bug fixes, or new features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please contact the project maintainer.
