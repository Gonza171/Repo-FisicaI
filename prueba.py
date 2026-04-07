import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Cargamos la clave secreta desde el archivo .env
load_dotenv()
clave_segura = os.getenv("GEMINI_API_KEY")

if not clave_segura:
    print("[Error] No se encontró la clave. Asegurate de haberla guardado en el archivo .env")
    exit()

# 2. Configuramos la conexión con la API de Google
genai.configure(api_key=clave_segura)

# 3. Preparamos a la IA con el rol específico de tu materia
modelo = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="Sos un profesor de Física I para estudiantes de Ingeniería de la UNS. Tu objetivo es ayudar a resolver problemas paso a paso. Explicá qué fórmulas usás, detallá los despejes matemáticos y asegurate de dar los resultados con sus unidades correspondientes en el Sistema Internacional."
)

print("\n==============================================")
print(" 🧠 ASISTENTE DE FÍSICA I (GEMINI)")
print("==============================================")
print("Escribí 'salir' para cerrar el programa.\n")

while True:
    pregunta = input("📝 Ingresá tu problema o duda de física:\n> ")
    
    if pregunta.lower() == 'salir':
        print("\n¡A seguir estudiando! Nos vemos.")
        break
        
    if pregunta.strip() == "":
        continue
        
    print("\n⏳ Calculando...\n")
    
    try:
        # Enviamos la pregunta a la IA
        respuesta = modelo.generate_content(pregunta)
        
        print("💡 RESOLUCIÓN:")
        print("-" * 50)
        print(respuesta.text)
        print("-" * 50 + "\n")
    except Exception as e:
        print(f"\n[Error] Hubo un problema de conexión: {e}\n")