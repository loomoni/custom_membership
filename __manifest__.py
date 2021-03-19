{
    'name': 'Membership',
    'version': '12.0.1.0.0',
    'category': 'Extra Tool',
    'summary': 'Associate Membership Registration',
    'author': 'Loomoni Morwo',
    'company': 'TANZANIA PRIVATE SECTOR FOUNDATION',
    'website': "http://www.tpsftz.org/",
    'depends': ['account', 'base', 'sale', 'board', 'base_setup', 'product', 'analytic', 'portal', 'digest'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/contact_inherit.xml',
    ],
    'qweb': [
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
