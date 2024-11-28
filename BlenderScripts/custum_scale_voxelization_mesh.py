import bpy
import bmesh

# Function to voxelize the mesh
def voxelize_mesh(obj, voxel_size):
    # Get the mesh data
    mesh = obj.data
    
    # Create a BMesh from the mesh data
    bm = bmesh.new()
    bm.from_mesh(mesh)
    
    # Calculate voxel size (adjust as needed for your scale)
    voxel_size *= obj.scale[0]  # Adjust voxel size based on object scale
    
    # Voxelization process: Loop through vertices and snap them to a grid
    for v in bm.verts:
        # Snap vertex coordinates to voxel grid
        v.co.x = round(v.co.x / voxel_size) * voxel_size
        v.co.y = round(v.co.y / voxel_size) * voxel_size
        v.co.z = round(v.co.z / voxel_size) * voxel_size
    
    # Update BMesh and apply changes back to mesh
    bm.to_mesh(mesh)
    bm.free()

# Example usage: Find the object by name and voxelize
obj = bpy.data.objects.get("CV2024_SU249Lev1-251Local")

# Check if the object is a mesh
if obj and obj.type == 'MESH':
    # Define voxel size in meters (0.01m)
    voxel_size = 0.01
    
    # Call the voxelization function
    voxelize_mesh(obj, voxel_size)
    
    print(f"Mesh '{obj.name}' voxelized with voxel size {voxel_size} meters.")
else:
    print(f"Mesh object 'CV2024_SU249Lev1-251Local' not found or is not a mesh.")
