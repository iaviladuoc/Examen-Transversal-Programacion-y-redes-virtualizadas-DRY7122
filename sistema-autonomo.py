#Creamos una funcion para identificar el numero y clasificarlo si es privado o publico

def AS_PP(asn_ET2024):
    if 1 <= asn_ET2024 <= 64511:
        return "este número de AS es Público"
    elif 64512 <= asn_ET2024 <= 65534 or 4200000000 <= asn_ET2024 <= 4294967294:
        return "este número de AS es Privado"
    else:
        return "Número de sistema autónomo no es correcto, intentelo nuevamente"

# Ejemplo de uso
asn_ET2024 = int(input("Introduce un número de sistema autónomo (ASN): "))
print(f"El AS ingesado es: {asn_ET2024} y  {AS_PP(asn_ET2024)}.")

