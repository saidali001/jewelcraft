import bpy
from bpy.types import Operator
from . import helpers






class IMPORT_GEM(Operator):
	'''Create gemstone'''
	bl_label = "Make Gemstone"
	bl_idname = "jewelcraft.import_gem"

	def execute(self, context):
		helpers.gem_import()
		return {'FINISHED'}


class IMPORT_TYPE(Operator):
	'''Change type of selected gemstones'''
	bl_label = "Change Type"
	bl_idname = "jewelcraft.import_type"

	@classmethod
	def poll(cls, context):
		return context.selected_objects

	def execute(self, context):
		helpers.type_replace()
		return {'FINISHED'}


class IMPORT_CUT(Operator):
	'''Change cut of selected gemstones'''
	bl_label = "Change Cut"
	bl_idname = "jewelcraft.import_cut"

	@classmethod
	def poll(cls, context):
		return context.selected_objects

	def execute(self, context):
		helpers.cut_replace()
		return {'FINISHED'}






class IMPORT_PRONGS(Operator):
	'''Create prongs for selected gemstones'''
	bl_label = "Change Cut and Size"
	bl_idname = "jewelcraft.import_prongs"

	@classmethod
	def poll(cls, context):
		return context.selected_objects

	def execute(self, context):
		helpers.prongs_import()
		return {'FINISHED'}


class IMPORT_SINGLE_PRONG(Operator):
	'''Create single prong'''
	bl_label = "Single Prong"
	bl_idname = "jewelcraft.import_single_prong"

	def execute(self, context):
		helpers.single_prong_import()
		return {'FINISHED'}


class IMPORT_CUTTER(Operator):
	'''Create cutters for selected gemstones'''
	bl_label = "Cutter"
	bl_idname = "jewelcraft.import_cutter"

	@classmethod
	def poll(cls, context):
		return context.selected_objects

	def execute(self, context):
		helpers.cutter_import()
		return {'FINISHED'}


class IMPORT_CUTTER_SEAT_ONLY(Operator):
	'''Create (seat only) cutters for selected gemstones'''
	bl_label = "Cutter (Seat only)"
	bl_idname = "jewelcraft.import_cutter_seat_only"

	@classmethod
	def poll(cls, context):
		return context.selected_objects

	def execute(self, context):
		helpers.cutter_import(seat_only=True)
		return {'FINISHED'}


class IMPORT_IMITATION_3_PRONG(Operator):
	'''Create imitation (3 prong)'''
	bl_label = "Imitation (3 prong)"
	bl_idname = "jewelcraft.import_imitation_3_prong"

	def execute(self, context):
		helpers.imitation_import()
		return {'FINISHED'}






class MAKE_DUPLIFACE(Operator):
	'''Create dupliface for selected objects'''
	bl_label = "Make Dupli-face"
	bl_idname = "jewelcraft.make_dupliface"

	@classmethod
	def poll(cls, context):
		return context.selected_objects

	def execute(self, context):
		helpers.make_dupliface()
		return {'FINISHED'}


class WEIGHT_DISPLAY(Operator):
	'''Display weight or volume of the active mesh object'''
	bl_label = "Calculate"
	bl_idname = "jewelcraft.weight_display"

	@classmethod
	def poll(cls, context):
		obj = context.active_object
		return (obj and obj.type == 'MESH')

	def execute(self, context):
		helpers.weight_display()
		return {'FINISHED'}






class EXPORT_STATS(Operator):
	'''Export statistics for the project'''
	bl_label = "Export Stats"
	bl_idname = "jewelcraft.export_stats"

	def execute(self, context):
		helpers.export_stats()
		return {'FINISHED'}
