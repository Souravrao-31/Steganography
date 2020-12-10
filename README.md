# LSB Steganography

⭐ [Project Report](assets/2-channel-lsb-steganography-project-report.pdf) | 📓 [Method Explanation](notebook/method-explanation.ipynb)

## 📖 Overview
1. [Introduction](#introduction)
1. [Running It On Your Machine](#running-it-on-your-machine)
1. [Bibliography](#bibliography)

## Introduction
Steganography is the art of hiding messages so that they can only be read or interpreted by the receiving
party for whom it was meant for. It is different from Cryptography, as Cryptography relies on encrypting
(changing) the data using an encryption function such that only the intended receiving party can decrypt
it and see the plaintext message.

Steganography on the other hand relies on the principle of security by obscurity, hiding the message in 
plain sight. There are many different methods of hiding data inside Images, one of the simplest and
very efficient ways to do that is by using the LSB (Least Significant Bit) Steganography technique.

In this technique we store the data bits in each of the least significant bits of the Red, Blue and 
green channel. In this project I implement the LSB technique and further enhance it by adding an 
additional Blue channel layer for pixel storage.

## Running it on Your Machine
Clone this repository and install all dependencies

```bash
https://github.com/Souravrao-31/Steganography.git
cd steganography
pip install -r requirements.txt
```

Start the server to test LSB Steganography wih your own test images

```bash
cd src 
waitress-serve app:app
```

This will start a server on [localhost:8080](http://localhost:8080)

## Bibliography
1. [Hiding Data in Images by Simple LSB Substitution ~Elsevier](https://www.sciencedirect.com/science/article/abs/pii/S003132030300284X)
1. [Image Steganography - Least Significant Bit with Multiple Progressions ~ Springer](https://link.springer.com/chapter/10.1007/978-3-319-12012-6_12)
1. [A Methodology fo Using Data Hiding using Images ~IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/727007)
1. [Forouzan A. - Cryptography and Network Security](https://dl.acm.org/doi/book/10.5555/1209579)
1. [Digital image steganography Survey and analysis of current methods Elsevier](https://www.sciencedirect.com/science/article/abs/pii/S0165168409003648)
