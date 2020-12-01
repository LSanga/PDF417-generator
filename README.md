Very minimal python3 script to generate PDF417 barcode (format used for USA driving license) from a txt/csv file.
Output are png images fixed at chosen size with 16 columns. 
CSV has:

    -no first row
    -1 full entry per line
    -new line (\n) as separator
    
Other options that can be specified for the barcode generation here: https://github.com/bwipp/postscriptbarcode/wiki/Options-Reference    

Is it possible to change size and format of the image (from Pillow library):
To specify width/height you need to modify the source with the correct value. You can either choose inches or pixels.

Image.convert modes (size in pixels):
https://pillow.readthedocs.io/en/3.1.x/handbook/concepts.html#concept-modes

Image.save formats:
https://pillow.readthedocs.io/en/3.1.x/handbook/image-file-formats.html

Based on the following library: https://pypi.org/project/treepoem/