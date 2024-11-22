# -*- coding: utf-8 -*-
{
    "name": "Academy System Information Management v1.2",

    "summary": "Create and manage students for your academy",

    "description": """
Create and manage students for your academy.
    """,

    "author": "Syamsul Maarif",
    "website": "https://halalmui.org",
    "category": "Education",
    "license": "AGPL-3",
    "website": "halalmui.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "version": "1.0",

    # any module necessary for this one to work correctly
    "depends": ["base"],

    # always loaded
    "data": [
        "views/menu.xml",
        "security/ir.model.access.csv",
        "views/course.xml",            
        "views/session.xml",    
        "views/attendee.xml",
        "views/partner.xml",
    #     "views/workflow.xml",
    ],
    # only loaded in demonstration mode
    # "demo": [
    #     "demo/demo.xml",
    # ],
    "images": ["static/images/banner.png", "static/description/icon.png"],
    "installable": True,
    "application": True,  # Esto indica que tu módulo es una aplicación.
    "auto_install": False,
}

