# Unit Converter

🔗 **Live Demo:** https://conversor-de-unidades-x3ff.onrender.com/

A Flask-based web application that converts between different units of measurement across three categories: **length**, **weight**, and **temperature**.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Supported Units](#supported-units)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Conversion Formulas](#conversion-formulas)
- [Error Handling](#error-handling)
- [License](#license)
- [Author](#author)

---

## Overview

Unit Converter is a web application built with **Flask** that allows users to convert values between different units of measurement. It currently supports conversions for **length**, **weight**, and **temperature**, featuring a clean interface and input validation.

---

## Features

- 📏 Convert between metric and imperial length units
- ⚖️ Convert between metric weight units
- 🌡️ Convert temperatures between Celsius, Fahrenheit and Kelvin
- ✅ Input validation with user-friendly error messages
- ⚡ Instant conversion results
- 📱 Responsive and easy-to-use interface

---

## Technologies

- Python
- Flask
- HTML5
- CSS3
- Jinja2

---

## Supported Units

### Length

| Unit | Description |
|------|-------------|
| km | Kilometer |
| m | Meter |
| dm | Decimeter |
| cm | Centimeter |
| mm | Millimeter |
| μm | Micrometer |
| nm | Nanometer |
| mi | Mile |
| yd | Yard |
| ft | Foot |
| in | Inch |

### Weight

| Unit | Description |
|------|-------------|
| t | Metric ton |
| kg | Kilogram |
| g | Gram |
| mg | Milligram |

### Temperature

| Unit | Description |
|------|-------------|
| °C | Celsius |
| °F | Fahrenheit |
| K | Kelvin |

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Lyncxxx/Conversor-de-unidades.git
cd Conversor-de-unidades
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

---

## Usage

1. Start the application:

```bash
python app.py
```

2. Open your browser and visit:

```
http://localhost:5000
```

3. Select:

- Conversion category
- Source unit
- Destination unit
- Value to convert

The result will be displayed instantly.

---

## Project Structure

```text
Conversor-de-unidades/
├── app.py
├── conversor.py
├── requirements.txt
├── Procfile
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── peso.html
│   ├── temperatura.html
│   └── resultado.html
└── static/
    └── style.css
```

---

## Conversion Formulas

### Temperature

- Celsius → Fahrenheit

```
°F = (°C × 9/5) + 32
```

- Fahrenheit → Celsius

```
°C = (°F − 32) × 5/9
```

- Celsius → Kelvin

```
K = °C + 273.15
```

### Length

Metric conversions are based on decimal scaling.

Examples:

- 1 km = 1000 m
- 1 m = 100 cm
- 1 cm = 10 mm

Imperial conversions include:

- 1 mile = 1760 yards
- 1 yard = 3 feet
- 1 foot = 12 inches

### Weight

Metric conversions are based on decimal scaling.

Examples:

- 1 t = 1000 kg
- 1 kg = 1000 g
- 1 g = 1000 mg

---

## Error Handling

The application validates user input and handles:

- Invalid numeric values
- Unsupported unit combinations
- Temperature conversion edge cases

Whenever an invalid value is entered, a clear error message is displayed to help the user correct the input.

---

## License

This project is licensed under the MIT License.

---

## Author

**Lyncon Lima**

GitHub: https://github.com/Lyncxxx