import os
from blender_embed.sculpt_tools import SculptTools
from blender_embed.auto_rig_generator import rig_character
from blender_embed.export_fbx import export_fbx

class CharacterSystem:
    def __init__(self):
        self.attributes = {}
        self.clothes = []
        self.nsfw = True

    def bind_viewport(self, viewport):
        self.viewport = viewport

    def set_body_attribute(self, key, value):
        self.attributes[key] = value

    def open_sculpt_in_blender(self):
        SculptTools.open_sculpt(self.attributes)

    def toggle_nsfw(self, state):
        self.nsfw = state

    def add_clothing(self, name):
        self.clothes.append(name)
        return name

    def auto_rig_character(self):
        rig_character()

    def export_character(self):
        export_fbx()
        if hasattr(self,"viewport"):
            self.viewport.display_model("exports/final_character.fbx")