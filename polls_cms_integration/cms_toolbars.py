from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.utils.urlutils import admin_reverse
from polls.models import Poll


class PollToolbar(CMSToolbar):

	supported_apps = ['polls']

	def populate(self):

		if not self.is_current_app:
			return

		#Menus
		menu = self.toolbar.get_or_create_menu(
			'polls_cms_integration-polls',  # a unique key for this menu
            'Polls',                        # the text that should appear in the menu
			)

		menu.add_sideframe_item(
			name='Poll list',  # name of the new menu item
			url=admin_reverse('polls_poll_changelist'),  # the URL it should open with
		)

		menu.add_modal_item(
			name='Add a new poll',  # name of the new menu item
			url=admin_reverse('polls_poll_add'),  # the URL it should open with
		)

		#Buttons
		buttonlist = self.toolbar.add_button_list()

		buttonlist.add_sideframe_button(
			name='Poll list',
			url=admin_reverse('polls_poll_changelist'),
		)

		buttonlist.add_modal_button(
		name = 'Add a new poll',
		url = admin_reverse('polls_poll_add'),
		)


# register the toolbar
toolbar_pool.register(PollToolbar)