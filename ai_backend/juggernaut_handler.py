import shutil

def generate_reference_image(prompt, outpath="exports/juggernaut_ref.png"):
    print("Juggernaut-Stub erzeugt Bild")
    with open(outpath, "wb") as f:
        f.write(b"\x89PNG\r\n")
    return outpath