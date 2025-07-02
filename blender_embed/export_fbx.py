import subprocess

def export_fbx():
    subprocess.run(["blender", "--background", "--python", "blender_embed/export_fbx_script.py"])
    print("FBX Export ausgeführt (Stub)")