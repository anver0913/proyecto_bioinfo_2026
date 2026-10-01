# taller1_2026

Converted from: taller1_2026.docx

---

## File Information

- **File Name**: taller1_2026.docx
- **File Size**: 171.68 KB
- **Modified Date**: 10/1/2026, 2:13:59 PM

## Content

## ## Content

**Taller 1 Bioinformática Aplicada**

**ICQ451**

Inspeccione los archivos proporcionados por el profesor a través de Campus Virtual, y responda a las siguientes preguntas adjuntando para cada una de ellas, imágenes correspondientes habiendo utilizado los servidores y software vistos en clase.

*Suba sus archivos y respuestas a su repo de GitHub la cual será previamente compartida con **herbert.venthur@ufrontera.cl**. Sus respuestas DEBEN estar en formato “markdown (.md)” con los aspectos señalados en clase dando énfasis a sus oraciones y conceptos asociados. Para el resto de archivos SOLO se aceptará .fasta, .png, .pdf y .txt *

****Separé muy bien lo que son archivos de este taller, tanto la data como sus resultados, de otros ficheros asociados a clases prácticas anteriores y que no tienen que ver con este taller.***

***Preguntas:***

1. ¿Cuántos dominios estructurales (o regiones) conservadas, con más de 3 amino ácidos, existen en las aldehído oxidasas proporcionadas “LbotAOX1, EsemAOX1, CmedAOX1 y SinfAOX1?

Se identificaron 21 regiones conservadas independientes que cuentan con una longitud estrictamente mayor a 3 aminoácidos compartidas exactamente entre las cuatro secuencias analizadas (LbotAOX1, SinfAOX1, CmedAOX1 y EsemAOX1)-

1. Fuente de datos: Se extrajeron las secuencias correspondientes al archivo pre-alineado AOXs_all.fasta para garantizar la alineación estructural por posiciones y evitar desfasajes por inserciones/deleciones (gaps).

2. Filtrado: Se seleccionaron únicamente las 4 secuencias requeridas: LbotAOX1, SinfAOX1, CmedAOX1 y EsemAOX1.

3. Procesamiento: Se desarrolló un script en Python utilizando la librería Biopython (Bio.AlignIO), el cual analizó columna por columna el alineamiento múltiple para evaluar la conservación idéntica absoluta (100% de identidad sin brechas) agrupando bloques continuos con longitud mayor a 3 aminoácidos.

1. ¿Cuál es el clado evolutivamente más distante entre las secuencias analizadas y el general de clados conformados? Justifique su respuesta.

El clado evolutivamente más distante entre las secuencias analizadas es el de las xantina deshidrogenasas (XDH), representado por MrotXDH, CcapXDH, CvicXDH, DpleXDH y BmorXDH. Dentro de las AOX, el clado más distante sería el de Lepidoptera (CmedAOX1, SinfAOX1, OfurAOX2), que se separa antes que el resto de AOX en el árbol. Sin embargo, el clado más distante de todos sigue siendo el de las XDH.

En el árbol filogenético construido con FastTree (Maximum Likelihood, modelo LG, bootstrap 100), este clado se separa en la rama más basal desde la raíz, antes de la diversificación de todas las aldehído oxidasas (AOX) de insectos. La rama que conecta este clado con el resto del árbol es la más larga, lo que indica una mayor distancia evolutiva. Los valores de bootstrap en los nodos internos de este clado son muy altos (nodos rojos grandes, cercanos a 1), confirmando que forman un grupo monofilético bien definido. Esto indica que las XDH divergieron tempranamente de las AOX, compartiendo un ancestro común más antiguo.

Clados conformados:

- XDH (outgroup): MrotXDH, CcapXDH, CvicXDH, DpleXDH, BmorXDH — rama más basal
- Diptera: AaegAOX, AgamAOX, CquiAOX, EsemAOX1, DmelAOX1-4 — bootstrap alto (nodos rojos)
- Lepidoptera: CmedAOX1-4, LbotAOX1-4, OfurAOX2, OfurAOX6, CpomAOX1-2, SinfAOX1-3 — bootstrap alto (nodos rojos)

1. Describa qué herramientas bioinformáticas utilizó para analizar y responder a las preguntas anteriores y para qué las utilizó.

Para la Pregunta 1 (regiones conservadas):

- ClustalW (ejecutado en Ubuntu/WSL): se usó para realizar el alineamiento múltiple de secuencias (MSA) de todas las AOX y XDH, generando el archivo AOXs_aa.fasta. Este alineamiento garantiza que las secuencias estén alineadas por posiciones equivalentes, evitando desfasajes por inserciones/deleciones (gaps).
- Python 3 + Biopython (en VS Code): se desarrolló un script (analizar.py) que analizó columna por columna el alineamiento múltiple para evaluar la conservación idéntica absoluta (100% de identidad sin gaps) entre las 4 secuencias (LbotAOX1, SinfAOX1, CmedAOX1, EsemAOX1), agrupó bloques continuos conservados y filtró aquellos con longitud mayor a 3 aminoácidos. El resultado fue 21 regiones conservadas.
- VS Code: se usó como editor de código para escribir el script analizar.py y como terminal integrada para ejecutarlo (python analizar.py).

Para la Pregunta 2:

- Ubuntu (WSL) + Terminal: entorno principal donde se ejecutaron todos los comandos de manipulación de archivos FASTA, alineamiento y filogenia.
- ClustalW (ejecutado en Ubuntu/WSL): se usó para realizar el alineamiento múltiple de secuencias (MSA) de todas las AOX y XDH, generando el archivo AOX_alineado.fasta. Este alineamiento fue la base para construir el árbol filogenético.
- MEGA 11 (Windows): se usó para calcular el mejor modelo de sustitución (LG+G+I, BIC = 86154.350) mediante Find Best DNA/Protein Models (ML), el cual sirvió como referencia para FastTree.
- FastTree (ejecutado en Ubuntu/WSL): se usó para construir el árbol filogenético por Maximum Likelihood con modelo LG automático para proteínas y bootstrap de 100 réplicas, generando el archivo AOX_tree.nwk. Fue la herramienta principal para responder la Pregunta 2.
- FigTree (Windows): se usó para visualizar el árbol filogenético, colorear los clados (XDH rosa, Diptera verde, Lepidoptera naranjo), escalar los nodos según bootstrap y exportar la imagen final. Fue clave para identificar visualmente el clado más distante (XDH).