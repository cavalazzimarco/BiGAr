import bpy

# Names of the two meshes
mesh_1_name = "Mesh1"  # Name of the target mesh
mesh_2_name = "Mesh2"  # Name of the mesh to subtract

# Ensure the meshes exist in the scene
if mesh_1_name in bpy.data.objects and mesh_2_name in bpy.data.objects:
    # Get the objects
    mesh_1 = bpy.data.objects[mesh_1_name]
    mesh_2 = bpy.data.objects[mesh_2_name]
    
    # Create a boolean modifier
    boolean_modifier = mesh_1.modifiers.new(name="Boolean Modifier", type='BOOLEAN')
    
    # Set the operation to difference (subtraction)
    boolean_modifier.operation = 'DIFFERENCE'
    
    # Set the object to subtract
    boolean_modifier.object = mesh_2
    
    # Apply the modifier
    bpy.context.view_layer.objects.active = mesh_1
    bpy.ops.object.modifier_apply(modifier=boolean_modifier.name)
    
    # Optionally, delete the subtracted mesh
    bpy.data.objects.remove(mesh_2, do_unlink=True)
    
    print(f"Boolean subtraction applied successfully between {mesh_1_name} and {mesh_2_name}.")
else:
    print("One or both meshes not found in the scene.")
