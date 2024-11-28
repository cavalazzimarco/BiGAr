import bpy

# Paths to the surfaces (use raw strings to handle Windows paths properly)
surface_1_path = r"F:\2024\CV2024_Topography\CV2024_Meshes\CV2024_SU249Lev1-251Local.obj"
surface_2_path = r"F:\2024\CV2024_Topography\CV2024_Meshes\CV2024_SU249Lev2-252Local.obj"

# Function to import OBJ file
def import_obj(filepath):
    bpy.ops.import_scene.obj(filepath=filepath)

# Import surfaces
import_obj(surface_1_path)
import_obj(surface_2_path)

# Assuming the imported objects are named as the filenames without the extension
surface_1_name = "CV2024_SU249Lev1-251Local"
surface_2_name = "CV2024_SU249Lev2-252Local"

# Get references to the imported objects
surface_1_obj = bpy.data.objects.get(surface_1_name)
surface_2_obj = bpy.data.objects.get(surface_2_name)

# Print debug information
print(f"Surface 1: {surface_1_obj}")
print(f"Surface 2: {surface_2_obj}")
