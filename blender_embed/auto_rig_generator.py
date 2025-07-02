import subprocess

def rig_character():
    subprocess.run(["blender", "--background", "--python", "blender_embed/rig_script.py"])
    print("Auto-Rig wurde ausgeführt (Stub)")