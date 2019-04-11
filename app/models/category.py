from datetime import datetime
from datetime import timezone


class Category:

	def __init__(self, id, title, description, parent, created_at, updated_at):
		"""
		Parent can be both 'Category' instance or JSON object.
		"""
		self.id = id
		self.title = title
		self.description = description or ""
		if parent is None:
			self.parent = None
		elif type(parent) is Category:
			self.parent = parent
		else:
			self.parent = Category.from_json(parent)
		self.created_at = created_at
		self.updated_at = updated_at
		self.history = self._history()

	def as_dict(self):
		return {
			'id': self.id,
			'description': self.description,
			'parent': self.parent,
			'created_at': self.created_at,
			'updated_at': self.updated_at,
		}

	@staticmethod
	def from_json(json):
		return Category(
			id=json['id'],
			title=json['title'],
			description=json['description'],
			parent=json['parent'],
			created_at=json['created_at'],
			updated_at=json['updated_at']
		)

	def _history(self, separator='/'):
		history = self.title
		parent = self.parent
		while parent:
			history = parent.title + separator + history
			if not parent.parent:
				break
			parent = parent.parent
		return history
