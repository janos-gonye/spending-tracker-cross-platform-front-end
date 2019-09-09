from kivy.lang import Builder

from services.category import CategoryService
from services.exceptions import ConnectionError_
from screens.category.base import CategoryScreen
from uix.popups.info import InfoPopup


Builder.load_file('screens/category/merge/category_merge.kv')


class CategoryMergeScreen(CategoryScreen):
    remove_merged_default = False

    def on_pre_enter(self):
        super().on_pre_enter()
        if self.cat_conn_error:
            return
        self.cat_subject_select.init(elements=self.categories)
        self.cat_target_select.init(elements=self.categories)
        self.service = CategoryService()

    def merge(self, ):
        subject = self.cat_subject_select.selected
        target = self.cat_target_select.selected
        remove_merged = self.remove_merged_checkbox.active
        if None in (subject, target):
            InfoPopup(title="Error", message="Both fields required.").open()
            return
        try:
            self.service.merge(subject.id, target.id, remove_merged)
        except ConnectionError_ as err:
            InfoPopup(title='Error', message=str(err)).open()
            return
        InfoPopup(title='Success',
                  message='Categories merged successfully.').open()
        self.manager.current = 'category_list'

    def reset(self):
        self.cat_subject_select.selected = None
        self.cat_target_select.selected = None
        remove_merged_checkbox = self.remove_merged_default

    def on_leave(self):
        self.reset()
