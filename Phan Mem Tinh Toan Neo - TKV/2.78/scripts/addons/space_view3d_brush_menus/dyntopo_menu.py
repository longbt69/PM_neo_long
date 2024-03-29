from bpy.props import *
from .Utils.core import *

class DynTopoMenu(bpy.types.Menu):
    bl_label = "Dyntopo"
    bl_idname = "VIEW3D_MT_sv3_dyntopo"

    @classmethod
    def poll(self, context):
        if get_mode() == sculpt:
            return True
        else:
            return False

    def draw(self, context):
        menu = Menu(self)

        if context.object.use_dynamic_topology_sculpting:
            menu.add_item().operator("sculpt.dynamic_topology_toggle", "Disable Dynamic Topology")

            menu.add_item().separator()

            menu.add_item().menu(DynDetailMenu.bl_idname)
            menu.add_item().menu(DetailMethodMenu.bl_idname)

            menu.add_item().separator()

            menu.add_item().operator("sculpt.optimize")
            if bpy.context.tool_settings.sculpt.detail_type_method == 'CONSTANT':
                menu.add_item().operator("sculpt.detail_flood_fill")

            menu.add_item().menu(SymmetrizeMenu.bl_idname)
            menu.add_item().prop(context.tool_settings.sculpt, "use_smooth_shading", toggle=True)

        else:
            menu.add_item()
            menu.current_item.operator_context = 'INVOKE_DEFAULT'
            menu.current_item.operator("sculpt.dynamic_topology_toggle", "Enable Dynamic Topology")


class DynDetailMenu(bpy.types.Menu):
    bl_label = "Detail Size"
    bl_idname = "VIEW3D_MT_sv3_dyn_detail"

    def init(self):
        settings = [["40", 40], ["30", 30], ["20", 20],
                    ["10", 10], ["5", 5], ["1", 1]]

        if bpy.context.tool_settings.sculpt.detail_type_method == 'RELATIVE':
            datapath = "tool_settings.sculpt.detail_size"
            slider_setting = "detail_size"

        else:
            datapath = "tool_settings.sculpt.constant_detail"
            slider_setting = "constant_detail"

        return settings, datapath, slider_setting

    def draw(self, context):
        settings, datapath, slider_setting = self.init()
        menu = Menu(self)

        # add the top slider
        menu.add_item().prop(context.tool_settings.sculpt, slider_setting, slider=True)
        menu.add_item().separator()

        # add the rest of the menu items
        for i in range(len(settings)):
            menuprop(menu.add_item(), settings[i][0], settings[i][1], datapath,
                     icon='RADIOBUT_OFF', disable=True,
                     disable_icon='RADIOBUT_ON')


class DetailMethodMenu(bpy.types.Menu):
    bl_label = "Detail Method"
    bl_idname = "VIEW3D_MT_sv3_detail_method_menu"

    def draw(self, context):
        menu = Menu(self)
        refine_path = "tool_settings.sculpt.detail_refine_method"
        type_path = "tool_settings.sculpt.detail_type_method"

        refine_items = [["Subdivide Edges", 'SUBDIVIDE'],
                        ["Collapse Edges", 'COLLAPSE'],
                        ["Subdivide Collapse", 'SUBDIVIDE_COLLAPSE']]

        type_items = [["Relative Detail", 'RELATIVE'],
                      ["Constant Detail", 'CONSTANT']]

        menu.add_item().label("Refine")
        menu.add_item().separator()

        # add the refine menu items
        for item in refine_items:
            menuprop(menu.add_item(), item[0], item[1], refine_path, disable=True,
                     icon='RADIOBUT_OFF', disable_icon='RADIOBUT_ON')

        menu.add_item().label("")

        menu.add_item().label("Type")
        menu.add_item().separator()

        # add the type menu items
        for item in type_items:
            menuprop(menu.add_item(), item[0], item[1], type_path, disable=True,
                     icon='RADIOBUT_OFF', disable_icon='RADIOBUT_ON')


class SymmetrizeMenu(bpy.types.Menu):
    bl_label = "Symmetrize"
    bl_idname = "VIEW3D_MT_sv3_symmetrize_menu"

    def draw(self, context):
        menu = Menu(self)
        path = "tool_settings.sculpt.symmetrize_direction"

        # add the the symmetrize operator to the menu
        menu.add_item().operator("sculpt.symmetrize")
        menu.add_item().separator()

        # add the rest of the menu items
        for item in context.tool_settings.sculpt.bl_rna.properties['symmetrize_direction'].enum_items:
            menuprop(menu.add_item(), item.name, item.identifier, path, disable=True, 
                     icon='RADIOBUT_OFF', disable_icon='RADIOBUT_ON')

