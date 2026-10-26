import os
import re

input_file = './chapters/1_theorical_framework.tex'
output_dir = './chapters/1_theorical_framework'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

sections = [
    ('01_introduccion', 'Introducción'),
    ('02_vision_artificial', 'Inteligencia Artificial'),
    ('03_deep_learning', 'Fundamentos de Aprendizaje Automático y Aprendizaje Profundo'),
    ('04_object_detection', 'Detección de Objetos mediante Aprendizaje Profundo'),
    ('05_percepcion_vehicular', 'Percepción Vehicular y Reconocimiento de Matrículas'),
    ('06_seguimiento_vehicular', 'Seguimiento Vehicular y Determinación de Eventos'),
    ('07_evaluacion_optimizacion', 'Evaluación y Optimización de Modelos de Visión Artificial')
]

master_content = "\\chapter{Marco Teórico}\n\n"
current_idx = -1
current_buffer = []

for line in lines:
    if line.strip().startswith('\\chapter{'):
        continue
    
    if line.strip().startswith('\\section{'):
        if current_idx != -1:
            out_path = os.path.join(output_dir, f"{sections[current_idx][0]}.tex")
            with open(out_path, 'w', encoding='utf-8') as out_f:
                out_f.writelines(current_buffer)
        
        current_idx += 1
        current_buffer = [line]
        master_content += f"\\input{{chapters/1_theorical_framework/{sections[current_idx][0]}}}\n"
    elif current_idx != -1:
        current_buffer.append(line)

if current_idx != -1:
    out_path = os.path.join(output_dir, f"{sections[current_idx][0]}.tex")
    with open(out_path, 'w', encoding='utf-8') as out_f:
        out_f.writelines(current_buffer)

with open(input_file, 'w', encoding='utf-8') as f:
    f.write(master_content)

print("Done")
