class Cam_Pan_Helper:




	def __init__(self):
		self.oX = 0
		self.oY = 0
		self.oZ = 0
		
		self.dof_object=None
		self.target_object=None
		
		self.init_cam_data();
		
		
	def init_cam_data(self):
		self.cam = bpy.context.scene.camera


		self.cam.select = True
		bpy.context.scene.objects.active = self.cam


		self.oX = self.cam.location.x
		self.oY = self.cam.location.y
		self.oZ = self.cam.location.z
		
		self.lens = self.cam.data.lens
		
		self.dof_object=self.find_dof(self.cam)


		if self.dof_object!=None:
			print("found DOF")
			self.oTX = self.dof_object.location.x
			self.oTY = self.dof_object.location.y
			self.oTZ = self.dof_object.location.z
			
	


	def find_dof(self,object):
		for constraint in object.constraints:
			if constraint.type == 'TRACK_TO':
				return constraint.target
		return None
		




	def get_object_largest_dimension(self,obj,usescale=False):
		max_obj_dimension = 0
		
		if usescale==True:


			if obj.scale.x&gt;max_obj_dimension:
				max_obj_dimension=obj.scale.x
				
			if obj.scale.y&gt;max_obj_dimension:
				max_obj_dimension=obj.scale.y
				
			if obj.scale.z&gt;max_obj_dimension:
				max_obj_dimension=obj.scale.z
		
		else:	


			if obj.dimensions.x&gt;max_obj_dimension:
				max_obj_dimension=obj.dimensions.x
				
			if obj.dimensions.y&gt;max_obj_dimension:
				max_obj_dimension=obj.dimensions.y
				
			if obj.dimensions.z&gt;max_obj_dimension:
				max_obj_dimension=obj.dimensions.z
			
		return max_obj_dimension
		
	def get_distance_between_objects(self,o1,o2):
		camObj = self.cam
		
		x1 = o1.location.x
		y1 = o1.location.y
		z1 = o1.location.z
		
		x2 = o2.location.x
		y2 = o2.location.y
		z2 = o2.location.z


		xd = x2-x1
		yd = y2-y1
		zd = z2-z1
		dist = math.sqrt(xd*xd + yd*yd + zd*zd)


		return dist
		
	def get_relative_angle(self,max_object_dimension,distance):
		relative_angle=math.atan(max_object_dimension/distance)
		return relative_angle


	def zoom_out(self,obj,stepX,stepY,stepZ,zoom_limit=200):
		camObj = self.cam
		
		camObj.location.x = obj.location.x+stepX
		camObj.location.y = obj.location.y+stepY
		camObj.location.z = obj.location.z+stepZ
		
		cam_angle = camObj.data.angle
		print("Camera Angle: " + str(math.degrees(cam_angle)))
		
		continue_zoom = True
		
		while continue_zoom:


			relative_angle = self.get_object_relative_angle(obj)
			print("relative_angle:" + str(math.degrees(relative_angle)) + " cam_angle: " + str(math.degrees(cam_angle)))
			if cam_angle&gt;(relative_angle*1.6):
				
				print("aborting")
				
				# at this point we have gone too far so set it to last good position
				
				continue_zoom=False
				
			else:
				camObj.location.x=camObj.location.x+stepX
				camObj.location.y=camObj.location.y+stepY
				camObj.location.z=camObj.location.z+stepZ
				
				
			# prevent something crazy from happening		
			if abs(camObj.location.x)&gt;zoom_limit:
				continue_zoom=False
				
			if abs(camObj.location.y)&gt;zoom_limit:
				continue_zoom=False
				
			if abs(camObj.location.z)&gt;zoom_limit:
				continue_zoom=False
				
		print("finished loop")
		relative_angle = self.get_object_relative_angle(obj)
		print("relative_angle:" + str(math.degrees(relative_angle)) + " cam_angle: " + str(math.degrees(cam_angle)))




	def get_object_relative_angle(self,obj):		


		camObj = self.cam
				
		distance = self.get_distance_between_objects(obj,camObj)
		print("distance from Camera to target: " + str(distance))
		
		max_object_dimension = self.get_object_largest_dimension(obj,True)
		print("Max Object Dimension:" + str(max_object_dimension))
		
		relative_angle=self.get_relative_angle(max_object_dimension,distance)
		print("Object Relative Angle:" + str(math.degrees(relative_angle)))
		
		return relative_angle