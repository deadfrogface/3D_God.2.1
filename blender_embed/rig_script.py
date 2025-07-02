import bpy
arm = bpy.data.armatures.new("AutoRigArm")
obj = bpy.data.objects.new("Armature", arm)
bpy.context.collection.objects.link(obj)
bpy.context.view_layer.objects.active = obj
bpy.ops.object.mode_set(mode='EDIT')
# minimal stub