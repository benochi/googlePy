import os.path
attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
#Mimetype and subtype tell what kind of file you're using. 
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)