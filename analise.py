import subprocess
from sys import argv, exit


def extracao_cdi():
    
    subprocess.run(['python', 'extracao.py'], check=True)

def visualizacao(output_image):
    
    subprocess.run(['python', 'visualizacao.py', output_image], check=True)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Uso: python analise.py <grafico>")
        exit(1)

    output_image = f"{argv[1]}"

    extracao_cdi()
    visualizacao(output_image)