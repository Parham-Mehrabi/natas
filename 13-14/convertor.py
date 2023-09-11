"""
    this module add jpeg signature to a file
"""
not_jpeg_file = None
not_jpeg_file = not_jpeg_file if not_jpeg_file else './upload.php' 
# either get the file path from user or use upload.php in the current directory

with open(not_jpeg_file, 'rb+') as f:
    hex_data = f.read().hex()

JPG_SIGNATURE = 'ffd8ffee'

modified_hex_data =  JPG_SIGNATURE + hex_data[8::]

with open('./modified_file.php', 'wb') as modified_file:
    modified_file.write(bytes.fromhex(modified_hex_data))


MESSAGE =   """
              created a file called modified_file.php similar to previous file but with modified signature \n \r
              now if you check the file with tools like "file command" "exiftool" and other stuff they will see it as jpg file  
            """
print(MESSAGE)
