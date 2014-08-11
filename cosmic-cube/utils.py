import subprocess
import os.path

class PDFConverter(object):
    """Converts a PDF to an image by calling poppler's pdftoppm in a subprocess"""
    def __init__(self, filepath, outputprefix=None, resolution=300, output_tiff=False):
        super(PDFConverter, self).__init__()
        self.filepath = os.path.abspath(filepath)
        self.outputprefix = outputprefix
        self.resolution = resolution
        self.output_tiff = output_tiff
        if self.outputprefix is None:
            pathparts = os.path.split(self.filepath)
            root, ext = os.path.splitext(pathparts[1])
            self.outputprefix = os.path.join(pathparts[0], root)

    def convert(self):
        sub_args = ['pdftoppm', '-r', str(self.resolution)]
        if self.output_tiff:
            sub_args.append('-tiff')
        sub_args.extend([self.filepath, self.outputprefix])
        result = subprocess.call(sub_args)
        if result == 0:
            print('Converted sucessfully')
        else:
            print("pdftoppm didn't complete successfully")