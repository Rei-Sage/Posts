import base64

from django.core.files.base import ContentFile


def base64_to_image_file(base64_string, filename='image'):
    _format = 'jpg'

    if 'data:' in base64_string:
        _format = base64_string.split(';')[0].split(':')[1].split('/')[1]

    if 'base64,' in base64_string:
        base64_string = base64_string.split('base64,')[1]

    # Decode the base64 string
    decoded_file = base64.b64decode(base64_string)

    # Create a ContentFile
    image_file = ContentFile(decoded_file, name=f'{filename}.{_format}')

    return image_file