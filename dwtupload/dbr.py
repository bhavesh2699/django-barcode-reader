import os.path
import DynamsoftBarcodeReader

formats = {
    0x1FFL : "OneD",
    0x1L   : "CODE_39",
    0x2L : "CODE_128",
    0x4L   : "CODE_93",
    0x8L : "CODABAR",
    0x10L   : "ITF",
    0x20L : "EAN_13",
    0x40L   : "EAN_8",
    0x80L : "UPC_A",
    0x100L   : "UPC_E",
}

def initLicense(license):
    DynamsoftBarcodeReader.initLicense(license)

def decodeFile(fileName):
    if not os.path.isfile(fileName):
        print "It is not a valid file."
        return

    results = DynamsoftBarcodeReader.decodeFile(fileName)
    json = {}
    tmp = []
    i = 0

    # Convert results to JSON
    for result in results:
        key = formats[result[0]]
        value = result[1]
        tmp = [key, value]
        json[i] = tmp
        i += 1;

    return str(json)

# Test
if __name__ == "__main__":
    # barcode_image = input("Enter the barcode file: ")
    barcode_image = r"F:\git\Dynamsoft-Barcode-Reader\Images\AllSupportedBarcodeTypes.tif"
    results = decodeFile(barcode_image);
    print results
