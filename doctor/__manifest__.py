# -*- encoding: utf-8 -*-
{
    'name': 'Doctor and Patient',
    'version': '1.0',
    'summary': 'Doctor and Patient Management System',
    'description': '''
    Doctor and Patient Management System Dveloped BY UTK 
    ============================================================    
    ''',
    # 'category': 'Hidden',
    'website': '',
    'depends': ['base', 'uom'],
    'data': ['security/ir.model.access.csv',
             'data/ir_sequence.xml',
             'views/patient.xml',
             'views/patient_consultation_detail.xml',
             ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
