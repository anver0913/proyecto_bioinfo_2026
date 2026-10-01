from Bio import AlignIO

# 1. Leer el archivo YA ALINEADO
archivo_alineado = "AOXs_all.fasta"
alignment = AlignIO.read(archivo_alineado, "fasta")

# 2. Filtrar solo las 4 secuencias de interés
objetivos = ["LbotAOX1", "EsemAOX1", "CmedAOX1", "SinfAOX1"]
records = [seq for seq in alignment if seq.id in objetivos]

print(f"=== ANÁLISIS DESDE ALINEAMIENTO MÚLTIPLE ({archivo_alineado}) ===")
print(f"Secuencias analizadas: {[r.id for r in records]}\n")

largo_alineamiento = len(records[0].seq)

bloques_conservados = []
bloque_actual = ""
pos_inicio = 0

for i in range(largo_alineamiento):
    # Obtener el aminoácido de cada secuencia en la columna i
    columna = [r.seq[i] for r in records]
    
    # Si todos son idénticos y no son un gap '-'
    if len(set(columna)) == 1 and columna[0] != '-':
        if not bloque_actual:
            pos_inicio = i + 1
        bloque_actual += columna[0]
    else:
        if len(bloque_actual) > 3:  # Criterio: más de 3 aminoácidos
            bloques_conservados.append((pos_inicio, bloque_actual))
        bloque_actual = ""

if len(bloque_actual) > 3:
    bloques_conservados.append((pos_inicio, bloque_actual))

print(f"Total de regiones conservadas (>3 aa): {len(bloques_conservados)}\n")

for idx, (pos, seq_cons) in enumerate(bloques_conservados, 1):
    print(f"Región {idx}: Posición alineada {pos} | Longitud: {len(seq_cons)} aa | Secuencia: {seq_cons}")