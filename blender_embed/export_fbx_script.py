import bpy
bpy.ops.export_scene.fbx(filepath="exports/final_character.fbx", embed_textures=True)
print("FBX tatsächlich exportiert.")