from django.http import HttpResponse
from django.shortcuts import render

from controlmateriales.models import *

# Create your views here.

def reiniciar(request):
    matfenix.objects.all().delete()
    matperseo.objects.all().delete()
    faltanteperseo.objects.all().delete()
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")

def pedidos_fenix(request):
    perseo = matperseo.objects.all()
    fenix = matfenix.objects.all()
    pedidos_fenix=[]
    no=[]
    cont=0
    cont2=0
    for p in fenix:
        try:
            ped_f=matperseo.objects.get(pedido=p.pedido)
            if ped_f.pedido in pedidos_fenix:
                pass
            else:
                pedidos_fenix.append(ped_f.pedido)
                cont+=1
        except:
            if p.pedido in no:
                pass
            else:
                no.append(p.pedido)
                cont2+=1
    print("pedidos que no estan en perseo: " + str(len(no)))

    return HttpResponse("termino") #(request, 'index.html')

def concatenar(pedidos, indicador):
    con=1
    for p in pedidos:
        if indicador==1:
            try:
                nombre_cambio_codigo = Guia.objects.get(nombre_perseo=p.codigo)
                p.codigo = nombre_cambio_codigo.nombre_fenix
                p.save()

            except:
                pass
        my_str=p.codigo

        try:
            final_str=my_str[-1]
            if final_str=='A':
                p.codigo= str(my_str[:-1])
        except:
            pass
       
        
        p.concatenacion = str(p.pedido + "-" + p.codigo)
        p.save()

def gestionarbd(request):
    pedidos_perseo = matperseo.objects.all()
    pedidos_fenix = matfenix.objects.all()

    concatenar(pedidos_fenix, 0)
    concatenar(pedidos_perseo, 1)

    return render(request, "index.html")

def calculo_faltantes_fenix(request):
    faltantes=[]
    pedidos_perseo = matperseo.objects.all()
    cont=0
    for pedido_perseo in pedidos_perseo:
        
        try:
            pedido_fenix = matfenix.objects.get(concatenacion=pedido_perseo.concatenacion)

            try:
                existe_faltante = faltanteperseo.objects.get(concatenacion = pedido_fenix.concatenacion)
                existe_faltante.cantidad= existe_faltante.cantidad + pedido_perseo.cantidad
                existe_faltante.diferencia = existe_faltante.cantidad - pedido_fenix.cantidad
                existe_faltante.save()

            except:
                if pedido_perseo.cantidad != pedido_fenix.cantidad:
                    faltante= faltanteperseo()
                    faltante.concatenacion = pedido_perseo.concatenacion
                    faltante.pedido = pedido_perseo.pedido
                    faltante.actividad = pedido_perseo.actividad
                    faltante.fecha = pedido_perseo.fecha
                    faltante.codigo = pedido_perseo.codigo
                    faltante.cantidad = pedido_perseo.cantidad
                    faltante.observacion = "Cantidad no coincide"
                    faltante.acta = pedido_perseo.acta
                    faltante.cantidad_fenix = pedido_fenix.cantidad
                    faltante.diferencia = pedido_perseo.cantidad - pedido_fenix.cantidad
                    faltante.save()        
        except:
            falt= faltanteperseo()
            falt.concatenacion = pedido_perseo.concatenacion
            falt.pedido = pedido_perseo.pedido
            falt.actividad = pedido_perseo.actividad
            falt.fecha = pedido_perseo.fecha
            falt.codigo = pedido_perseo.codigo
            falt.cantidad = pedido_perseo.cantidad
            falt.observacion = "No digitado en fenix"
            falt.acta = pedido_perseo.acta
            falt.diferencia = -9999
            falt.save()

        ped= faltanteperseo.objects.filter(diferencia=0)
        ped.delete()

    calculo_numero_acta()


    return render(request, "index.html")

def calculo_numero_acta():
    acta= Acta.objects.first()
    pedidos_perseo = matperseo.objects.all()
    con=1
 
    for pedido_perseo in pedidos_perseo:
        try:
            if str(pedido_perseo.acta) != str(acta.numero):
                faltante= faltanteperseo()
                faltante.concatenacion = pedido_perseo.concatenacion
                faltante.pedido = pedido_perseo.pedido
                faltante.actividad = pedido_perseo.actividad
                faltante.fecha = pedido_perseo.fecha
                faltante.codigo = pedido_perseo.codigo
                faltante.cantidad = pedido_perseo.cantidad
                faltante.observacion = "Acta incorrecta"
                faltante.acta = pedido_perseo.acta
                faltante.diferencia = -9999
                faltante.save()                        
        except:
            print("error en el acta")





    

