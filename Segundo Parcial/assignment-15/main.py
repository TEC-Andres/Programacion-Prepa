'''
#       Sesión 15: Sistema de admnistración de cuentas de gastos
#       Andrés Rodríguez Cantú ─ A01287002
#       
#       Copyright (C) Tecnológico de Monterrey
#
#       Archivo: main.py
#
#       Creado:                   30/03/2025
#       Última Modificación:      30/03/2025
'''

# =============================================================================
# Prompt
# Hazme una aplicación de python usando tkinter con una UI moderna que haga las siguientes cosas. Asegurate de usar una estructura clara y moderna para una app full-stack.
# 
# Objetivo: Administrar mi cuenta de gastos de tal manera que pueda registrar los movimientos tanto de entrada como de salida y obtener reportes de gastos.
# 
# 
# Funcionalidades:
# 1. Registrar una cuenta de gastos
# 2. Registrar categorías de gastos
# 3. Registrar un gasto
# 4. Registrar un ingreso
# 5. Modificar un gasto o un ingreso
# 6. Obtener el saldo actual
# 7. Obtener reporte de gastos por categoría
# 8. Obtener reporte de gastos por un rango de fecha
# 9. Obtener gráfico de gastos por categoría
# 10. Obtener gráfico de gastos por rango de fecha
# Datos:
# Cuentas
# ID Cuenta
# Nombre de la cuenta
# Cuenta
# Banco
# Saldo
# Categorías
# ID Categoría
# Nombre de la Categoría
# Categoria
# Tipo (Ingreso / Gasto)
#  
# 
# Registro
# 
# ID Registro
# ID Cuenta
# ID Categoría
# Fecha
# Valor
# Ingreso/Gasto
# 
# Algoritmo:
# 0. Iniciar la aplicación
# 0.1 Mostrar el menú de opciones
# 0.2 Leer datos de cuentas
# 0.3 Leer datos de categorías
# 0.4 Leer datos de gastos
# 1. Registrar una cuenta de gastos
# 1.1 Solicitar el nombre de la cuenta
# 1.1.1 Validar que el nombre de la cuenta no esté vacío
# 1.1.2 Validar que el nombre de la cuenta no exista
# 1.2 Solicitar el saldo inicial
# 1.2.1 Validar que el saldo inicial sea un número
# 1.2.2 Validar que el saldo inicial sea mayor o igual a cero
# 1.3 Confirmar el registro de la cuenta
# 1.4 Registrar la cuenta
# 2. Registrar un gasto 
# 2.1 Solicitar la cuenta de gastos 
# 2.2 Solicitar la categoría del gasto 
# 2.3 Solicitar la fecha del gasto 
# 2.4 Solicitar el monto del gasto 
# 2.5 Confirmar el registro del gasto 
# 2.6 Registrar el gasto 
# 3. Editar
# 3.1 Solicitud de edición
# 3.2 Solicitud de edición de datos de cuenta
# 3.2.1 Cambio de nombre
# 3.2.2 Cambio de apellido
# 3.2.3 Cambio de ID del usuario
# 3.3 Solicitud de edición de historial
# 3.3.1 Eliminar Historial
# 3.3.2 Agregar contenido al historial
# 3.3.3 Editar información del historial
# 3.3.4 Editar la descripción de la acción.
# ==============================================================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sqlite3
import matplotlib.pyplot as plt
import os

DB_NAME = os.path.join(os.path.dirname(__file__), 'expenses.db')

# =============================================================================
# Clase para manejar la base de datos (backend)
# =============================================================================
class DBManager:
    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        # Tabla de cuentas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                account TEXT,
                bank TEXT,
                balance REAL CHECK(balance >= 0)
            )
        ''')
        # Tabla de categorías
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                type TEXT CHECK(type IN ('Ingreso', 'Gasto'))
            )
        ''')
        # Tabla de registros (gastos/ingresos)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER,
                category_id INTEGER,
                date TEXT,
                amount REAL,
                type TEXT CHECK(type IN ('Ingreso', 'Gasto')),
                FOREIGN KEY(account_id) REFERENCES accounts(id),
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        ''')
        self.conn.commit()

    # Métodos para cuentas
    def add_account(self, name, initial_balance):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", (name, initial_balance))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(e)
            return False

    def get_accounts(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, balance FROM accounts")
        return cursor.fetchall()

    def update_account_balance(self, account_id, new_balance):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (new_balance, account_id))
        self.conn.commit()

    # Métodos para categorías
    def add_category(self, name, category, type_):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO categories (name, category, type) VALUES (?, ?, ?)",
                           (name, category, type_))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(e)
            return False

    def get_categories(self, type_=None):
        cursor = self.conn.cursor()
        if type_:
            cursor.execute("SELECT id, name FROM categories WHERE type=?", (type_,))
        else:
            cursor.execute("SELECT id, name FROM categories")
        return cursor.fetchall()

    # Métodos para registros
    def add_record(self, account_id, category_id, date, amount, type_):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO records (account_id, category_id, date, amount, type) VALUES (?, ?, ?, ?, ?)",
                       (account_id, category_id, date, amount, type_))
        # Actualizar el saldo de la cuenta
        cursor.execute("SELECT balance FROM accounts WHERE id=?", (account_id,))
        current_balance = cursor.fetchone()[0]
        if type_ == 'Ingreso':
            new_balance = current_balance + amount
        else:
            new_balance = current_balance - amount
        cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (new_balance, account_id))
        self.conn.commit()

    def get_records(self, account_id=None):
        cursor = self.conn.cursor()
        if account_id:
            cursor.execute("SELECT * FROM records WHERE account_id=?", (account_id,))
        else:
            cursor.execute("SELECT * FROM records")
        return cursor.fetchall()

    def update_record(self, record_id, new_account_id, new_category_id, new_date, new_amount, new_type):
        cursor = self.conn.cursor()
        # Para simplificar, se ignora el ajuste de saldo anterior y se recalcula la diferencia
        cursor.execute("SELECT account_id, amount, type FROM records WHERE id=?", (record_id,))
        old = cursor.fetchone()
        if not old:
            return False
        old_account_id, old_amount, old_type = old
        # Revertir el efecto en el saldo de la cuenta original
        cursor.execute("SELECT balance FROM accounts WHERE id=?", (old_account_id,))
        current_balance = cursor.fetchone()[0]
        if old_type == 'Ingreso':
            current_balance -= old_amount
        else:
            current_balance += old_amount
        cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (current_balance, old_account_id))
        # Actualizar registro
        cursor.execute('''
            UPDATE records 
            SET account_id=?, category_id=?, date=?, amount=?, type=? 
            WHERE id=?
        ''', (new_account_id, new_category_id, new_date, new_amount, new_type, record_id))
        # Aplicar efecto del nuevo registro
        cursor.execute("SELECT balance FROM accounts WHERE id=?", (new_account_id,))
        new_balance = cursor.fetchone()[0]
        if new_type == 'Ingreso':
            new_balance += new_amount
        else:
            new_balance -= new_amount
        cursor.execute("UPDATE accounts SET balance=? WHERE id=?", (new_balance, new_account_id))
        self.conn.commit()
        return True

    def get_current_balance(self, account_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE id=?", (account_id,))
        return cursor.fetchone()[0]

    def get_expenses_by_category(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT c.name, SUM(r.amount) 
            FROM records r 
            JOIN categories c ON r.category_id = c.id 
            WHERE r.type = 'Gasto'
            GROUP BY c.name
        ''')
        return cursor.fetchall()

    def get_expenses_by_date_range(self, start_date, end_date):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM records 
            WHERE date BETWEEN ? AND ? AND type='Gasto'
        ''', (start_date, end_date))
        return cursor.fetchall()


# =============================================================================
# Clase principal de la aplicación
# =============================================================================
class ExpenseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Administrador de Gastos")
        self.geometry("800x600")
        self.db = DBManager()

        # Configurar estilo moderno
        style = ttk.Style(self)
        style.theme_use('clam')

        # Crear contenedor principal (usamos un Notebook para separar secciones)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Pestañas
        self.create_account_tab()
        self.create_category_tab()
        self.create_record_tab()
        self.create_reports_tab()

    # Pestaña para administrar cuentas
    def create_account_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Cuentas")

        lbl_title = ttk.Label(frame, text="Registrar Cuenta de Gastos", font=('Arial', 16))
        lbl_title.pack(pady=10)

        frm = ttk.Frame(frame)
        frm.pack(pady=10)

        ttk.Label(frm, text="Nombre de la cuenta:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.entry_account_name = ttk.Entry(frm)
        self.entry_account_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Saldo Inicial:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.entry_initial_balance = ttk.Entry(frm)
        self.entry_initial_balance.grid(row=1, column=1, padx=5, pady=5)

        btn_add = ttk.Button(frm, text="Registrar Cuenta", command=self.add_account)
        btn_add.grid(row=2, column=0, columnspan=2, pady=10)

        self.lbl_account_msg = ttk.Label(frame, text="", foreground="red")
        self.lbl_account_msg.pack()

    def add_account(self):
        name = self.entry_account_name.get().strip()
        try:
            balance = float(self.entry_initial_balance.get().strip())
        except ValueError:
            self.lbl_account_msg.config(text="El saldo inicial debe ser un número.")
            return

        if not name:
            self.lbl_account_msg.config(text="El nombre de la cuenta no puede estar vacío.")
            return

        if balance < 0:
            self.lbl_account_msg.config(text="El saldo inicial debe ser mayor o igual a cero.")
            return

        if self.db.add_account(name, balance):
            self.lbl_account_msg.config(text="Cuenta registrada exitosamente.", foreground="green")
            self.entry_account_name.delete(0, tk.END)
            self.entry_initial_balance.delete(0, tk.END)
        else:
            self.lbl_account_msg.config(text="La cuenta ya existe o error en el registro.")

    # Pestaña para administrar categorías
    def create_category_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Categorías")

        lbl_title = ttk.Label(frame, text="Registrar Categoría", font=('Arial', 16))
        lbl_title.pack(pady=10)

        frm = ttk.Frame(frame)
        frm.pack(pady=10)

        ttk.Label(frm, text="Nombre de la Categoría:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.entry_category_name = ttk.Entry(frm)
        self.entry_category_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Categoría (descripción):").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.entry_category_desc = ttk.Entry(frm)
        self.entry_category_desc.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frm, text="Tipo:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.cmb_category_type = ttk.Combobox(frm, values=["Ingreso", "Gasto"], state="readonly")
        self.cmb_category_type.grid(row=2, column=1, padx=5, pady=5)
        self.cmb_category_type.current(0)

        btn_add = ttk.Button(frm, text="Registrar Categoría", command=self.add_category)
        btn_add.grid(row=3, column=0, columnspan=2, pady=10)

        self.lbl_category_msg = ttk.Label(frame, text="", foreground="red")
        self.lbl_category_msg.pack()

    def add_category(self):
        name = self.entry_category_name.get().strip()
        desc = self.entry_category_desc.get().strip()
        type_ = self.cmb_category_type.get()

        if not name:
            self.lbl_category_msg.config(text="El nombre de la categoría no puede estar vacío.")
            return

        if self.db.add_category(name, desc, type_):
            self.lbl_category_msg.config(text="Categoría registrada exitosamente.", foreground="green")
            self.entry_category_name.delete(0, tk.END)
            self.entry_category_desc.delete(0, tk.END)
        else:
            self.lbl_category_msg.config(text="Error o categoría duplicada.")

    # Pestaña para registros (gastos e ingresos) y edición
    def create_record_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Registros")

        lbl_title = ttk.Label(frame, text="Registrar Ingreso / Gasto", font=('Arial', 16))
        lbl_title.pack(pady=10)

        frm = ttk.Frame(frame)
        frm.pack(pady=10)

        # Selección de cuenta
        ttk.Label(frm, text="Cuenta:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.cmb_account = ttk.Combobox(frm, values=self.get_accounts_list(), state="readonly")
        self.cmb_account.grid(row=0, column=1, padx=5, pady=5)

        # Selección de categoría (según tipo)
        ttk.Label(frm, text="Categoría:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.cmb_category = ttk.Combobox(frm, state="readonly")
        self.cmb_category.grid(row=1, column=1, padx=5, pady=5)
        # Actualizar categorías cuando se seleccione el tipo de registro
        ttk.Label(frm, text="Tipo de registro:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.cmb_record_type = ttk.Combobox(frm, values=["Ingreso", "Gasto"], state="readonly")
        self.cmb_record_type.grid(row=2, column=1, padx=5, pady=5)
        self.cmb_record_type.current(0)
        self.cmb_record_type.bind("<<ComboboxSelected>>", self.update_category_combobox)

        # Fecha y monto
        ttk.Label(frm, text="Fecha (YYYY-MM-DD):").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        self.entry_date = ttk.Entry(frm)
        self.entry_date.grid(row=3, column=1, padx=5, pady=5)
        self.entry_date.insert(0, datetime.now().strftime("%Y-%m-%d"))

        ttk.Label(frm, text="Monto:").grid(row=4, column=0, sticky='e', padx=5, pady=5)
        self.entry_amount = ttk.Entry(frm)
        self.entry_amount.grid(row=4, column=1, padx=5, pady=5)

        btn_add_record = ttk.Button(frm, text="Registrar", command=self.add_record)
        btn_add_record.grid(row=5, column=0, columnspan=2, pady=10)

        self.lbl_record_msg = ttk.Label(frame, text="", foreground="red")
        self.lbl_record_msg.pack()

        # Sección para edición de registros (lista y botón de editar)
        frm_edit = ttk.Frame(frame)
        frm_edit.pack(pady=20, fill='x')
        ttk.Label(frm_edit, text="Historial de Registros:", font=('Arial', 14)).pack()
        self.lst_records = tk.Listbox(frm_edit, height=8)
        self.lst_records.pack(fill='both', padx=10, pady=5)
        self.refresh_records_list()

        btn_edit = ttk.Button(frm_edit, text="Editar Registro", command=self.edit_record)
        btn_edit.pack(pady=5)

    def get_accounts_list(self):
        accounts = self.db.get_accounts()
        # Mostrar como "id - nombre"
        return [f"{acc[0]} - {acc[1]}" for acc in accounts]

    def update_category_combobox(self, event=None):
        type_ = self.cmb_record_type.get()
        categories = self.db.get_categories(type_)
        self.cmb_category['values'] = [f"{cat[0]} - {cat[1]}" for cat in categories]
        if categories:
            self.cmb_category.current(0)

    def add_record(self):
        try:
            account_str = self.cmb_account.get()
            account_id = int(account_str.split(" - ")[0])
        except:
            self.lbl_record_msg.config(text="Debe seleccionar una cuenta válida.")
            return

        try:
            cat_str = self.cmb_category.get()
            category_id = int(cat_str.split(" - ")[0])
        except:
            self.lbl_record_msg.config(text="Debe seleccionar una categoría válida.")
            return

        date_str = self.entry_date.get().strip()
        try:
            # Validar formato de fecha
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            self.lbl_record_msg.config(text="Fecha inválida. Use YYYY-MM-DD.")
            return

        try:
            amount = float(self.entry_amount.get().strip())
        except ValueError:
            self.lbl_record_msg.config(text="El monto debe ser numérico.")
            return

        type_ = self.cmb_record_type.get()
        self.db.add_record(account_id, category_id, date_str, amount, type_)
        self.lbl_record_msg.config(text="Registro agregado exitosamente.", foreground="green")
        self.refresh_records_list()

    def refresh_records_list(self):
        self.lst_records.delete(0, tk.END)
        records = self.db.get_records()
        for rec in records:
            # Formato: ID | Cuenta | Categoría | Fecha | Monto | Tipo
            self.lst_records.insert(tk.END, f"{rec[0]} | Cuenta:{rec[1]} | Cat:{rec[2]} | {rec[3]} | {rec[4]} | {rec[5]}")

    def edit_record(self):
        # Seleccionar registro de la lista
        selection = self.lst_records.curselection()
        if not selection:
            messagebox.showerror("Error", "Seleccione un registro para editar.")
            return
        index = selection[0]
        record_str = self.lst_records.get(index)
        record_id = int(record_str.split(" | ")[0])
        # Abrir una ventana para editar el registro
        EditRecordWindow(self, record_id)

    # Pestaña de reportes y gráficos
    def create_reports_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Reportes & Gráficos")

        frm = ttk.Frame(frame)
        frm.pack(pady=10)

        # Reporte de saldo actual
        ttk.Label(frm, text="Saldo Actual de una Cuenta:").grid(row=0, column=0, padx=5, pady=5)
        self.cmb_balance_account = ttk.Combobox(frm, values=self.get_accounts_list(), state="readonly")
        self.cmb_balance_account.grid(row=0, column=1, padx=5, pady=5)
        btn_balance = ttk.Button(frm, text="Consultar Saldo", command=self.show_balance)
        btn_balance.grid(row=0, column=2, padx=5, pady=5)

        # Reporte de gastos por categoría
        btn_cat_report = ttk.Button(frm, text="Reporte de Gastos por Categoría", command=self.report_by_category)
        btn_cat_report.grid(row=1, column=0, columnspan=3, pady=10)

        # Reporte de gastos por rango de fecha
        ttk.Label(frm, text="Fecha Inicio (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
        self.entry_start_date = ttk.Entry(frm)
        self.entry_start_date.grid(row=2, column=1, padx=5, pady=5)
        ttk.Label(frm, text="Fecha Fin (YYYY-MM-DD):").grid(row=3, column=0, padx=5, pady=5)
        self.entry_end_date = ttk.Entry(frm)
        self.entry_end_date.grid(row=3, column=1, padx=5, pady=5)
        btn_date_report = ttk.Button(frm, text="Reporte por Fecha", command=self.report_by_date_range)
        btn_date_report.grid(row=2, column=2, rowspan=2, padx=5, pady=5)

        # Gráficos
        btn_graph_cat = ttk.Button(frm, text="Gráfico: Gastos por Categoría", command=self.graph_by_category)
        btn_graph_cat.grid(row=4, column=0, columnspan=3, pady=10)
        btn_graph_date = ttk.Button(frm, text="Gráfico: Gastos por Rango de Fecha", command=self.graph_by_date_range)
        btn_graph_date.grid(row=5, column=0, columnspan=3, pady=10)

    def show_balance(self):
        try:
            account_str = self.cmb_balance_account.get()
            account_id = int(account_str.split(" - ")[0])
        except:
            messagebox.showerror("Error", "Seleccione una cuenta válida.")
            return
        balance = self.db.get_current_balance(account_id)
        messagebox.showinfo("Saldo Actual", f"El saldo actual es: {balance}")

    def report_by_category(self):
        data = self.db.get_expenses_by_category()
        report = "Gastos por Categoría:\n"
        for cat, total in data:
            report += f"{cat}: {total}\n"
        messagebox.showinfo("Reporte", report)

    def report_by_date_range(self):
        start_date = self.entry_start_date.get().strip()
        end_date = self.entry_end_date.get().strip()
        # Validar formato
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Fechas inválidas. Use el formato YYYY-MM-DD.")
            return
        data = self.db.get_expenses_by_date_range(start_date, end_date)
        report = f"Gastos entre {start_date} y {end_date}:\n"
        for rec in data:
            report += f"ID:{rec[0]} Cuenta:{rec[1]} Cat:{rec[2]} Fecha:{rec[3]} Monto:{rec[4]}\n"
        messagebox.showinfo("Reporte", report)

    def graph_by_category(self):
        data = self.db.get_expenses_by_category()
        if not data:
            messagebox.showinfo("Gráfico", "No hay datos para graficar.")
            return
        categories = [d[0] for d in data]
        totals = [d[1] for d in data]
        plt.figure(figsize=(8,6))
        plt.bar(categories, totals, color='skyblue')
        plt.title("Gastos por Categoría")
        plt.xlabel("Categoría")
        plt.ylabel("Total Gastado")
        plt.tight_layout()
        plt.show()

    def graph_by_date_range(self):
        start_date = self.entry_start_date.get().strip()
        end_date = self.entry_end_date.get().strip()
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Fechas inválidas. Use el formato YYYY-MM-DD.")
            return
        data = self.db.get_expenses_by_date_range(start_date, end_date)
        if not data:
            messagebox.showinfo("Gráfico", "No hay datos para graficar en ese rango.")
            return
        # Agrupar por fecha
        gastos_por_fecha = {}
        for rec in data:
            fecha = rec[3]
            gastos_por_fecha[fecha] = gastos_por_fecha.get(fecha, 0) + rec[4]
        fechas = sorted(gastos_por_fecha.keys())
        totales = [gastos_por_fecha[f] for f in fechas]
        plt.figure(figsize=(8,6))
        plt.plot(fechas, totales, marker='o', linestyle='-', color='green')
        plt.title(f"Gastos entre {start_date} y {end_date}")
        plt.xlabel("Fecha")
        plt.ylabel("Monto")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# =============================================================================
# Ventana secundaria para editar registros
# =============================================================================
class EditRecordWindow(tk.Toplevel):
    def __init__(self, parent, record_id):
        super().__init__(parent)
        self.parent = parent
        self.db = parent.db
        self.record_id = record_id
        self.title("Editar Registro")
        self.geometry("400x400")

        # Obtener datos actuales del registro
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT account_id, category_id, date, amount, type FROM records WHERE id=?", (record_id,))
        rec = cursor.fetchone()
        if not rec:
            messagebox.showerror("Error", "Registro no encontrado.")
            self.destroy()
            return
        self.orig_account_id, self.orig_category_id, self.orig_date, self.orig_amount, self.orig_type = rec

        frm = ttk.Frame(self)
        frm.pack(pady=10, padx=10, fill='x')

        # Cuenta
        ttk.Label(frm, text="Cuenta:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.cmb_account = ttk.Combobox(frm, values=self.parent.get_accounts_list(), state="readonly")
        self.cmb_account.grid(row=0, column=1, padx=5, pady=5)
        # Seleccionar la cuenta actual
        accounts = self.db.get_accounts()
        for idx, acc in enumerate(accounts):
            if acc[0] == self.orig_account_id:
                self.cmb_account.current(idx)
                break

        # Tipo
        ttk.Label(frm, text="Tipo:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.cmb_type = ttk.Combobox(frm, values=["Ingreso", "Gasto"], state="readonly")
        self.cmb_type.grid(row=1, column=1, padx=5, pady=5)
        self.cmb_type.set(self.orig_type)
        self.cmb_type.bind("<<ComboboxSelected>>", self.update_category_combobox)

        # Categoría
        ttk.Label(frm, text="Categoría:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
        self.cmb_category = ttk.Combobox(frm, state="readonly")
        self.cmb_category.grid(row=2, column=1, padx=5, pady=5)
        self.update_category_combobox()

        # Fecha
        ttk.Label(frm, text="Fecha (YYYY-MM-DD):").grid(row=3, column=0, sticky='e', padx=5, pady=5)
        self.entry_date = ttk.Entry(frm)
        self.entry_date.grid(row=3, column=1, padx=5, pady=5)
        self.entry_date.insert(0, self.orig_date)

        # Monto
        ttk.Label(frm, text="Monto:").grid(row=4, column=0, sticky='e', padx=5, pady=5)
        self.entry_amount = ttk.Entry(frm)
        self.entry_amount.grid(row=4, column=1, padx=5, pady=5)
        self.entry_amount.insert(0, str(self.orig_amount))

        btn_update = ttk.Button(frm, text="Actualizar Registro", command=self.update_record)
        btn_update.grid(row=5, column=0, columnspan=2, pady=10)

    def update_category_combobox(self, event=None):
        type_ = self.cmb_type.get()
        categories = self.db.get_categories(type_)
        self.cmb_category['values'] = [f"{cat[0]} - {cat[1]}" for cat in categories]
        # Seleccionar la categoría que concuerda con la original (si existe)
        for idx, cat in enumerate(categories):
            if cat[0] == self.orig_category_id:
                self.cmb_category.current(idx)
                break
        else:
            if categories:
                self.cmb_category.current(0)

    def update_record(self):
        try:
            account_str = self.cmb_account.get()
            account_id = int(account_str.split(" - ")[0])
        except:
            messagebox.showerror("Error", "Cuenta inválida.")
            return
        try:
            cat_str = self.cmb_category.get()
            category_id = int(cat_str.split(" - ")[0])
        except:
            messagebox.showerror("Error", "Categoría inválida.")
            return
        date_str = self.entry_date.get().strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Fecha inválida. Use YYYY-MM-DD.")
            return
        try:
            amount = float(self.entry_amount.get().strip())
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser numérico.")
            return
        new_type = self.cmb_type.get()
        if self.db.update_record(self.record_id, account_id, category_id, date_str, amount, new_type):
            messagebox.showinfo("Éxito", "Registro actualizado correctamente.")
            self.parent.refresh_records_list()
            self.destroy()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el registro.")


# =============================================================================
# Inicio de la aplicación
# =============================================================================
if __name__ == "__main__":
    app = ExpenseApp()
    app.mainloop()
