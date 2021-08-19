import bpy

bl_info = {
    "name": "Toggle Debug All",
    "author": "gryldz",
    "version": (1, 0),
    "blender": (2, 83, 0),
    "location": "Scripting > Info > Toggle Debug All",
    "description": "Adds a button to toggle advanced debugging On and Off.",
    "warning": "",
    "doc_url": "",
    "tracker_url": "https://github.com/MehmetHY/BlenderToggleDebugAll",
    "category": "Development"
}

class ToggleDebugAll(bpy.types.Operator):
    bl_idname = "console.toggle_debug_all"
    bl_label = "Toggle Debug All"
    bl_options = {'REGISTER', 'UNDO'}
  
    def execute(self, context):
        bpy.app.debug_wm = not bpy.app.debug_wm
        return {'FINISHED'}


def draw_item(self, context):
    layout = self.layout
    layout.operator("console.toggle_debug_all")


def register():
    bpy.utils.register_class(ToggleDebugAll)
    bpy.types.INFO_HT_header.append(draw_item)


def unregister():
    bpy.utils.unregister_class(ToggleDebugAll)
    bpy.types.INFO_HT_header.remove(draw_item)


if __name__ == "__main__":
    register()
