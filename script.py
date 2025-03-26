from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction
from pyrevit import revit, DB

# Get the active Revit document
doc = revit.doc

# Collect all walls in the model
walls = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls).WhereElementIsNotElementType().ToElements()

# Start a transaction to modify the document
t = Transaction(doc, "Assign Wall Mark Numbers")
t.Start()

# Loop through walls and assign sequential numbers
for index, wall in enumerate(walls, start=1):
    mark_param = wall.LookupParameter("Mark")
    if mark_param and not mark_param.IsReadOnly:
        mark_param.Set(str(index))  # Assign numbers sequentially

t.Commit()

print("Wall Mark numbers assigned successfully!")
