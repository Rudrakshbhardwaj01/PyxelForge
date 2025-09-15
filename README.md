# PyxelForge

PyxelForge is a Python project that transforms text prompts into AI-generated images using Mistral, and then converts those images into visually appealing ASCII art. Both the original image and the ASCII art output are saved, with the ASCII optimized for readability and aesthetics in terminals or text editors.

---

##  Folder Structure

```
PyxelForge/
├── imageGen/         # Contains code for generating AI images using Mistral
│   └── imageGen.py
├── ASCIIgen/         # Contains code for converting images to ASCII art
│   └── ASCIIgen.py
├── images/           # Generated AI images and ASCII art outputs will be saved here
├── main.py           # Main script to generate image and ASCII art together
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## Features

- **AI Image Generation**: Convert text prompts into AI-generated images with Mistral API.
- **ASCII Art Conversion**: Transform images into high-quality ASCII art.
- **Save Outputs**: Automatically saves both the generated image and ASCII art.
- **Modular & Easy to Use**: Clean Python scripts organized for clarity and extensibility.

---

##  Installation & Setup

### 1. Clone the Repository

```sh
git clone https://github.com/Rudrakshbhardwaj01/PyxelForge.git
cd PyxelForge
```

### 2. Install Python Dependencies

Required libraries:
- `Pillow` (`PIL`)
- `mistral-sdk` (Mistral Python SDK)
- Any additional dependencies listed in `requirements.txt`

Install them with:

```sh
pip install -r requirements.txt
```

### 3. Set Up Mistral API

- Sign up at [Mistral AI](https://mistral.ai/) to create your account.
- Generate your Mistral API key in the dashboard.

#### Add Your API Key

You can set your API key as an environment variable:

```sh
export MISTRAL_API_KEY="your_mistral_api_key_here"
```

Or, insert it directly in the code (not recommended for production).

---

## Usage

Run the main script to generate an image and ASCII art from a prompt:

```sh
python main.py --prompt "A futuristic city skyline at sunset"
```

**Outputs:**
- The generated image will be saved in the `images/` folder.
- The corresponding ASCII art will also be saved in `images/`.

**Optional Parameters:**
- Adjust the ASCII output width:
  ```sh
  python main.py --prompt "A cat with glasses" --width 80
  ```
- Customize output file names:
  ```sh
  python main.py --prompt "A mountain landscape" --image_name mountain.png --ascii_name mountain.txt
  ```

---

## 🖼️ Example Output

**ASCII Art Snippet:**

```
      . . . . : : : : : : : . . . .
    . : % @ # # @ % : . . . . . : .
  . : # @ @ @ @ @ # % : . . . . . .
  . % # @ # # # # @ # % : . . . . .
  . % # @ # . . # @ # % : . . . . .
    . % # . . . # # % : : . . . .
      . . . : % # % : : . . . . .
```

> *ASCII art is optimized for readability in terminals and text editors.*

---

##  Author

**Rudraksh Bhardwaj**  
- [GitHub Profile](https://github.com/Rudrakshbhardwaj01)
- For questions: [rudrakshbhardwaj01@gmail.com](mailto:rudrakshbhardwaj01@gmail.com)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Submit a pull request with a clear description.

Read the [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## 📬 Contact

For questions, suggestions, or feedback, open an issue or email [rudrakshbhardwaj01@gmail.com](mailto:rudrakshbhardwaj01@gmail.com).

---

Happy forging pixels into art! 🎨
