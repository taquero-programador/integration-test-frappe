# Copyright (c) 2022, Javier Rangel and contributors
# For license information, please see license.txt

import frappe
from urllib.request import ftpwrapper
from frappe.website.website_generator import WebsiteGenerator

class TiendaFisica(WebsiteGenerator):
	
	def before_submit(self):
		self.stock_validate()
		existencia = frappe.db.exists(
			'Tienda Fisica',
			{
				'item_name': self.item_name,
				'docstatus': 1,
			},
		)
		if existencia:
			frappe.throw('El item ya existe!')

	# validar nivel de stock
	def stock_validate(self):
		
		if self.stock <= '10':
			frappe.throw('El stock es muy bajo!')