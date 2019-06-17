from utils.date import timestamp2datetime


class Category:

	def __init__(self, id, title, description, parent, created_at=None, updated_at=None):
		"""
		Parent can be both 'Category' instance or JSON object.
		"""
		self.id = id
		self.title = title
		self.description = description or ""
		if parent is None:
			self.parent = None
		elif isinstance(parent, Category):
			self.parent = parent
		else:
			self.parent = Category.from_json(parent)
		if created_at:
			self.created_at = timestamp2datetime(timestamp=created_at)
		if updated_at:
			self.updated_at = timestamp2datetime(timestamp=updated_at)
		self.history = self._history()

	def as_json(self):
		return {
			'id': self.id,
			'title': self.title,
			'description': self.description,
			'parent_id': None if not self.parent else self.parent.id
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

	def get_ancestors(self):
		ancestors = []
		parent = self.parent
		while parent:
			ancestors.append(parent)
			parent = parent.parent
		return ancestors

	def _history(self, separator='/'):
		history = self.title
		parent = self.parent
		while parent:
			history = parent.title + separator + history
			if not parent.parent:
				break
			parent = parent.parent
		return history
