# TIFF files have transparent backaground which original JPG format doesn't
# support. PNG would be a more suitable option, but the lab calls for JPEG.
rx_frmt = "JPEG"

# gather list of image files:
img_files = [f for f in listdir(src_dir) if f.startswith("ic_")]

# reprocess images:
for file in img_files:
    src_img = Image.open(src_dir + file)

    # rotate & resize image:
    new_img = src_img.rotate(rx_90dg).resize(rx_size)

    # NOTE: we need to convert to RGB here to avoid error:
    new_img = new_img.convert("RGB")

    # save new output file:
    new_img.save(new_dir + file, rx_frmt)
