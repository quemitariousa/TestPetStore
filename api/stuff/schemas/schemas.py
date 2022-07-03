schema_pet_create = {'type': 'object',
                     'properties': {'id': {'type': 'integer'},
                                    'name': {'type': 'string'},
                                    'photoUrls': {'type': 'array'},
                                    'tags': {'type': 'array'}},
                     'required': ['id', 'name', 'photoUrls', 'tags']}

schema_pet_update = {'type': 'object',
                     'properties': {'id': {'type': 'integer'},
                                    'category': {'type': 'object',
                                                 'properties': {'id': {'type': 'integer'},
                                                                'name': {'type': 'string'}},
                                                 'required': ['id', 'name']},
                                    'name': {'type': 'string'},
                                    'photoUrls': {'type': 'array',
                                                  'items': {'type': 'string'}},
                                    'tags': {'type': 'array', 'items':
                                        {'type': 'object',
                                         'properties': {'id': {'type': 'integer'},
                                                        'name': {'type': 'string'}},
                                         'required': ['id', 'name']}},
                                    'status': {'type': 'string'}},
                     'required': ['category', 'id', 'name', 'photoUrls', 'status', 'tags']}

schema_pet_delete = {'type': 'object',
                     'properties': {'code': {'type': 'integer'},
                                    'type': {'type': 'string'},
                                    'message': {'type': 'string'}},
                     'required': ['code', 'message', 'type']}

schema_pet_get = {'type': 'object',
                  'properties': {'id': {'type': 'integer'},
                                 'name': {'type': 'string'},
                                 'photoUrls': {'type': 'array'},
                                 'tags': {'type': 'array'}},
                  'required': ['id', 'name', 'photoUrls', 'tags']}

schema_user_get = {'type': 'object',
                   'properties': {'code': {'type': 'integer'},
                                  'type': {'type': 'string'},
                                  'message': {'type': 'string'}},
                   'required': ['code', 'message', 'type']}
