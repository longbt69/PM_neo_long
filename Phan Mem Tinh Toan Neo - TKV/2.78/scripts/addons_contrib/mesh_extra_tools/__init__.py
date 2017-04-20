# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Contributed to by:
# meta-androcto,  Hidesato Ikeya, zmj100, luxuy_BlenderCN, TrumanBlending, PKHG, #
# Oscurart, Greg, Stanislav Blinov, komi3D, BlenderLab, Paul Marshall (brikbot), #
# metalliandy, macouno, CoDEmanX, dustractor, Liero, lijenstina #

bl_info = {
    "name": "Edit Tools 2",
    "author": "meta-androcto",
    "version": (0, 3, 1),
    "blender": (2, 77, 0),
    "location": "View3D > Toolshelf > Tools and Specials (W-key)",
    "description": "Extra mesh edit tools - modifying meshes and selection",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://developer.blender.org/maniphest/task/edit/form/2/",
    "category": "Mesh"}


# Import From Files
if "bpy" in locals():
    import importlib
    importlib.reload(face_inset_fillet)
    importlib.reload(mesh_filletplus)
    importlib.reload(mesh_vertex_chamfer)
    importlib.reload(mesh_mextrude_plus)
    importlib.reload(mesh_offset_edges)
    importlib.reload(pkhg_faces)
    importlib.reload(mesh_edge_roundifier)
    importlib.reload(mesh_cut_faces)
    importlib.reload(split_solidify)
    importlib.reload(mesh_to_wall)
    importlib.reload(mesh_edges_length)
    importlib.reload(random_vertices)
    importlib.reload(mesh_fastloop)
    importlib.reload(mesh_edgetools)
    importlib.reload(mesh_pen_tool)
    importlib.reload(vfe_specials)
    importlib.reload(mesh_help)

    importlib.reload(mesh_select_by_direction)
    importlib.reload(mesh_select_by_edge_length)
    importlib.reload(mesh_select_by_pi)
    importlib.reload(mesh_select_by_type)
    importlib.reload(mesh_select_connected_faces)
    importlib.reload(mesh_index_select)
    importlib.reload(mesh_selection_topokit)
    importlib.reload(mesh_info_select)

else:
    from . import face_inset_fillet
    from . import mesh_filletplus
    from . import mesh_vertex_chamfer
    from . import mesh_mextrude_plus
    from . import mesh_offset_edges
    from . import pkhg_faces
    from . import mesh_edge_roundifier
    from . import mesh_cut_faces
    from . import split_solidify
    from . import mesh_to_wall
    from . import mesh_edges_length
    from . import random_vertices
    from . import mesh_fastloop
    from . import mesh_edgetools
    from . import mesh_pen_tool
    from . import vfe_specials
    from . import mesh_help

    from .mesh_select_tools import mesh_select_by_direction
    from .mesh_select_tools import mesh_select_by_edge_length
    from .mesh_select_tools import mesh_select_by_pi
    from .mesh_select_tools import mesh_select_by_type
    from .mesh_select_tools import mesh_select_connected_faces
    from .mesh_select_tools import mesh_index_select
    from .mesh_select_tools import mesh_selection_topokit
    from .mesh_select_tools import mesh_info_select

import bpy
from bpy.types import (
        Menu,
        Panel,
        PropertyGroup,
        AddonPreferences,
        )
from bpy.props import (
        BoolProperty,
        IntVectorProperty,
        PointerProperty,
        )


# ------ MENUS ------ #

# Define the "Extras" menu
class VIEW3D_MT_edit_mesh_extras(Menu):
    bl_idname = "VIEW3D_MT_edit_mesh_extras"
    bl_label = "Edit Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'
        mode = context.tool_settings.mesh_select_mode

        if mode[0]:
            split = layout.split()
            col = split.column()

            col.label(text="Vertex", icon="VERTEXSEL")
            col.separator()

            col.operator("mesh.vertex_chamfer", text="Vertex Chamfer")
            col.operator("mesh.random_vertices", text="Random Vertices")

            col = split.column()
            col.label(text="Utilities", icon="SCRIPTWIN")
            col.separator()

            col.operator("object_ot.fastloop", text="Fast loop")
            col.operator("mesh.flip_normals", text="Normals Flip")
            col.operator("mesh.remove_doubles", text="Remove Doubles")
            col.operator("mesh.subdivide", text="Subdivide")
            col.operator("mesh.dissolve_limited", text="Dissolve Limited")

        elif mode[1]:
            split = layout.split()
            col = split.column()
            col.label(text="Edge", icon="EDGESEL")
            col.separator()

            col.operator("mesh.fillet_plus", text="Edge Fillet Plus")
            col.operator("mesh.offset_edges", text="Offset Edges")
            col.operator("mesh.edge_roundifier", text="Edge Roundify")
            col.operator("object.mesh_edge_length_set", text="Set Edge Length")
            col.operator("bpt.mesh_to_wall", text="Edge(s) to Wall")

            col = split.column()
            col.label(text="Utilities", icon="SCRIPTWIN")
            col.separator()

            col.operator("object_ot.fastloop", text="Fast loop")
            col.operator("mesh.flip_normals", text="Normals Flip")
            col.operator("mesh.remove_doubles", text="Remove Doubles")

            col.operator("mesh.subdivide", text="Subdivide")
            col.operator("mesh.dissolve_limited", text="Dissolve Limited")

        elif mode[2]:
            split = layout.split()
            col = split.column()
            col.label(text="Face", icon="FACESEL")
            col.separator()

            col.operator("object.mextrude", text="Multi Extrude")
            col.operator("mesh.face_inset_fillet", text="Face Inset Fillet")
            col.operator("mesh.add_faces_to_object", text="PKHG Faces")
            col.operator("mesh.ext_cut_faces", text="Cut Faces")
            col.operator("mesh.split_solidify", text="Split Solidify")

            col = split.column()
            col.label(text="Utilities", icon="SCRIPTWIN")
            col.separator()

            col.operator("object_ot.fastloop", text="Fast loop")
            col.operator("mesh.flip_normals", text="Normals Flip")
            col.operator("mesh.remove_doubles", text="Remove Doubles")
            col.operator("mesh.subdivide", text="Subdivide")
            col.operator("mesh.dissolve_limited", text="Dissolve Limited")


class EditToolsPanel(Panel):
    bl_label = "Mesh Edit Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "mesh_edit"
    bl_category = "Tools"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        scene = context.scene
        VERTDROP = scene.mesh_extra_tools.UTVertDrop
        EDGEDROP = scene.mesh_extra_tools.UTEdgeDrop
        FACEDROP = scene.mesh_extra_tools.UTFaceDrop
        UTILSDROP = scene.mesh_extra_tools.UTUtilsDrop

        # Change icons depending on the bool state (complient with the rest of the UI)
        icon_active_1 = "TRIA_RIGHT" if not VERTDROP else "TRIA_DOWN"
        icon_active_2 = "TRIA_RIGHT" if not EDGEDROP else "TRIA_DOWN"
        icon_active_3 = "TRIA_RIGHT" if not FACEDROP else "TRIA_DOWN"
        icon_active_4 = "TRIA_RIGHT" if not UTILSDROP else "TRIA_DOWN"

        layout = self.layout

        # Vert options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene.mesh_extra_tools, "UTVertDrop", icon=icon_active_1)
        if not VERTDROP:
            row.menu("mesh.vert_select_tools", icon="RESTRICT_SELECT_OFF", text="")
            row.menu("VIEW3D_MT_Select_Vert", icon="VERTEXSEL", text="")
        else:
            layout = self.layout

            row = layout.row()
            row.label(text="Vertex Tools:", icon="VERTEXSEL")

            row = layout.split(0.8, align=True)
            row.operator("mesh.vertex_chamfer", text="Chamfer")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "mesh_vertex_chamfer"

            row = layout.split(0.8, align=True)
            row.operator("mesh.random_vertices", text="Random Vertices")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "random_vertices"

        # Edge options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene.mesh_extra_tools, "UTEdgeDrop", icon=icon_active_2)

        if not EDGEDROP:
            row.menu("mesh.edge_select_tools", icon="RESTRICT_SELECT_OFF", text="")
            row.menu("VIEW3D_MT_Select_Edge", icon="EDGESEL", text="")
        else:
            layout = self.layout

            row = layout.row()
            row.label(text="Edge Tools:", icon="EDGESEL")
            row.menu("VIEW3D_MT_edit_mesh_edgetools", icon="GRID")

            row = layout.split(0.8, align=True)
            row.operator("mesh.fillet_plus", text="Fillet plus")

            prop = row.operator("mesh.extra_tools_help", icon="LAYER_USED")
            prop.help_ids = "mesh_filletplus"
            prop.popup_size = 400

            row = layout.split(0.8, align=True)
            row.operator("mesh.offset_edges", text="Offset Edges")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "mesh_offset_edges"

            row = layout.split(0.8, align=True)
            row.operator("mesh.edge_roundifier", text="Roundify")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "mesh_edge_roundifier"

            row = layout.split(0.8, align=True)
            row.operator("object.mesh_edge_length_set", text="Set Edge Length")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "mesh_edges_length"

            row = layout.split(0.8, align=True)
            row.operator("bpt.mesh_to_wall", text="Edge(s) to Wall")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "mesh_to_wall"

        # Face options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene.mesh_extra_tools, "UTFaceDrop", icon=icon_active_3)

        if not FACEDROP:
            row.menu("mesh.face_select_tools", icon="RESTRICT_SELECT_OFF", text="")
            row.menu("VIEW3D_MT_Select_Face", icon="FACESEL", text="")
        else:
            layout = self.layout

            row = layout.row()
            row.label(text="Face Tools:", icon="FACESEL")

            row = layout.split(0.8, align=True)
            row.operator("object.mextrude", text="Multi Extrude")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "mesh_mextrude_plus"

            row = layout.split(0.8, align=True)
            row.operator("mesh.face_inset_fillet", text="Inset Fillet")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "face_inset_fillet"

            row = layout.split(0.8, align=True)
            row.operator("mesh.ext_cut_faces", text="Cut Faces")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "mesh_cut_faces"

            row = layout.split(0.8, align=True)
            row.operator("mesh.split_solidify", text="Split Solidify")
            row.operator("mesh.extra_tools_help",
                        icon="LAYER_USED").help_ids = "split_solidify"

        # Utils options
        box1 = self.layout.box()
        col = box1.column(align=True)
        row = col.row(align=True)
        row.prop(scene.mesh_extra_tools, "UTUtilsDrop", icon=icon_active_4)

        if not UTILSDROP:
            row.menu("mesh.utils specials", icon="SOLO_OFF", text="")
            row.menu("VIEW3D_MT_Edit_MultiMET", icon="LOOPSEL", text="")
        else:
            layout = self.layout

            row = layout.row()
            row.label(text="Utilities:")

            row = layout.row()
            row = layout.split(0.8, align=True)
            row.operator("object_ot.fastloop", text="Fast Loop")

            prop = row.operator("mesh.extra_tools_help", icon="LAYER_USED")
            prop.help_ids = "mesh_fastloop"
            prop.popup_size = 400

            row = layout.row()
            row.operator("mesh.flip_normals", text="Normals Flip")

            row = layout.row()
            row.operator("mesh.remove_doubles", text="Remove Doubles")

            row = layout.row()
            row.operator("mesh.subdivide", text="Subdivide")

            row = layout.row()
            row.operator("mesh.dissolve_limited", text="Dissolve Limited")

            row = layout.row(align=True)
            row.operator("mesh.select_vert_edge_face_index",
                          icon="VERTEXSEL", text="Vert Index").select_type = 'VERT'
            row.operator("mesh.select_vert_edge_face_index",
                          icon="EDGESEL", text="Edge Index").select_type = 'EDGE'
            row.operator("mesh.select_vert_edge_face_index",
                          icon="FACESEL", text="Face Index").select_type = 'FACE'


# ********** Edit Multiselect **********
class VIEW3D_MT_Edit_MultiMET(Menu):
    bl_label = "Multi Select"
    bl_description = "Multi Select Modes"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value",
                               text="Vertex Select",
                               icon='VERTEXSEL')
        prop.value = "(True, False, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Edge Select",
                               icon='EDGESEL')
        prop.value = "(False, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Face Select",
                               icon='FACESEL')
        prop.value = "(False, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        layout.separator()

        prop = layout.operator("wm.context_set_value",
                               text="Vertex and Edge Select",
                               icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex and Face Select",
                               icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Edge and Face Select",
                               icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex, Edge and Face Select",
                               icon='SNAP_VOLUME')
        prop.value = "(True, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"


# Select Tools
class VIEW3D_MT_Select_Vert(Menu):
    bl_label = "Select Vert"
    bl_description = "Vertex Selection Modes"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value",
                               text="Vertex Select",
                               icon='VERTEXSEL')
        prop.value = "(True, False, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex and Edge Select",
                               icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex and Face Select",
                               icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"


class VIEW3D_MT_Select_Edge(Menu):
    bl_label = "Select Edge"
    bl_description = "Edge Selection Modes"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value",
                               text="Edge Select",
                               icon='EDGESEL')
        prop.value = "(False, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex and Edge Select",
                               icon='EDITMODE_HLT')
        prop.value = "(True, True, False)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Edge and Face Select",
                               icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"


class VIEW3D_MT_Select_Face(Menu):
    bl_label = "Select Face"
    bl_description = "Face Selection Modes"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        prop = layout.operator("wm.context_set_value",
                               text="Face Select",
                               icon='FACESEL')
        prop.value = "(False, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Vertex and Face Select",
                               icon='ORTHO')
        prop.value = "(True, False, True)"
        prop.data_path = "tool_settings.mesh_select_mode"

        prop = layout.operator("wm.context_set_value",
                               text="Edge and Face Select",
                               icon='SNAP_FACE')
        prop.value = "(False, True, True)"
        prop.data_path = "tool_settings.mesh_select_mode"


class VIEW3D_MT_selectface_edit_mesh_add(Menu):
    bl_label = "Select by Face"
    bl_idname = "mesh.face_select_tools"
    bl_description = "Face Selection Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label(text="Face Selection Tools", icon="RESTRICT_SELECT_OFF")
        layout.separator()

        layout.operator("mesh.select_all").action = 'TOGGLE'
        layout.operator("mesh.select_all", text="Inverse").action = 'INVERT'
        layout.operator("mesh.ext_deselect_boundary", text="Deselect Boundary")
        layout.separator()

        layout.operator("data.facetype_select", text="Triangles").face_type = "3"
        layout.operator("data.facetype_select", text="Quads").face_type = "4"
        layout.operator("data.facetype_select", text="Ngons").face_type = "5"
        layout.separator()

        layout.operator("mesh.select_vert_edge_face_index",
                        text="By Face Index").select_type = 'FACE'
        layout.operator("mesh.select_by_direction", text="By Direction")
        layout.operator("mesh.select_by_pi", text="By Pi or e")
        layout.operator("mesh.select_connected_faces", text="By Connected Faces")
        layout.operator("mesh.conway", text="By Conway's game of life")
        layout.separator()

        layout.operator("mesh.e2e_efe", text="Neighbors by Face")
        layout.operator("mesh.f2f_fvnef", text="Neighbors by Vert not Edge")


class VIEW3D_MT_selectedge_edit_mesh_add(Menu):
    bl_label = "Select by Edge"
    bl_idname = "mesh.edge_select_tools"
    bl_description = "Edge Selection Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label(text="Edge Selection Tools", icon="RESTRICT_SELECT_OFF")
        layout.separator()

        layout.operator("mesh.select_all").action = 'TOGGLE'
        layout.operator("mesh.select_all", text="Inverse").action = 'INVERT'
        layout.separator()

        layout.operator("mesh.select_vert_edge_face_index",
                        text="By Edge Index").select_type = 'EDGE'
        layout.operator("mesh.select_by_direction", text="By Direction")
        layout.operator("mesh.select_by_pi", text="By Pi or e")
        layout.operator("mesh.select_by_edge_length", text="By Edge Length")
        layout.separator()

        layout.operator("mesh.e2e_eve", text="Neighbors by Vertex")
        layout.operator("mesh.e2e_evfe", text="Neighbors by Vertex and Face")
        layout.operator("mesh.e2e_efnve", text="Lateral Neighbors")
        layout.operator("mesh.e2e_evnfe", text="Longitudinal Edges")


class VIEW3D_MT_selectvert_edit_mesh_add(Menu):
    bl_label = "Select by Vert"
    bl_idname = "mesh.vert_select_tools"
    bl_description = "Vertex Selection Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label(text="Vertex Selection Tools", icon="RESTRICT_SELECT_OFF")
        layout.separator()

        layout.operator("mesh.select_all").action = 'TOGGLE'
        layout.operator("mesh.select_all", text="Inverse").action = 'INVERT'
        layout.separator()

        layout.operator("mesh.select_vert_edge_face_index",
                        text="By Vert Index").select_type = 'VERT'
        layout.operator("mesh.select_by_direction", text="By Direction")
        layout.operator("mesh.select_by_pi", text="By Pi or e")
        layout.separator()

        layout.operator("mesh.v2v_by_edge", text="Neighbors by Edge")
        layout.operator("mesh.e2e_eve", text="Neighbors by Vertex")
        layout.operator("mesh.e2e_efe", text="Neighbors by Face")
        layout.operator("mesh.v2v_facewise", text="Neighbors by Face - Edge")


class VIEW3D_MT_utils_specials(Menu):
    bl_label = "Specials Menu"
    bl_idname = "mesh.utils specials"
    bl_description = "Utils Quick Specials"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.label(text="Fast Specials")
        layout.separator()

        layout.menu("VIEW3D_MT_edit_mesh_clean")
        layout.separator()

        layout.operator("mesh.subdivide", text="Subdivide").smoothness = 0.0
        layout.operator("mesh.merge", text="Merge...")
        layout.operator("mesh.remove_doubles")
        layout.operator("mesh.inset")
        layout.operator("mesh.bevel", text="Bevel")
        layout.operator("mesh.bridge_edge_loops")
        layout.separator()

        layout.operator("mesh.normals_make_consistent",
                        text="Recalculate Outside").inside = False
        layout.operator("mesh.normals_make_consistent",
                        text="Recalculate Inside").inside = True
        layout.operator("mesh.flip_normals")


# Define the "Extras" Menu append
class VIEW3D_MT_edit_mesh_all(Menu):
    bl_idname = "VIEW3D_MT_edit_mesh_all"
    bl_label = "Mesh Edit Tools"

    def draw(self, context):
        layout = self.layout

        layout.menu("VIEW3D_MT_edit_mesh_extras")
        layout.menu("VIEW3D_MT_edit_mesh_edgetools")


def menu_func(self, context):
    self.layout.menu("VIEW3D_MT_edit_mesh_all")


# Define "Select" Menu append
def menu_select(self, context):
    if context.tool_settings.mesh_select_mode[2]:
        self.layout.menu("mesh.face_select_tools", icon="FACESEL")
    if context.tool_settings.mesh_select_mode[1]:
        self.layout.menu("mesh.edge_select_tools", icon="EDGESEL")
    if context.tool_settings.mesh_select_mode[0]:
        self.layout.menu("mesh.vert_select_tools", icon="VERTEXSEL")


# Scene Properties
class MeshExtraToolsSceneProps(PropertyGroup):
    UTVertDrop = BoolProperty(
        name="Vertex",
        default=False,
        description="Show/Hide Vertex Tools"
        )
    UTEdgeDrop = BoolProperty(
        name="Edge",
        default=False,
        description="Show/Hide Edge Tools"
        )
    UTFaceDrop = BoolProperty(
        name="Face",
        default=False,
        description="Show/Hide Face Tools"
        )
    UTUtilsDrop = BoolProperty(
        name="Utils",
        default=False,
        description="Show/Hide Miscellaneous Utils"
        )


# Add-on Preferences
class mesh_extra_tools_pref(AddonPreferences):
    bl_idname = __name__

    show_info = BoolProperty(
            name="Info",
            default=False,
            description="Some general information about the add-on",
            )
    show_shortcuts = BoolProperty(
            name="Hot Keys",
            default=False,
            description="List of the shortcuts used for the included various tools",
            )

    def draw(self, context):
        layout = self.layout
        box = layout.box()

        box.prop(self, "show_info", icon="INFO")
        if self.show_info:
            box.label(text="Collection of various extra Mesh Edit Functions",
                      icon="LAYER_ACTIVE")
            box.label("The majority of the tools can be found in"
                      "Mesh Edit Mode Toolshelf or W key Specials Menu",
                      icon="LAYER_USED")
            box.label("The Pen tool is a separate Panel in the Toolshelf",
                      icon="LAYER_USED")
            box.label("The Face Extrude tool is only available in Object Mode "
                      "as a separate panel in the Toolshelf",
                      icon="LAYER_USED")
            box.label("Face Info / Select is a separate Panel located in Properties > Data Editor",
                      icon="LAYER_USED")

        box.prop(self, "show_shortcuts", icon="KEYINGSET")
        if self.show_shortcuts:
            col = box.column()
            col.label(text="Double Right Click in Edit mode in the 3D Viewport",
                      icon="LAYER_ACTIVE")
            col.label("Used for quick access to the Vertex, Edge and Face context menus",
                      icon="LAYER_USED")
            col.separator()
            col.label(text="W-key in Edit Mode in the 3D Viewport",
                      icon="LAYER_ACTIVE")
            col.label("Tools are grouped into menus prepended to the Specials Menu",
                      icon="LAYER_USED")
            col.separator()
            col.label(text="Ctrl+D in Edit Mode in the 3D Viewport",
                      icon="LAYER_ACTIVE")
            col.label("Used by the Pen Tool to start drawing. When activated:",
                      icon="LAYER_USED")
            col.label("Shift + Mouse Move is used to draw along the X axis",
                      icon="LAYER_USED")
            col.label("Alt + Mouse Move is used to draw along the Y axis",
                      icon="LAYER_USED")
            col.separator()
            col.label(text="Note: when using Fast Loop operator, press Esc twice to finish",
                      icon="LAYER_ACTIVE")


def register():
    mesh_pen_tool.register()
    vfe_specials.register()
    bpy.utils.register_module(__name__)

    # Register Scene Properties
    bpy.types.Scene.mesh_extra_tools = PointerProperty(
                                            type=MeshExtraToolsSceneProps
                                            )
    # Used in mesh_selection_topokit to store cache selection data
    bpy.types.Object.tkkey = IntVectorProperty(size=4)

    # Add "Extras" menu to the "W-key Specials" menu
    bpy.types.VIEW3D_MT_edit_mesh_specials.prepend(menu_func)
    bpy.types.VIEW3D_MT_select_edit_mesh.prepend(menu_select)

    try:
        bpy.types.VIEW3D_MT_Select_Edit_Mesh.prepend(menu_select)
    except:
        pass


def unregister():
    mesh_pen_tool.unregister()
    vfe_specials.unregister()

    del bpy.types.Scene.mesh_extra_tools
    del bpy.types.Object.tkkey

    bpy.utils.unregister_module(__name__)

    # Remove "Extras" menu from the "" menu.
    bpy.types.VIEW3D_MT_edit_mesh_specials.remove(menu_func)
    bpy.types.VIEW3D_MT_select_edit_mesh.remove(menu_select)

    try:
        bpy.types.VIEW3D_MT_Select_Edit_Mesh.remove(menu_select)
    except:
        pass


if __name__ == "__main__":
    register()
