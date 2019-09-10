from kivy.lang import Builder

from screens.category.base import CategoryScreen
from services.category import CategoryService
from services.exceptions import ConnectionError_
from uix.popups.confirm.helpers import confirm
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

    def merge(self):
        if not self.check():
            return
        confirm(title='Merging Categories',
                question=(
                    'All transactions of the selected category\n'
                    "and its descendents' transactions will be merged\n"
                    'into the second selected category.\n'
                    'The result of this action is permanent.\n'
                    'Are you sure you want to continue?'),
                confirmed=self._merge)

    def _merge(self):
        subject = self.cat_subject_select.selected
        target = self.cat_target_select.selected
        remove_merged = self.remove_merged_checkbox.active
        try:
            self.service.merge(subject, target, remove_merged)
        except ConnectionError_ as err:
            InfoPopup(title='Error', message=str(err)).open()
            return
        InfoPopup(title='Success',
                  message='Categories merged successfully.').open()
        self.manager.current = 'category_list'

    def check(self):
        subject = self.cat_subject_select.selected
        target = self.cat_target_select.selected
        if None in (subject, target):
            InfoPopup(title="Error", message="Both fields required.").open()
            return False
        return True

    def reset(self):
        self.cat_subject_select.selected = None
        self.cat_target_select.selected = None
        remove_merged_checkbox = self.remove_merged_default

    def on_leave(self):
        self.reset()
