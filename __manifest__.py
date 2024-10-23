{
  'name' : 'Access permission management system',
  'summary' : 'Access permission management system',
  'author' : 'Agustin Battigane',
  'sequence' : '-1',
  'website' : 'http://www.dooit.ar',
  'category' : 'Administration',
  'version' : '0.1',
  'installable' : True,
  'application' : True,
  'auto_install' : False,
  'depends' : ['base', 'contacts'],
  'data' : [
      'security/ir.model.access.csv',
      'views/autorization.xml',
      'views/location.xml',
      'views/user.xml',
      'views/menu.xml',
      'views/autorization_secuence.xml',
      'wizard/create_autorization_wizard.xml',
  ],
  'assets': {
    'web.assets_backend': [
      'ams/static/src/js/autorization_tree_extend.js',
      'ams/static/src/xml/autorization_list_button.xml',
      ],
    },
}

""" los assets se copian igual, se modifica el nombre de los archivos al nombre que les haya designado """