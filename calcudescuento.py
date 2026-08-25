print("=========================================")
print("=============CALCUDESCUENTO==============")
print ("========================================")

monto=float(input("Ingrese solamente el monto al cual se le aplicarà el decuento "))
descuento=float(input("Ingrese solamente el numero (sin el %) correspondiente al descuento "))
def calculopreciofinal():
     return monto*(1-(descuento/100))
   
print("el monto que debera abonar luego de que se aplicara el descuento sera de $ ", calculopreciofinal())
