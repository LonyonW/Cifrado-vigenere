import tkinter as tk
from tkinter import messagebox

class VigenereCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cifrado de Vigenère")
        self.root.geometry("500x400")

        # Alfabeto que se tiene en cuenta para el cifrado excluyendo la ñ
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.modT = len(self.alphabet)

        # Elementos de la UI
        self.label_key = tk.Label(root, text="Clave:")
        self.label_key.pack(pady=5)
        self.entry_key = tk.Entry(root)
        self.entry_key.pack(pady=5)

        self.label_text = tk.Label(root, text="Texto claro:")
        self.label_text.pack(pady=5)
        self.entry_text = tk.Entry(root)
        self.entry_text.pack(pady=5)

        self.encrypt_button = tk.Button(root, text="Cifrar", command=self.encrypt)
        self.encrypt_button.pack(pady=10)

        self.label_result = tk.Label(root, text="Texto cifrado:")
        self.label_result.pack(pady=5)
        self.result_text = tk.Text(root, height=3, width=40)
        self.result_text.pack(pady=5)

    def vigenere_encrypt(self, plaintext, key):
        # preparar el texto plano pasandolo a minusculas
        plaintext = plaintext.lower()
        key = key.lower()

        # preparar la clave para que coincida con la longitud del texto plano
        key_repeated = ''
        key_index = 0
        for char in plaintext:
            if char in self.alphabet:
                key_repeated += key[key_index % len(key)]
                key_index += 1
            else:
                key_repeated += char 

        # proceso de cifrado
        ciphertext = ''
        for p, k in zip(plaintext, key_repeated):
            if p in self.alphabet:
                # obtener el indice de la letra en el alfabeto
                p_index = self.alphabet.index(p)
                k_index = self.alphabet.index(k)
                # aplcar la formula vigenere: Yi = (Xi + Zi) mod T
                c_index = (p_index + k_index) % self.modT
                ciphertext += self.alphabet[c_index]
            else:
                ciphertext += p  # si no es una letra del alfabeto, se deja tal cual

        return ciphertext

    def encrypt(self):
        key = self.entry_key.get().strip()
        plaintext = self.entry_text.get().strip()

        # validacion de inputs
        if not key or not plaintext:
            messagebox.showerror("Error", "Por favor, ingrese tanto la clave como el texto claro.")
            return

        # validar la llave para que solo contenga letras del alfabeto definido anteriormente
        if not all(char in self.alphabet for char in key):
            messagebox.showerror("Error", "La clave solo debe contener letras del alfabeto (a-z).")
            return

        # cifrar el texto plano
        try:
            ciphertext = self.vigenere_encrypt(plaintext, key)
            # limpiar la interfaz
            self.result_text.delete(1.0, tk.END)
            # mostrar el resultado
            self.result_text.insert(tk.END, ciphertext)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cifrar: {str(e)}")

# correr la aplicacion
if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereCipherApp(root)
    root.mainloop()