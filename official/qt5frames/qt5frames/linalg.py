# -*- coding: utf-8 -*-
# Copyright (c) Sebastian Klaassen. All Rights Reserved.
# Distributed under the MIT License. See LICENSE file for more info.

import numbers
import math
import numpy as np
import quaternion

__all__ = [
	'lerp', 'saturate', 'sqlength', 'length', 'normalize', 'dot', 'cross', 'reflect', 'mod', 'step',
	'mat4', 'quat', 'vec2', 'vec2a', 'vec3', 'vec3a', 'vec4', 'vec4a'
]

def lerp(origin, target, f):
	f = saturate(f)
	g = 1 - f
	if isinstance(origin, numbers.Number) and isinstance(target, numbers.Number):
		return origin * g + target * f
	elif isinstance(origin, vec4) and isinstance(target, vec4):
		return vec4(
			origin.x * g + target.x * f,
			origin.y * g + target.y * f,
			origin.z * g + target.z * f,
			origin.w * g + target.w * f
		)
	elif isinstance(origin, vec3) and isinstance(target, vec3):
		return vec3(
			origin.x * g + target.x * f,
			origin.y * g + target.y * f,
			origin.z * g + target.z * f
		)
	elif isinstance(origin, vec2) and isinstance(target, vec2):
		return vec2(
			origin.x * g + target.x * f,
			origin.y * g + target.y * f
		)
	elif isinstance(origin, quat) and isinstance(target, quat):
		return quaternion.slerp_evaluate(origin, target, f)
	else:
		raise TypeError

def saturate(f):
	if isinstance(f, numbers.Number):
		return 0.0 if f <= 0.0 else (1.0 if f >= 1.0 else f)
	elif isinstance(f, vec4):
		return vec4(saturate(f.x), saturate(f.y), saturate(f.z), saturate(f.w))
	else:
		raise TypeError

def sqlength(v):
	if isinstance(v, vec4):
		return v.x * v.x + v.y * v.y + v.z * v.z
	elif isinstance(v, vec2):
		return v.x * v.x + v.y * v.y
	else:
		raise TypeError
def length(v):
	if isinstance(v, vec4):
		return math.sqrt(v.x * v.x + v.y * v.y + v.z * v.z)
	elif isinstance(v, vec2):
		return math.sqrt(v.x * v.x + v.y * v.y)
	else:
		raise TypeError

def normalize(v):
	if isinstance(v, vec4):
		div = 1.0 / math.sqrt(v.x * v.x + v.y * v.y + v.z * v.z + v.w * v.w)
		return vec4(v.x * div, v.y * div, v.z * div, v.w * div)
	elif isinstance(v, vec3):
		div = 1.0 / math.sqrt(v.x * v.x + v.y * v.y + v.z * v.z)
		return vec3(v.x * div, v.y * div, v.z * div)
	elif isinstance(v, vec2):
		div = 1.0 / math.sqrt(v.x * v.x + v.y * v.y)
		return vec2(v.x * div, v.y * div)
	else:
		raise TypeError

def dot(a, b):
	if isinstance(a, vec4) and isinstance(b, vec4):
		return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w
	elif isinstance(a, vec3) and isinstance(b, vec3):
		return a.x * b.x + a.y * b.y + a.z * b.z
	elif isinstance(a, vec2) and isinstance(b, vec2):
		return a.x * b.x + a.y * b.y
	else:
		raise TypeError
def cross(a, b):
	if isinstance(a, vec3) and isinstance(b, vec3):
		return vec3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)
	else:
		raise TypeError

def reflect(n, v):
	if isinstance(n, vec3) and isinstance(v, vec3):
		return v - n * (2 * dot(n, v))
	else:
		raise TypeError

def mod(a, b):
	return a % b

def step(edge, x):
	return 0.0 if x < edge else 1.0

class vec2(np.ndarray):
	def __new__(cls, *args):
		return super(vec2, cls).__new__(cls, (2,), np.float32)
	def __init__(self, *args):
		super(vec2, self).__init__()
		idx = 0
		for arg in args:
			if isinstance(arg, numbers.Number):
				if idx >= 2:
					raise ValueError("Too many arguments to vec2()")
				self[idx] = arg
				idx += 1
			elif hasattr(arg, '__len__'):
				if hasattr(arg, 'flat'):
					arg = arg.flat
				if idx + len(arg) > 2:
					raise ValueError("Too many arguments to vec2()")
				for i, val in enumerate(arg):
					self[idx + i] = val
				idx += len(arg)
		for idx in range(idx, 2):
			self[idx] = 0
	def __array_finalize__(self, obj):
		if obj is None: return
		self.info = getattr(obj, 'info', None)
	def __str__(self):
		return "vec2({}, {})".format(self[0], self[1])

	@property
	def x(self): return self[0]
	@x.setter
	def x(self, value): self[0] = value
	@property
	def y(self): return self[1]
	@y.setter
	def y(self, value): self[1] = value

	def copyto(self, v): np.copyto(v, self)
	def clone(self): return vec2(self) #TODO: Consider replacing with np.ndarray.clone()

class vec3(np.ndarray):
	def __new__(cls, *args):
		return super(vec3, cls).__new__(cls, (3,), np.float32)
	def __init__(self, *args):
		super(vec3, self).__init__()
		idx = 0
		for arg in args:
			if isinstance(arg, numbers.Number):
				if idx >= 3:
					raise ValueError("Too many arguments to vec3()")
				self[idx] = arg
				idx += 1
			elif hasattr(arg, '__len__'):
				if hasattr(arg, 'flat'):
					arg = arg.flat
				if idx + len(arg) > 3:
					raise ValueError("Too many arguments to vec3()")
				for i, val in enumerate(arg):
					self[idx + i] = val
				idx += len(arg)
		for idx in range(idx, 3):
			self[idx] = 0
	def __array_finalize__(self, obj):
		if obj is None: return
		self.info = getattr(obj, 'info', None)
	def __str__(self):
		return "vec3({}, {}, {})".format(self[0], self[1], self[2])

	@property
	def x(self): return self[0]
	@x.setter
	def x(self, value): self[0] = value
	@property
	def y(self): return self[1]
	@y.setter
	def y(self, value): self[1] = value
	@property
	def z(self): return self[2]
	@z.setter
	def z(self, value): self[2] = value

	def copyto(self, v): np.copyto(v, self)
	def clone(self): return vec3(self) #TODO: Consider replacing with np.ndarray.clone()

	def __mul__(self, other):
		return vec3(super(vec3, self).__mul__(other))
	def __truediv__(self, other):
		return vec3(super(vec3, self).__truediv__(other))

class vec4(np.ndarray):
	def __new__(cls, *args):
		return super(vec4, cls).__new__(cls, (4,), np.float32)
	def __init__(self, *args):
		super(vec4, self).__init__()
		idx = 0
		for arg in args:
			if isinstance(arg, numbers.Number):
				if idx >= 4:
					raise ValueError("Too many arguments to vec4()")
				self[idx] = arg
				idx += 1
			elif hasattr(arg, '__len__'):
				if hasattr(arg, 'flat'):
					arg = arg.flat
				if idx + len(arg) > 4:
					raise ValueError("Too many arguments to vec4()")
				for i, val in enumerate(arg):
					self[idx + i] = val
				idx += len(arg)
		for idx in range(idx, 4):
			self[idx] = 0
	def __array_finalize__(self, obj):
		if obj is None: return
		self.info = getattr(obj, 'info', None)
	def __str__(self):
		return "vec4({}, {}, {}, {})".format(self[0], self[1], self[2], self[3])

	@property
	def x(self): return self[0]
	@x.setter
	def x(self, value): self[0] = value
	@property
	def y(self): return self[1]
	@y.setter
	def y(self, value): self[1] = value
	@property
	def z(self): return self[2]
	@z.setter
	def z(self, value): self[2] = value
	@property
	def w(self): return self[3]
	@w.setter
	def w(self, value): self[3] = value
	@property
	def xy(self): return vec2(self[0], self[1])

	def copyto(self, v): np.copyto(v, self)
	def clone(self): return vec4(self) #TODO: Consider replacing with np.ndarray.clone()

class mat4(np.matrix):
	def __new__(cls, *elements):
		return super(mat4, cls).__new__(cls, np.array(np.empty((4, 4)), np.float32, copy=False))
	def __init__(self, *args, **kwargs):
		super(mat4, self).__init__()
		if args:
			idx = 0
			for arg in args:
				if isinstance(arg, numbers.Number):
					if idx >= 16:
						raise ValueError("Too many arguments to mat4()")
					self.put(idx, arg)
					idx += 1
				elif hasattr(arg, '__len__'):
					if hasattr(arg, 'flat'):
						arg = arg.flat
					if idx + len(arg) > 16:
						raise ValueError("Too many arguments to mat4()")
					for i, val in enumerate(arg):
						self.put(idx + i, val)
					idx += len(arg)
			if idx != 16:
				raise ValueError("Too little arguments to mat4()")
		else:
			self[0, 0] = 1.0
			self[0, 1] = 0.0
			self[0, 2] = 0.0
			self[0, 3] = 0.0
			self[1, 0] = 0.0
			self[1, 1] = 1.0
			self[1, 2] = 0.0
			self[1, 3] = 0.0
			self[2, 0] = 0.0
			self[2, 1] = 0.0
			self[2, 2] = 1.0
			self[2, 3] = 0.0
			self[3, 0] = 0.0
			self[3, 1] = 0.0
			self[3, 2] = 0.0
			self[3, 3] = 1.0

	def __array_finalize__(self, obj):
		if obj is None: return
		self.info = getattr(obj, 'info', None)
	#def __str__(self):
	#	return super.__str__(self)
	def ortho(self, left, right, bottom, top, znear, zfar):
		self[0, 0] = 2.0 / (right - left)
		self[0, 1] = 0.0
		self[0, 2] = 0.0
		self[0, 3] = 0.0
		self[1, 0] = 0.0
		self[1, 1] = 2.0 / (top - bottom)
		self[1, 2] = 0.0
		self[1, 3] = 0.0
		self[2, 0] = 0.0
		self[2, 1] = 0.0
		self[2, 2] = -2.0 / (zfar - znear)
		self[2, 3] = 0.0
		self[3, 0] = (left + right) / (left - right)
		self[3, 1] = (bottom + top) / (bottom - top)
		self[3, 2] = (znear + zfar) / (znear - zfar)
		self[3, 3] = 1.0
	@staticmethod
	def from_ortho(left, right, bottom, top, znear, zfar):
		return mat4(
			2.0 / (right - left), 0.0, 0.0, 0.0,
			0.0 ,2.0 / (top - bottom), 0.0, 0.0,
			0.0, 0.0, -2.0 / (zfar - znear), 0.0,
			(left + right) / (left - right), (bottom + top) / (bottom - top), (znear + zfar) / (znear - zfar), 1.0)
	def frustum(self, left, right, bottom, top, znear, zfar):
		# Source: https://www.khronos.org/opengl/wiki/GluPerspective_code
		temp = 2.0 * znear
		temp2 = right - left
		temp3 = top - bottom
		temp4 = zfar - znear
		self[0, 0] = temp / temp2
		self[0, 1] = 0.0
		self[0, 2] = 0.0
		self[0, 3] = 0.0
		self[1, 0] = 0.0
		self[1, 1] = temp / temp3
		self[1, 2] = 0.0
		self[1, 3] = 0.0
		self[2, 0] = (right + left) / temp2
		self[2, 1] = (top + bottom) / temp3
		self[2, 2] = (-zfar - znear) / temp4
		self[2, 3] = -1.0
		self[3, 0] = 0.0
		self[3, 1] = 0.0
		self[3, 2] = (-temp * zfar) / temp4
		self[3, 3] = 0.0
	@staticmethod
	def from_frustum(left, right, bottom, top, znear, zfar):
		# Source: https://www.khronos.org/opengl/wiki/GluPerspective_code
		temp = 2.0 * znear
		temp2 = right - left
		temp3 = top - bottom
		temp4 = zfar - znear
		return mat4(
			temp / temp2, 0.0, 0.0, 0.0,
			0.0, temp / temp3, 0.0, 0.0,
			(right + left) / temp2, (top + bottom) / temp3, (-zfar - znear) / temp4, -1.0,
			0.0, 0.0, (-temp * zfar) / temp4, 0.0)
	def perspective(self, fovy, aspect_ratio, znear, zfar):
		# Source: https://www.khronos.org/opengl/wiki/GluPerspective_code
		ymax = znear * math.tan(fovy * math.pi / 360.0)
		xmax = ymax * aspect_ratio
		return self.frustum(-xmax, xmax, -ymax, ymax, znear, zfar)
	@staticmethod
	def from_perspective(fovy, aspect_ratio, znear, zfar):
		# Source: https://www.khronos.org/opengl/wiki/GluPerspective_code
		ymax = znear * math.tan(fovy * math.pi / 360.0)
		xmax = ymax * aspect_ratio
		return mat4.from_frustum(-xmax, xmax, -ymax, ymax, znear, zfar)

	def copyto(self, m):
		np.copyto(m, self)
	def clone(self): #TODO: Consider replacing with np.ndarray.clone()
		return mat4(self)

	def transform_normal(self, v):
		if type(v) == vec3:
			return vec3(self.dot(vec4(v[0], v[1], v[2], 1.0))[0:3])
		elif type(v) == vec2:
			return vec2(self.dot(vec4(v[0], v[1], 0.0, 1.0))[0:2])
		else:
			raise ValueError()
	def transform_coord(self, v):
		if type(v) == vec3:
			return vec3(self.dot(vec4(v[0], v[1], v[2], 0.0))[0:3])
		elif type(v) == vec2:
			return vec2(self.dot(vec4(v[0], v[1], 0.0, 0.0))[0:2])
		else:
			raise ValueError()

class quat(np.quaternion):
	def __init__(self, *args):
		if args:
			q = np.empty((4,), np.float32)
			idx = 0
			for arg in args:
				if isinstance(arg, numbers.Number):
					if idx >= 4:
						raise ValueError("Too many arguments to quat()")
					q[idx] = arg
					idx += 1
				elif hasattr(arg, '__len__'):
					if hasattr(arg, 'flat') and not isinstance(arg, np.quaternion):
						arg = arg.flat
					if idx + len(arg) > 4:
						raise ValueError("Too many arguments to quat()")
					for i, val in enumerate(arg):
						q[idx + i] = val
					idx += len(arg)
			for idx in range(idx, 4):
				q[idx] = 0
			super(quat, self).__init__(*q)
		else:
			super(quat, self).__init__(1, 0, 0, 0)

		# if elements and len(elements) == 4:
		# 	super(quat, self).__init__(*elements)
		# elif elements and len(elements) == 1 and isinstance(elements[0], np.quaternion):
		# 	q = elements[0]
		# 	super(quat, self).__init__(q.w, q.x, q.y, q.z)
		# elif elements and len(elements) <= 3:
		# 	q = quat.from_euler_angles(elements[0], 0.0 if len(elements) < 2 else elements[1], 0.0 if len(elements) < 3 else elements[2])
		# 	super(quat, self).__init__(q.w, q.x, q.y, q.z)
		# else:
		# 	super(quat, self).__init__(1, 0, 0, 0)
	def copyto(self, q):
		q.w = self.w
		q.x = self.x
		q.y = self.y
		q.z = self.z
	def clone(self): #TODO: Consider replacing with np.ndarray.clone()
		return quat(self)
	def __len__(self):
		return 4
	def __getitem__(self, idx):
		if idx == 0: return self.w
		if idx == 1: return self.x
		if idx == 2: return self.y
		if idx == 3: return self.z
		raise IndexError()
	@staticmethod
	def from_axis_angle(axis, angle):
		angle /= 2
		s = math.sin(angle)
		return quat(math.cos(angle), s * axis.x, s * axis.y, s * axis.z)
	def look_at(self, eye, target, up):
		zaxis = normalize(eye - target)
		xaxis = normalize(cross(up, zaxis))
		yaxis = cross(zaxis, xaxis)
		m = np.matrix([
			[xaxis.x, xaxis.y, xaxis.z],
			[yaxis.x, yaxis.y, yaxis.z],
			[zaxis.x, zaxis.y, zaxis.z]
		])
		q = quaternion.from_rotation_matrix(m)
		self.w = q.w
		self.x = q.x
		self.y = q.y
		self.z = q.z
	@staticmethod
	def from_look_at(eye, target, up):
		# zaxis = normalize(eye - target)
		# xaxis = normalize(cross(zaxis, up))
		# yaxis = cross(zaxis, xaxis)
		# m = np.matrix([
		# 	[xaxis.x, xaxis.y, xaxis.z],
		# 	[yaxis.x, yaxis.y, yaxis.z],
		# 	[zaxis.x, zaxis.y, zaxis.z]
		# ])
		# return quat(quaternion.from_rotation_matrix(m))
		q = quat()
		q.look_at(eye, target, up)
		return q
	@staticmethod
	def from_two_vectors(a, b):
		m = math.sqrt(2.0 + 2.0 * dot(a, b))
		w = cross(a, b) / m
		return quat(w.x, w.y, w.z, 0.5 * m)
	def euler_angles(self, pitch, roll, yaw):
		cy = math.cos(yaw * 0.5)
		sy = math.sin(yaw * 0.5)
		cr = math.cos(roll * 0.5)
		sr = math.sin(roll * 0.5)
		cp = math.cos(pitch * 0.5)
		sp = math.sin(pitch * 0.5)
		self.w = cy * cr * cp + sy * sr * sp
		self.x = cy * sr * cp - sy * cr * sp
		self.y = cy * cr * sp + sy * sr * cp
		self.z = sy * cr * cp - cy * sr * sp
	@staticmethod
	def from_euler_angles(pitch, roll, yaw):
		q = quat()
		q.euler_angles(pitch, roll, yaw)
		return q
	def rotate_vector(self, v):
		s = self[0]
		r = np.array([self[1], self[2], self[3]])
		m = np.inner(self, self).real
		vr = v + np.cross(2.0 * r, s * v + np.cross(r, v)) / m
		vr2 = quaternion.rotate_vectors([self], v)[0, :]
		#assert(np.array_equal(vr, vr2)) #TODO: Assertion raised. Check equation
		return vr2

class vec2a(np.ndarray):
	def __new__(cls, arg):
		if isinstance(arg, int):
			return super(vec2a, cls).__new__(cls, (arg, 2), np.float32)
		elif isinstance(arg, list):
			return super(vec2a, cls).__new__(cls, (len(arg) if type(arg[0]) == vec2 else len(arg) // 2, 2), np.float32)
		else:
			raise ValueError
	def __init__(self, arg):
		super(vec2a, self).__init__()
		if isinstance(arg, list):
			np.copyto(self, np.reshape(arg, self.shape))
	def __array_finalize__(self, obj):
		if obj is None: return
		self.info = getattr(obj, 'info', None)
	def __str__(self):
		return "vec2a[{}]".format(self.shape[0])
	def __getitem__(self, idx):
		out = vec2()
		super(vec2a, self).take(idx, 0, out)
		return out

class vec3a(np.ndarray):
	def __new__(cls, arg):
		if isinstance(arg, int):
			return super(vec3a, cls).__new__(cls, (arg, 3), np.float32)
		elif isinstance(arg, list):
			return super(vec3a, cls).__new__(cls, (len(arg) if type(arg[0]) == vec3 else len(arg) // 3, 3), np.float32)
		else:
			raise ValueError
	def __init__(self, arg):
		super(vec3a, self).__init__()
		if isinstance(arg, list):
			np.copyto(self, np.reshape(arg, self.shape))
	def __array_finalize__(self, obj):
		if obj is None: return
		self.info = getattr(obj, 'info', None)
	def __str__(self):
		return "vec3a[{}]".format(self.shape[0])
	def __getitem__(self, idx):
		out = vec3()
		super(vec3a, self).take(idx, 0, out)
		return out

class vec4a(np.ndarray):
	def __new__(cls, arg):
		if isinstance(arg, int):
			return super(vec4a, cls).__new__(cls, (arg, 4), np.float32)
		elif isinstance(arg, list):
			return super(vec4a, cls).__new__(cls, (len(arg) if type(arg[0]) == vec4 else len(arg) // 4, 4), np.float32)
		else:
			raise ValueError
	def __init__(self, arg):
		super(vec4a, self).__init__()
		if isinstance(arg, list):
			np.copyto(self, np.reshape(arg, self.shape))
	def __array_finalize__(self, obj):
		if obj is None: return
		self.info = getattr(obj, 'info', None)
	def __str__(self):
		return "vec4a[{}]".format(self.shape[0])
	def __getitem__(self, idx):
		out = vec4()
		super(vec4a, self).take(idx, 0, out)
		return out
