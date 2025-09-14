class Producto:
    def __init__(self, nombre, ISBN, precio, stock, categoria):
        self.nombre = nombre
        self.ISBN = ISBN
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self):
        return f"Producto: {self.nombre} - ISBN: {self.ISBN} - Precio: {self.precio} - Stock: {self.stock} - Categoria: {self.categoria}"

class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def __str__(self):
        return f"Nombre {self.nombre} - Email: {self.email}"

class Compra:
    def __init__(self, cliente, producto, cantidad):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad

    def __str__(self):
        return f"Compra: {self.cliente.nombre} - Producto: {self.producto.nombre} - Cantidad: {self.cantidad}"
    
class TiendaOnline:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.clientes = []
        self.compras = []
    
    def agregar_producto(self, nombre, ISBN, precio, stock, categoria):
        oProducto = Producto(nombre, ISBN, precio, stock, categoria)
        self.productos.append(oProducto)
        print("Producto agregado exitosamente.")
    
    def registrar_cliente(self, nombre, email):
        oCliente = Cliente(nombre, email)
        self.clientes.append(oCliente)
        print("Cliente registrado exitosamente.")
    
    def hacer_compra(self, email, ISBN, cantidad):
        cliente = next((c for c in self.clientes if c.email == email),None)
        if not cliente:
            return "Cliente no encontrado. Por favor registre al cliente primero."
        
        producto = next((p for p in self.productos if p.ISBN == ISBN),None)
        if not producto:
            return "Producto no encontrado. Registre el producto primero."
        
        if producto.stock < cantidad:
            return "Stock insuficiente para completar la compra."
        producto.stock -= cantidad
        oCompra = Compra(cliente, producto, cantidad)
        self.compras.append(oCompra)
        return "Compra realizada exitosamente."
    
    def listar_productos(self):
        for producto in self.productos:
            print(producto)
    
    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)
    
    def listar_compras(self):
        for compra in self.compras:
            print(compra)

tiendaOnline = TiendaOnline("Mi Tienda")
tiendaOnline.agregar_producto("Libro A", "123-456", 29.99, 10, "Libros")
tiendaOnline.agregar_producto("Libro Geometris", "789-101", 39.99, 5, "Libros")
tiendaOnline.agregar_producto("Juego CallOFDuty", "112-131", 59.99, 3, "Juegos")
tiendaOnline.agregar_producto("Kit Tazas", "415-161", 49.99, 7, "Juegos")
tiendaOnline.agregar_producto("Peluche Gorilla", "718-192", 19.99, 15, "Peliculas")
tiendaOnline.agregar_producto("Poster Volver al Futuro", "021-222", 24.99, 8, "Peliculas")
tiendaOnline.agregar_producto("iMac 16''", "324-252", 14.99, 20, "Musica")
tiendaOnline.registrar_cliente("Juan Perez","jperez@dominio.com")
tiendaOnline.registrar_cliente("Ana Gomez","ana@dominio.com")
tiendaOnline.registrar_cliente("Luis Martinez","luis@dominio.com")
print(tiendaOnline.hacer_compra("jperez@dominio.com", "123-456", 2))
print(tiendaOnline.hacer_compra("ana@dominio.com","021-222",1))
print(tiendaOnline.hacer_compra("luis@dominio.com","021-222",18))
print(tiendaOnline.hacer_compra("usuario@dominio.com.mx","324-252",2))
tiendaOnline.listar_productos()
tiendaOnline.listar_clientes()
tiendaOnline.listar_compras()