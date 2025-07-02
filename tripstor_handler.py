import subprocess

def generate_3d_from_image(image_path, outpath="exports/triposr_output.obj"):
    print("TripoSR läuft auf", image_path)
    subprocess.run(["echo", "TriposR stubing..."])
    shutil.copy(image_path, outpath)
    return outpath