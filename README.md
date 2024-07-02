# PROYECTO-PYTHON-SCRUM
	Prototipo preliminar de proyecto de biblioteca virtual en Python - Knowledge Jungle
	Este contiene un menú principal en el que se le pregunta al usuario sobre como desea acceder: usuario normal (sin privilegios) y usuario administrador. Se va a brindar la opción de desistir del ingreso al programa en cualquier momento.
	El usuario administrador para ingresar le va a ser requerida una contraseña predefinida para salvaguardar la seguridad y la información del repositorio de libros (La contraseña predefinida del usuario administrador es admin12345), ya que, este usuario tiene privilegios de mayor categoría que el usuario común, y, por consiguiente permiso para realizar ciertas acciones y cambios como:

	•	Añadir libros
	Para esta característica le será requerida cierta información sobre el libro a añadir:

	o	El nombre del libro 
	o	Edad mínima para acceder al contenido de este libro
	o	Autor (es) del libro
	o	Género literario al que pertenece el libro
	o	Descripción del libro
	o	Año de publicación
	o	Cantidad de copia del libro que hay en inventario
	o	Precio del libro

	•	Modificar los datos de un libro
	Se le solicitará introducir el nombre del libro que desea modificar y podrá escoger entre estas opciones a modificar:
	o	Nombre del libro
	o	Edad mínima para acceder al libro
	o	Autor (es)
	o	Categoría del libro
	Se le pedirá al usuario que introduzca el numero de la categoría a la cual desea reasignar el libro
	o	Descripción del libro
	o	Stock de copias del libro
	o	Precio del libro
	
	•	Eliminar un libro
	Se le solicitara el nombre del libro a eliminar y una confirmación de seguridad
	•	Mostrar Libros
	Esto va a mostrar todos los libros existentes en la biblioteca y algunos datos de estos como:
	o	Nombre
	o	Edad mínima para acceder al libro
	o	Autor (es)
	o	Categoría del libro
	o	Descripción
	o	Año de publicación
	o	Stock
	o	Precio
	•	Eliminar usuarios
	Esto va a mostrar una lista de usuarios existentes enumerados en orden de registro, se le va a pedir al usuario que introduzca el numero del usuario que desea eliminar.
	Lo ideal es que en un futuro se pueda buscar el usuario que se quiere eliminar ya que si se maneja un gran volumen de usuarios va a ser poco conveniente tener que buscar entre una gran lista de números para encontrar el del usuario que se desea eliminar
	•	Modificar usuarios
	Se va a solicitar el numero de documento del usuario del cual se desea modificar información.
	Se podrá modificar la siguiente información:
	o	Nombre
	o	Edad
	o	Correo Electrónico
	o	Libros adquiridos
	o	Tipo de cliente
	Después contamos con el usuario normal el cual al acceder a su menú va a tener tres opciones:
	•	Registrarse
	•	Iniciar sesión
	•	Salir
	Para la de registro se le van a pedir los siguientes datos al usuario:
	o	Nombre
	o	Numero de documento de identificación (Esto para identificar cada usuario más fácil y evitar que se creen usuarios con el mismo ID)
	o	Contraseña para el usuario a crear
	o	Correo electrónico para recuperación
	o	Edad
	Después de realizar el registro se llevará de nuevo al menú principal del usuario.
	Al seleccionar la opción de iniciar sesión se le va a pedir el número de identificación con el que se registró y la contraseña que estableció.
	Al ingresar a su usuario va a encontrar las siguientes opciones:
	o	Buscar libros por nombre
	Se le va a solicitar al usuario que introduzca el nombre del libro, lo ideal es que escriba el nombre y tal y como esta ya que de otra manera el programa no lo reconocerá (No hay conflicto con mayúsculas ni minúsculas)
	o	Acceder a los libros mediante género literario
	Se le mostraran al usuario los géneros literarios disponibles y los libros contenidos en estos
	o	Comprar libros
	El usuario podrá ingresar a este menú y agregar un libro al carrito mediante búsqueda o género literario
	o	Ver el carrito
	Aquí se podrán acceder a dos opciones: Enlistar libros en el carrito y comprar carrito. La primera enumera los libros agregados al carrito en orden cronológico y permite eliminar elementos dentro del carrito. En caso de que no haya ningún libro en el carrito se le mostrara un mensaje al usuario y lo devolverá al menú inicial, la de comprar permitirá confirmar y comprar los ítems en el carrito.
	o	Salir
