import time

Name=(str(input("Ingrese su nombre: ")));
Age=(int(input("Ingrese su año de nacimiento: ")));
año=2022-Age;
if (año>=18):
    VentaPrim=float(input("Ingrese la ventas del primer semestre del año 2021: "));
    VentaSeg=float(input("Ingrese la venta del segundo bimestre del año 2021: "));
    total=float(VentaPrim+VentaSeg);

    if VentaPrim>VentaSeg:
        mejo1="1ro";
    else:
        mejo1 = "2do";

    if total<=100000:
        medalla="Bronce";
        Premio="Un dia libre para el vendedor";
    elif total<=500000:
        medalla = "Plata";
        Premio = "Un dia libre con un bono de Q250";
    elif total<=1000000:
        medalla = "Oro";
        Premio = "Un dia libre con un bono de Q500";
    else:
        medalla = "Diamante";
        Premio = "Dos dia libre con un bono de Q1000";
    print("Vendedor:",Name);
    print("Ventas anuales:Q",total);
    print("Mejor semestre:",mejo1);
    print("Medalla acreditada:",medalla);
    print("Premio:",Premio);
else:
    print(Name,"lo siento muchisimo pero es menor de edad")
time.sleep(10)
