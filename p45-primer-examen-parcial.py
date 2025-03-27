#Inscripcion a evento académico
import os
dia=0
while(True):
    os.system('cls')

    print('Universidad Patito SA de CV')
    print('Sistema de inscripcion congreso de sistemas')

    u=int(input('Tipo de usuario:[1] Alumno $100, [2]Trabajador $200, [3]Docente $500'))
    p=int(input('Tipo de paquete:[1]Solo conferencias $600, [2]Con eventos sociales $800, [3]Con kit $900'))
    c=int(input('Cantidad de boletos: '))
    s=0
    t=0

    if u==1 and p==1:
        e=100
        con=600
        n=e+con
        s=n*c
        da=s*(0.20)
        print(f'Tu pedido fue: tipo alumno, con solo conferencias y {c} boletos')
        if s>5000:
            t=s-da
            print(f'Subtotal: {s} con un descuento de: {da} y un total de {t}')
            dia+=t

        else:
            t=s
            print(f'Da un total de {t}')
            dia+=t

    elif u==2 and p==1:
        e=200
        con=600
        n=e+con
        s=n*c
        dt=s*(0.10)
        print(f'Tu pedido fue: tipo trabajador, con solo conferencias y {c} boletos')
        if s>=5000:
            t=s-dt
            print(f'Subtotal: {s} con un descuento de: {dt} y un total de {t}')
            dia+=t

        else:
            t=s
            print(f'Da un total de {t}')
            dia+=t

        
    elif u==3 and p==1:
        e=500
        con=600
        n=e+con
        s=n*c
        dd=s*(0.05)
       
        print(f'Tu pedido fue: tipo docente, con solo conferencias y {c} boletos')
        if s>=5000:
            t=s-dd
            print(f'Subtotal: {s} con un descuento de: {dd} y un total de {t}')
            dia+=t

        else:
            t=s
        print(f'Da un total de {t}')  
        dia+=t

    elif u==1 and p==2:
        e=100
        con=800
        n=e+con
        s=n*c
        da=s*(0.20)
        
        print(f'Tu pedido fue: tipo alumno, con evento y {c} boletos')
        if s>=5000:
            t=s-da
            print(f'Subtotal: {s} con un descuento de: {da} y un total de {t}')
            dia+=t

        else:
            t=s
            print(f'Da un total de {t}')
            dia+=t
    elif u==2 and p==2:
        e=200
        con=800
        n=e+con
        s=n*c
        dt=s*(0.10)
        
        print(f'Tu pedido fue: tipo trabajador, con evento y {c} boletos')
        if s>=5000:
            t=s-dt
            print(f'Subtotal: {s} con un descuento de: {dt} y un total de {t}')
            dia+=t
        else:
            t=s
            print(f'Da un total de {t}')
            dia+=t
        
    elif u==3 and p==2:
        e=500
        con=800
        n=e+con
        s=n*c
        dd=s*(0.05)
        
        print(f'Tu pedido fue: tipo docente, con evento y {c} boletos')
        if s>=5000:
            t=s-dd
            print(f'Subtotal: {s} con un descuento de: {dd} y un total de {t}')
            dia+=t
        else:
            t=s
            print(f'Da un total de {t}')
            dia+=t
    elif u==1 and p==3:
        e=100
        con=900
        n=e+con
        s=n*c
        da=s*(0.20)
        
        print(f'Tu pedido fue: tipo alumno, con kit y {c} boletos')
        if s>=5000:
            t=s-da
            print(f'Subtotal: {s} con un descuento de: {da} y un total de {t}')
            dia+=t
        else:
            t=s
            print(f'Da un total de {t}')
            dia+=t
    elif u==2 and p==3:
        e=200
        con=900
        n=e+con
        s=n*c
        dt=s*(0.10)
        
        print(f'Tu pedido fue: tipo trabajador, con kit y {c} boletos')
        if s>=5000:
            t=s-dt
            print(f'Subtotal: {s} con un descuento de: {dt} y un total de {t}')
            dia+=t
        else:
            t=s
            print(f'Da un total de {t}')
            dia+=t
        
    elif u==3 and p==3:
        e=500
        con=900
        n=e+con
        s=n*c
        dd=s*(0.05)

        print(f'Tu pedido fue: tipo docente, con kit y {c} boletos')
        if s>=5000:
            t=s-dd
            print(f'Subtotal: {s} con un descuento de: {dd} y un total de {t}')
            dia+=t
        else:
            t=s
            print(f'Da un total de {t}')
            dia+=t
    if input('Deseas continuar (S/N)').upper()=='N':break
print(f'Importe total de la venta: {dia}')
print('Proceso terminado')
      