from . import __version__ as app_version

app_name = "keyboard_shortcuts"
app_title = "Keyboard Shortcuts"
app_publisher = "Your Organization"
app_description = "Add and manage custom keyboard shortcuts across ERPNext"
app_email = "your@email.com"
app_license = "MIT"

# App version
app_version = app_version

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/keyboard_shortcuts/css/keyboard_shortcuts.css"
app_include_js = "/assets/keyboard_shortcuts/js/keyboard_shortcuts.js"

# include js, css files in header of web template
# web_include_css = "/assets/keyboard_shortcuts/css/keyboard_shortcuts.css"
# web_include_js = "/assets/keyboard_shortcuts/js/keyboard_shortcuts.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "keyboard_shortcuts/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "keyboard_shortcuts/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by login)
# website_user_home_page = "login"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "keyboard_shortcuts.utils.jinja_methods",
# 	"filters": "keyboard_shortcuts.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "keyboard_shortcuts.install.before_install"
after_install = "keyboard_shortcuts.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "keyboard_shortcuts.uninstall.before_uninstall"
# after_uninstall = "keyboard_shortcuts.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "keyboard_shortcuts.utils.before_app_install"
# after_app_install = "keyboard_shortcuts.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "keyboard_shortcuts.utils.before_app_uninstall"
# after_app_uninstall = "keyboard_shortcuts.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "keyboard_shortcuts.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"keyboard_shortcuts.tasks.all"
# 	],
# 	"daily": [
# 		"keyboard_shortcuts.tasks.daily"
# 	],
# 	"hourly": [
# 		"keyboard_shortcuts.tasks.hourly"
# 	],
# 	"weekly": [
# 		"keyboard_shortcuts.tasks.weekly"
# 	],
# 	"monthly": [
# 		"keyboard_shortcuts.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "keyboard_shortcuts.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "keyboard_shortcuts.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype form,
# along with any modifications made in the `config` function, will be discarded

# override_doctype_dashboards = {
# 	"Task": "keyboard_shortcuts.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["keyboard_shortcuts.utils.before_request"]
# after_request = ["keyboard_shortcuts.utils.after_request"]

# Job Events
# ----------
# before_job = ["keyboard_shortcuts.utils.before_job"]
# after_job = ["keyboard_shortcuts.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"is_table": True,
# 		"redact_fields": ["{field_1}", "{field_2}"]
# 	},
# 	{
# 		"doctype": "{doctype_4}",
# 		"is_table": True,
# 	}
# ]

# Authentication and authorization
# ---------------------------------

# auth_hooks = [
# 	"keyboard_shortcuts.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app's doctypes
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
