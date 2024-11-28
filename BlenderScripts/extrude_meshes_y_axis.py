import bpy

def extrude_mesh_along_y(obj, distance):
    # Set the object to edit mode
    bpy.context.view_layer.objects.active = obj
    bpy.ops.object.mode_set(mode='EDIT')

    # Select all faces
    bpy.ops.mesh.select_all(action='SELECT')

    # Extrude faces along the Y axis
    bpy.ops.mesh.extrude_region_move(
        MESH_OT_extrude_region={"use_normal_flip": False, "use_dissolve_ortho_edges": False},
        TRANSFORM_OT_translate={"value": (0, distance, 0)}  # Extruding along Y axis
    )

    # Switch back to object mode
    bpy.ops.object.mode_set(mode='OBJECT')

# Mesh object names
mesh1_name = 'CV2024_SU249Lev1-251Local'
mesh2_name = 'CV2024_SU249Lev2-252Local'

# Get the mesh objects
obj1 = bpy.data.objects[mesh1_name]
obj2 = bpy.data.objects[mesh2_name]

# Extrude the meshes along the Y axis by 10 units
extrude_mesh_along_y(obj1, 5)
extrude_mesh_along_y(obj2, 5)
