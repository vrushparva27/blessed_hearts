# -*- coding: utf-8 -*-
{

    "name": "Blessed Hearts",
    "version": "13.0.0.0",
    "currency": 'INR',
    "summary": "Based ",
    "category": "Industries",
    "description": """
    Blessed Hearts
""",

    "depends": ["base", 'backend_theme_v13'],
    "data": [
        'data/ir_sequence_data.xml',
        'views/assets.xml',
        'views/medical_patient.xml',
        # 'views/account_view.xml',
        'security/ir.model.access.csv',
    ],
    "author": "Vrushparva Vaishnav",
    "installable": True,
    "application": True,
    "auto_install": False,
}
