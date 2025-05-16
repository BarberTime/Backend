def get_upload_path(instance, filename):
    # Caso: imagen relacionada a un servicio (Servicio tiene FK a Negocio)
    if hasattr(instance, 'servicio'):
        negocio = getattr(instance.servicio, 'negocio', None)
        if negocio and hasattr(negocio, 'nombre'):
            return f'imagenes/{negocio.nombre}/servicios/{filename}'

    # Caso: imagen relacionada a un empleado (Empleado tiene FK a Negocio)
    elif hasattr(instance, 'empleado'):
        negocio = getattr(instance.empleado, 'negocio', None)
        if negocio and hasattr(negocio, 'nombre'):
            return f'imagenes/{negocio.nombre}/empleados/{filename}'

    # Caso: logo del negocio directamente
    elif hasattr(instance, 'logo'):
        if hasattr(instance, 'nombre'):  # Es el modelo Negocio directamente
            return f'imagenes/{instance.nombre}/logo/{filename}'

    # Caso: foto de perfil de usuario
    elif hasattr(instance, 'foto_perfil'):
        if hasattr(instance, 'id_rol'):
            rol = instance.id_rol.nombre.lower()
            return f'usuarios/{rol}/{filename}'
        elif hasattr(instance, 'rol'):
            rol = instance.rol.nombre.lower()
            return f'usuarios/{rol}/{filename}'

    # Default: imágenes generales del negocio
    if hasattr(instance, 'nombre'):
        return f'imagenes/{instance.nombre}/fotos_negocio/{filename}'

    return f'uploads/otros/{filename}'
