# Cipher64

A cryptic fusion of Caesar cipher and Base64 encoding, Cipher64 conceals names and sensitive data in layered shadows. Perfect for lightweight, enigmatic encryption.

## Overview
Cipher64 is a hybrid encryption system designed to securely obscure names or short strings. It combines a Caesar cipher (with a configurable shift) and Base64 encoding to create a simple yet effective encryption pipeline. Ideal for developers seeking a minimalistic approach to data obfuscation.

## Features
- **Caesar Cipher**: Shifts letters to mask the original text.
- **Base64 Encoding**: Adds a layer of encoding for enhanced obscurity.
- **Lightweight**: Easy to integrate and customize for small-scale projects.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/thehidesofheav/Cipher64.git
   ```
2. Run the Python script:
   ```bash
   python cipher64.py
   ```
3. Input a name (e.g., "Heav") to get an encrypted output (e.g., "S2hkeQ==").

## Example
```python
from cipher64 import encrypt_name
name = "Heav"
encrypted = encrypt_name(name, shift=3)
print(f"Encrypted: {encrypted}")  # Output: S2hkeQ==
```

## Requirements
- Python 3.x
- No external dependencies

## License
MIT License
