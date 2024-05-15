import frappe
from frappe import _

from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from alpha_medical.custom_fields.patient import patient


def after_app_install(app_name):
    create_custom_fields(get_custom_fields())


def get_custom_fields():
    return {
        "Patient": patient(),
    }


def before_uninstall():
    delete_custom_fields(get_custom_fields())


def delete_custom_fields(custom_fields: dict):
    """
    :param custom_fields: a dict like `{'Salary Slip': [{fieldname: 'loans', ...}]}`
    """
    for doctype, fields in custom_fields.items():
        frappe.db.delete(
            "Custom Field",
            {
                "fieldname": ("in", [field["fieldname"] for field in fields]),
                "dt": doctype,
            },
        )

        frappe.clear_cache(doctype=doctype)
