tabela = {
    'km':   {'m': 1000, 'dm': 10000, 'cm': 100000, 'mm': 1_000_000, 'μm': 1e9, 'nm': 1e12},
    'm':    {'km': 1/1000, 'dm': 10, 'cm': 100, 'mm': 1000, 'μm': 1e6, 'nm': 1e9},
    'dm':   {'km': 0.0001, 'm': 0.1, 'cm': 10, 'mm': 100, 'μm': 100_000, 'nm': 1e8},
    'cm':   {'km': 1/100_000, 'm': 0.01, 'dm': 0.1, 'mm': 10, 'μm': 10_000, 'nm': 1e7},
    'mm':   {'km': 1/1_000_000, 'm': 0.001, 'dm': 0.01, 'cm': 0.1, 'μm': 1000, 'nm': 1e6},
    'μm':   {'km': 1e-9, 'm': 1e-6, 'dm': 1e-5, 'cm': 0.0001, 'mm': 0.001, 'nm': 1000},
    'nm':   {'km': 1e-12, 'm': 1e-9, 'dm': 1e-8, 'cm': 1e-7, 'mm': 1e-6, 'μm': 0.001},

    'mi': {'km': 1.60934, 'm': 1609.34, 'cm': 160934, 'mm': 1_609_340, 'yd': 1760, 'ft': 5280, 'in': 63360},
    'yd': {'km': 0.0009144, 'm': 0.9144, 'cm': 91.44, 'mm': 914.4, 'mi': 1/1760, 'ft': 3, 'in': 36},
    'ft': {'km': 0.0003048, 'm': 0.3048, 'cm': 30.48, 'mm': 304.8, 'mi': 1/5280, 'yd': 1/3, 'in': 12},
    'in': {'km': 0.0000254, 'm': 0.0254, 'cm': 2.54, 'mm': 25.4, 'mi': 1/63360, 'yd': 1/36, 'ft': 1/12}
}

tabela_peso = {
    't':   {'kg': 1000, 'g': 1_000_000, 'mg': 1_000_000_000},
    'kg':  {'t': 1/1000, 'g': 1000, 'mg': 1_000_000},
    'g':   {'t': 1/1_000_000, 'kg': 1/1000, 'mg': 1000},
    'mg':  {'t': 1/1_000_000_000, 'kg': 1/1_000_000, 'g': 1/1000},
}

def converter_comprimento(valor, de, para):
    if de == para:
        return valor
    try:
        return valor * tabela[de][para]
    except KeyError:
        raise ValueError("Conversão inválida.")

def para_celsius(valor, de):
    if de == 'C':
        return valor
    elif de == 'K':
        return valor - 273.15
    elif de == 'F':
        return (valor - 32) / 1.8
    raise ValueError("Unidade inválida")

def de_celsius(valor, para):
    if para == 'C':
        return valor
    elif para == 'K':
        return valor + 273.15
    elif para == 'F':
        return valor * 1.8 + 32
    raise ValueError("Unidade inválida")

def converter_temperatura(valor, de, para):
    if de == para:
        return valor
    celsius = para_celsius(valor, de)
    return de_celsius(celsius, para)

def converter_peso(valor, de, para):
    de = de.strip().lower()
    para = para.strip().lower()
    if de == para:
        return valor
    try:
        return valor * tabela_peso[de][para]
    except KeyError:
        raise ValueError("Conversão inválida.")
    

def valida_float(valor):
    try:
        valor = float(valor)
    except:
        return "Insira um valor válido"
    else:
        return valor
