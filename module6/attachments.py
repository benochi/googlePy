import os.path
attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
#Mimetype and subtype tell what kind of file you're using. 
import mimetypes
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)

#The EmailMessage type needs a MIME type and subtypes as separate strings, so let's split this up:
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
#image
print(mime_subtype)
#png