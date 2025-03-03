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

    "depends": ["base", 'account'],
    "data": [
        'data/ir_sequence_data.xml',
        'report/invoice_report.xml',
        'views/account_view.xml',
        'views/medical_patient.xml',
        'views/patient_medicine.xml',
        'views/medicines_list.xml',
        'report/report.xml',
        'report/md_layout.xml',
        'report/medicines_report.xml',
        'report/report_all.xml',
        'security/ir.model.access.csv',
        'views/assets.xml',
    ],
    "author": "Vrushparva Vaishnav",
    "installable": True,
    "application": True,
    "auto_install": False,
}
