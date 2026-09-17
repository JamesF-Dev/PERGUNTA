import tkinter as tk
from tkinter import messagebox
import logging
import sys

# =========================
# Configuração de Logs
# =========================
def configurar_logs():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("sistema_gui.log")
        ]
    )