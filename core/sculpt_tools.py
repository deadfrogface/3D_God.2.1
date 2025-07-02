import subprocess, json

def open_sculpt(attributes):
    data = {"attributes": attributes}
    with open("tmp_sculpt_input.json","w") as f:
        json.dump(data,f)
    subprocess.run(["blender", "--background", "blender_embed/sculpt_main.py", "--python-expr", f"print('Sculpt attributes {attributes}')"])