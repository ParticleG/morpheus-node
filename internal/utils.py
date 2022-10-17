def images2base64(images):
    from io import BytesIO
    from base64 import b64encode

    b64_images = []
    for _image in images:
        with BytesIO() as buffer:
            _image.save(buffer, format="PNG")
            b64_images.append(b64encode(buffer.getvalue()).decode("utf-8"))

    return b64_images
