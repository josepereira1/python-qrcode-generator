## Setup & run:

Install the requirement modules:
```cmd
  pip3 install --upgrade --force-reinstall --no-cache-dir -r requirements.txt
```

Run the service:

```cmd
  sudo python3 qrcode-generator.py
```
Note: Some of these commands are in makefile.

## QR code generation:

There are two options to QR code generation.

Firt option (**recommended option**):
- Open the **qrcode-generator.py** file and set the **QRCODE_TEXT** with content of your QR code. After, access via browser or other http request tool to the http://localhost/qrcode.

Second option (use this just for simple text):
- Access via browser or other http request tool to the http://localhost/qrcode/<qrcode_text> and specify your QR code text in URL path.
