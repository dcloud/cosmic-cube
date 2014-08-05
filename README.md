# cosmic-cube

PDF image analysis and selective text extraction using tesseract

## Requirements

You can use the Vagrantfile in this repo to configure an Ubuntu box for you. Requires [Vagrant](http://www.vagrantup.com)+[Ansible](http://www.ansible.com).

Or, you could install each of these yourself:

- [tesseract](https://code.google.com/p/tesseract-ocr/) - OCR
- [opencv](http://opencv.org/) - Computer vision (Feature detection)
- [poppler](http://poppler.freedesktop.org/) - Get info about pdfs, convert to image files
- [python-tesseract](https://code.google.com/p/python-tesseract/).

## Notes

When importing opencv in python (`import cv2`) on the Vagrant box, you will probably get the warning `libdc1394 error: Failed to initialize libdc1394`. Relax! It's just looking for a firewire camera controller. You [don't need it](http://stackoverflow.com/questions/12689304/ctypes-error-libdc1394-error-failed-to-initialize-) for opencv to work properly.