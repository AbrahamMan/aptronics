# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "aptronics"
app_title = "Aptronics"
app_publisher = "Hemant"
app_description = "Aptronics Custom Application"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "hemant@aptronics.co.za"
app_version = "0.0.1"
app_license = "Private"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aptronics/css/aptronics.css"
# app_include_js = "/assets/aptronics/js/aptronics.js"

# include js, css files in header of web template
# web_include_css = "/assets/aptronics/css/aptronics.css"
# web_include_js = "/assets/aptronics/js/aptronics.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "aptronics.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "aptronics.install.before_install"
# after_install = "aptronics.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aptronics.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

#doc_events = {
# 	"Customer": {
# 		"validate": "aptronics.aptronics.config.customer.get_custom_series"
#	},
#	"Contact": {
# 		"validate": "aptronics.aptronics.config.customer.get_custom_series"
#	},
#	"Supplier": {
# 		"validate": "aptronics.aptronics.config.customer.get_custom_series"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"aptronics.tasks.all"
# 	],
# 	"daily": [
# 		"aptronics.tasks.daily"
# 	],
# 	"hourly": [
# 		"aptronics.tasks.hourly"
# 	],
# 	"weekly": [
# 		"aptronics.tasks.weekly"
# 	]
# 	"monthly": [
# 		"aptronics.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "aptronics.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "aptronics.event.get_events"
# }

