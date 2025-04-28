# Unit Converter  

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Supported Units](#supported-units)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Conversion Formulas](#conversion-formulas)
- [Error Handling](#error-handling)
- [License](#license)
- [Contact](#contact)

## Overview
A Flask-based web application that converts between different units of measurement across three categories: length, weight, and temperature.

## Features
- **Three Conversion Categories**:
  - 📏 Length (metric and imperial)
  - ⚖️ Weight (metric and imperial)
  - 🌡️ Temperature (Celsius, Fahrenheit, Kelvin)
- **Input Validation**:
  - Checks for numeric inputs
  - Provides clear error messages
- **User-Friendly Interface**:
  - Clean, responsive design
  - Easy navigation between categories
- **Real-Time Results**:
  - Instant conversion display
  - Accurate calculations

## Supported Units

### Length
| Unit | Description          |
|------|----------------------|
| km   | Kilometer            |
| m    | Meter                |
| dm   | Decimeter            |
| cm   | Centimeter           |
| mm   | Millimeter           |
| μm   | Micrometer           |
| nm   | Nanometer            |
| mi   | Mile                 |
| yd   | Yard                 |
| ft   | Foot                 |
| in   | Inch                 |

### Weight
| Unit | Description          |
|------|----------------------|
| t    | Metric ton           |
| kg   | Kilogram             |
| g    | Gram                 |
| mg   | Milligram            |

### Temperature
| Unit | Description          |
|------|----------------------|
| °C   | Celsius              |
| °F   | Fahrenheit           |
| K    | Kelvin               |

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/unit-converter.git
   cd unit-converter

2. **Create virtual environment (recommended)**:
    ```bash
    python -m venv venv
    # Linux/Mac:
    source venv/bin/activate
    # Windows:
    venv\Scripts\activate

3. **Install the dependecies**
    ```bash
    pip install flask

## Usage
1. **Run the application**:
    ```bash
    python app.py

2. **Access the web interface**:
    Open your browser and navigate to: http://localhost:5000
    
3. **Perform conversions**:

    - Select conversion category

    - Enter the value to convert

    - Choose source and target units

    - Click "Convert" button

## Project Structure
unit-converter/
├── app.py                 # Main Flask application
├── converter.py           # Conversion logic
├── requirements.txt       # Dependencies
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Length converter
│   ├── weight.html        # Weight converter
│   ├── temperature.html   # Temperature converter
│   └── result.html        # Results page
└── static/
    └── styles.css         # CSS styles

## Conversion Formulas
### Temperature
- **Celsius to Fahrenheit:**
°F = (°C × 9/5) + 32

- **Fahrenheit to Celsius:**
°C = (°F - 32) × 5/9

- **Celsius to Kelvin:**
K = °C + 273.15

### Length
- **Metric conversions:**
Based on decimal scaling (1km = 1000m, 1m = 100cm, etc.)

- **Imperial conversions:**

    - 1 mile = 1760 yards

    - 1 yard = 3 feet

    - 1 foot = 12 inches

### Weight
- **Metric conversions**:
Based on decimal scaling (1t = 1000kg, 1kg = 1000g, etc.)

## Error Handling
The application includes robust error handling for:

- Non-numeric inputs

- Invalid unit combinations

- Edge cases in temperature conversions

Error messages are displayed clearly to help users correct their inputs.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or feedback, please contact:

Email: lynconlima00@gmail.com

GitHub: github.com/Lyncxxx
