import openai
import os
from dotenv import load_dotenv

# Configura tu API key de OpenAI creando el archivo .env con tu clave particular
load_dotenv()
openai.api_key = os.getenv("api_key")

def generate_readme(script_code) -> str:
    description_prompt: str = "Genera un archivo README a partir de un script en Python. Proporciona una descripción breve, indicación de uso y un ejemplo.\n\n"

    instructions: str = "## Uso\n\nReemplaza este texto con una descripción detallada de cómo usar este script. Incluye ejemplos de comandos y sus resultados.\n\n"

    example: str = "## Ejemplo\n\nReemplaza este texto con un ejemplo de cómo ejecutar este script y su resultado esperado.\n\n"

    prompt: str = description_prompt + instructions + example

    prompt += "```python\n" + script_code + "\n```"

    # Generamos el README utilizando la API de OpenAI
    response = openai.Completion.create(
        engine="davinci",  # Puedes ajustar el motor según disponibilidad
        prompt=prompt,
        max_tokens=500
    )

    # Extraemos el contenido del README generado
    generated_readme: str = response.choices[0].text.strip()  # type: ignore

    return generated_readme


if __name__ == "__main__":

    input_script = """
    import optparse
    parser: optparse.OptionParser = optparse.OptionParser('usage%prog -f' + '<code_file>')
    parser.add_option('-f', dest='code_file', type='string', help='especifica el archivo sobre el que se genera el readme')
    code_file: str = options.code_file
    """

    # Genera el README utilizando la función y el script proporcionado
    readme_content = generate_readme(input_script)

    # Escribe el contenido del README en un archivo
    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)

    print("README generado exitosamente como README.md")
