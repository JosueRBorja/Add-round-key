# --- MATRICES DE EJEMPLO ---
state = [
    [0x32, 0x43, 0xf6],
    [0x88, 0x5a, 0x30],
    [0x31, 0x31, 0x98],
    [0xe0, 0x37, 0x07]
]

round_key = [
    [0x2b, 0x28, 0xab],
    [0x7e, 0xae, 0xf7],
    [0x15, 0xd2, 0x15],
    [0x16, 0xa6, 0x88]
]

# --- FUNCIÓN AddRoundKey ---
def addRoundKey(A, B):
    resultado = []
    for i in range(len(A)):        # recorrer filas
        fila = []
        for j in range(len(A[0])): # recorrer columnas
            # XOR entre cada elemento
            valor = A[i][j] ^ B[i][j]
            fila.append(valor)
        resultado.append(fila)
    return resultado

# --- EJECUCIÓN ---
resultado = addRoundKey(state, round_key)

# --- MOSTRAR RESULTADO ---
print("Resultado (AddRoundKey):")
for fila in resultado:
    print([hex(x) for x in fila])
