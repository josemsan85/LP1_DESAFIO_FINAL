"""Ventana principal del sistema del Centro de Salud Rural "Santa Rosa".

Usa el patrón Singleton (RepositorioCentroSalud) como fuente única de datos
y demuestra programación orientada a eventos (comandos sobre botones).
Equivalente en Python (tkinter) de VentanaPrincipal.java (Swing).
"""
import re
import tkinter as tk
from datetime import date, timedelta
from tkinter import messagebox, ttk

from repositorio_centro_salud import RepositorioCentroSalud


# ---------------------------------------------------------
# Utilitarios de interfaz
# ---------------------------------------------------------
class ComboObjetos(ttk.Combobox):
    """Combobox que guarda objetos del dominio y muestra una etiqueta de texto.

    Reemplaza a JComboBox<T> de Java: tkinter solo maneja textos, así que
    se guarda la lista de objetos en paralelo.
    """

    def __init__(self, padre, etiquetar=str):
        super().__init__(padre, state="readonly")
        self._objetos = []
        self._etiquetar = etiquetar  # función que convierte el objeto en texto

    def agregar(self, objeto) -> None:
        self._objetos.append(objeto)
        self["values"] = [self._etiquetar(o) for o in self._objetos]
        if self.current() == -1:  # si no hay nada elegido, selecciona el primero
            self.current(0)

    def seleccionado(self):
        indice = self.current()
        return self._objetos[indice] if indice != -1 else None


def _crear_formulario(padre) -> ttk.Frame:
    formulario = ttk.Frame(padre)
    formulario.columnconfigure(1, weight=1)
    return formulario


def _poner_en_fila(formulario, fila: int, texto: str, widget):
    ttk.Label(formulario, text=texto).grid(row=fila, column=0, sticky="w", padx=5, pady=2)
    widget.grid(row=fila, column=1, sticky="ew", padx=5, pady=2)
    return widget


def _campo_texto(formulario, fila: int, texto: str, valor: str = "") -> ttk.Entry:
    campo = ttk.Entry(formulario)
    campo.insert(0, valor)
    return _poner_en_fila(formulario, fila, texto, campo)


def _limpiar(*campos: ttk.Entry) -> None:
    for campo in campos:
        campo.delete(0, tk.END)


def _crear_tabla(padre, columnas: tuple):
    """Devuelve (marco, tabla): el marco se empaqueta, la tabla recibe las filas."""
    marco = ttk.Frame(padre)
    tabla = ttk.Treeview(marco, columns=columnas, show="headings", selectmode="browse")
    for columna in columnas:
        tabla.heading(columna, text=columna)
        tabla.column(columna, width=110, anchor="w")
    barra = ttk.Scrollbar(marco, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=barra.set)
    tabla.pack(side="left", fill="both", expand=True)
    barra.pack(side="right", fill="y")
    return marco, tabla


def _nombre_completo(persona) -> str:
    return f"{persona.nombres} {persona.apellidos}"


class VentanaPrincipal(tk.Tk):
    ANCHO = 850
    ALTO = 600

    def __init__(self):
        super().__init__()
        self.title("Centro de Salud Rural Santa Rosa - Chugur")
        self._centrar()

        self._repo = RepositorioCentroSalud.get_instancia()

        # Combos que dependen de los pacientes/profesionales registrados.
        # Se crean en los paneles; se declaran aquí para que sea claro qué existe.
        self._combo_paciente_atencion = None
        self._combo_profesional_atencion = None
        self._combo_paciente_cita = None
        self._combo_profesional_cita = None
        self._combo_atencion_receta = None
        self._tabla_citas = None

        pestanas = ttk.Notebook(self)
        pestanas.add(self._crear_panel_pacientes(pestanas), text="Pacientes")
        pestanas.add(self._crear_panel_profesionales(pestanas), text="Profesionales")
        pestanas.add(self._crear_panel_atenciones(pestanas), text="Atenciones y Recetas")
        pestanas.add(self._crear_panel_citas(pestanas), text="Citas")
        pestanas.pack(fill="both", expand=True)

    def _centrar(self) -> None:
        x = (self.winfo_screenwidth() - self.ANCHO) // 2
        y = (self.winfo_screenheight() - self.ALTO) // 2
        self.geometry(f"{self.ANCHO}x{self.ALTO}+{x}+{y}")

    def _avisar(self, titulo: str, mensaje: str) -> None:
        messagebox.showwarning(titulo, mensaje, parent=self)

    def _datos_persona_validos(self, dni: str, nombres: str, apellidos: str) -> bool:
        """Valida los datos comunes de paciente y profesional; avisa si hay error."""
        if re.fullmatch(r"[0-9]{8}", dni) is None:
            self._avisar("Dato inválido", "El DNI debe tener exactamente 8 dígitos.")
            return False
        if not nombres or not apellidos:
            self._avisar("Dato inválido", "Nombres y apellidos son obligatorios.")
            return False
        return True

    # ---------------------------------------------------------
    # TAB 1: PACIENTES
    # ---------------------------------------------------------
    def _crear_panel_pacientes(self, pestanas) -> ttk.Frame:
        panel = ttk.Frame(pestanas, padding=10)

        formulario = _crear_formulario(panel)
        fecha_sugerida = (date.today() - timedelta(days=365 * 30)).isoformat()  # aprox. 30 años atrás
        txt_dni = _campo_texto(formulario, 0, "DNI (8 dígitos):")
        txt_nombres = _campo_texto(formulario, 1, "Nombres:")
        txt_apellidos = _campo_texto(formulario, 2, "Apellidos:")
        txt_fecha_nac = _campo_texto(formulario, 3, "Fecha nacimiento (AAAA-MM-DD):", fecha_sugerida)
        txt_sexo = _campo_texto(formulario, 4, "Sexo (M/F):")

        marco_tabla, tabla = _crear_tabla(
            panel, ("ID", "DNI", "Nombres", "Apellidos", "F. Nacimiento", "Sexo"))

        # Evento: click en "Registrar paciente"
        def registrar() -> None:
            dni = txt_dni.get().strip()
            nombres = txt_nombres.get().strip()
            apellidos = txt_apellidos.get().strip()
            if not self._datos_persona_validos(dni, nombres, apellidos):
                return

            paciente = self._repo.crear_paciente(
                dni, nombres, apellidos, txt_fecha_nac.get().strip(), txt_sexo.get().strip())

            tabla.insert("", tk.END, values=(
                paciente.id_persona, paciente.dni, paciente.nombres, paciente.apellidos,
                paciente.fecha_nacimiento, paciente.sexo))

            self._combo_paciente_atencion.agregar(paciente)
            self._combo_paciente_cita.agregar(paciente)

            _limpiar(txt_dni, txt_nombres, txt_apellidos, txt_sexo)

        ttk.Button(formulario, text="Registrar paciente", command=registrar).grid(
            row=5, column=1, sticky="ew", padx=5, pady=2)

        formulario.pack(fill="x")
        marco_tabla.pack(fill="both", expand=True, pady=(10, 0))
        return panel

    # ---------------------------------------------------------
    # TAB 2: PROFESIONALES
    # ---------------------------------------------------------
    def _crear_panel_profesionales(self, pestanas) -> ttk.Frame:
        panel = ttk.Frame(pestanas, padding=10)

        formulario = _crear_formulario(panel)
        txt_dni = _campo_texto(formulario, 0, "DNI (8 dígitos):")
        txt_nombres = _campo_texto(formulario, 1, "Nombres:")
        txt_apellidos = _campo_texto(formulario, 2, "Apellidos:")
        txt_especialidad = _campo_texto(formulario, 3, "Especialidad:")
        txt_cargo = _campo_texto(formulario, 4, "Cargo:")

        marco_tabla, tabla = _crear_tabla(
            panel, ("ID", "DNI", "Nombres", "Apellidos", "Especialidad", "Cargo"))

        def registrar() -> None:
            dni = txt_dni.get().strip()
            nombres = txt_nombres.get().strip()
            apellidos = txt_apellidos.get().strip()
            if not self._datos_persona_validos(dni, nombres, apellidos):
                return

            profesional = self._repo.crear_profesional(
                dni, nombres, apellidos, txt_especialidad.get().strip(), txt_cargo.get().strip())

            tabla.insert("", tk.END, values=(
                profesional.id_persona, profesional.dni, profesional.nombres,
                profesional.apellidos, profesional.especialidad, profesional.cargo))

            self._combo_profesional_atencion.agregar(profesional)
            self._combo_profesional_cita.agregar(profesional)

            _limpiar(txt_dni, txt_nombres, txt_apellidos, txt_especialidad, txt_cargo)

        ttk.Button(formulario, text="Registrar profesional", command=registrar).grid(
            row=5, column=1, sticky="ew", padx=5, pady=2)

        formulario.pack(fill="x")
        marco_tabla.pack(fill="both", expand=True, pady=(10, 0))
        return panel

    # ---------------------------------------------------------
    # TAB 3: ATENCIONES + RECETAS
    # ---------------------------------------------------------
    def _crear_panel_atenciones(self, pestanas) -> ttk.Frame:
        panel = ttk.Frame(pestanas, padding=10)

        # --- Formulario de atención ---
        form_atencion = _crear_formulario(panel)
        self._combo_paciente_atencion = _poner_en_fila(
            form_atencion, 0, "Paciente:", ComboObjetos(form_atencion))
        self._combo_profesional_atencion = _poner_en_fila(
            form_atencion, 1, "Profesional:", ComboObjetos(form_atencion))
        txt_fecha = _campo_texto(form_atencion, 2, "Fecha:", date.today().isoformat())
        txt_motivo = _campo_texto(form_atencion, 3, "Motivo:")
        txt_diagnostico = _campo_texto(form_atencion, 4, "Diagnóstico:")
        txt_tratamiento = _campo_texto(form_atencion, 5, "Tratamiento:")

        # Tabla arriba, receta abajo (equivale al JSplitPane vertical).
        # Los paneles deben crearse como hijos del PanedWindow.
        centro = ttk.PanedWindow(panel, orient="vertical")
        marco_atenciones, tabla_atenciones = _crear_tabla(
            centro, ("Fecha", "Paciente", "Profesional", "Diagnóstico"))

        def registrar_atencion() -> None:
            paciente = self._combo_paciente_atencion.seleccionado()
            profesional = self._combo_profesional_atencion.seleccionado()
            if paciente is None or profesional is None:
                self._avisar("Faltan datos", "Registra al menos un paciente y un profesional primero.")
                return

            atencion = self._repo.crear_atencion(
                paciente, profesional, txt_fecha.get().strip(), txt_motivo.get().strip(),
                txt_diagnostico.get().strip(), txt_tratamiento.get().strip())

            tabla_atenciones.insert("", tk.END, values=(
                atencion.fecha, _nombre_completo(paciente), _nombre_completo(profesional),
                atencion.diagnostico))
            self._combo_atencion_receta.agregar(atencion)

            _limpiar(txt_motivo, txt_diagnostico, txt_tratamiento)

        ttk.Button(form_atencion, text="Registrar atención", command=registrar_atencion).grid(
            row=6, column=1, sticky="ew", padx=5, pady=2)

        # --- Formulario de receta (usa la atención seleccionada) ---
        marco_receta = ttk.LabelFrame(
            centro, text="Receta médica de la atención seleccionada", padding=5)

        self._combo_atencion_receta = ComboObjetos(marco_receta)  # Atencion.__str__ da la etiqueta
        self._combo_atencion_receta.pack(fill="x", pady=2)

        fila_medicamento = ttk.Frame(marco_receta)
        fila_medicamento.columnconfigure(0, weight=1)
        fila_medicamento.pack(fill="x", pady=2)
        txt_medicamento = ttk.Entry(fila_medicamento)
        txt_medicamento.grid(row=0, column=0, sticky="ew", padx=(0, 5))

        fila_indicaciones = ttk.Frame(marco_receta)
        fila_indicaciones.columnconfigure(1, weight=1)
        fila_indicaciones.pack(fill="x", pady=2)
        ttk.Label(fila_indicaciones, text="Indicaciones: ").grid(row=0, column=0)
        txt_indicaciones = ttk.Entry(fila_indicaciones)
        txt_indicaciones.grid(row=0, column=1, sticky="ew", padx=5)

        lista_medicamentos = tk.Listbox(marco_receta, height=5)
        lista_medicamentos.pack(fill="both", expand=True, pady=2)

        def agregar_medicamento() -> None:
            medicamento = txt_medicamento.get().strip()
            if medicamento:
                lista_medicamentos.insert(tk.END, medicamento)
                _limpiar(txt_medicamento)

        def guardar_receta() -> None:
            atencion = self._combo_atencion_receta.seleccionado()
            medicamentos = list(lista_medicamentos.get(0, tk.END))
            if atencion is None or not medicamentos:
                self._avisar("Faltan datos",
                             "Selecciona una atención y agrega al menos un medicamento.")
                return

            receta = self._repo.crear_receta(atencion, txt_indicaciones.get().strip(), medicamentos)
            messagebox.showinfo(
                "Receta guardada",
                f"Receta {receta.id_receta} guardada con {len(receta.medicamentos)} medicamento(s).",
                parent=self)

            lista_medicamentos.delete(0, tk.END)
            _limpiar(txt_indicaciones)

        ttk.Button(fila_medicamento, text="+ Medicamento", command=agregar_medicamento).grid(
            row=0, column=1)
        ttk.Button(fila_indicaciones, text="Guardar receta", command=guardar_receta).grid(
            row=0, column=2)

        centro.add(marco_atenciones, weight=55)
        centro.add(marco_receta, weight=45)

        form_atencion.pack(fill="x")
        centro.pack(fill="both", expand=True, pady=(10, 0))
        return panel

    # ---------------------------------------------------------
    # TAB 4: CITAS
    # ---------------------------------------------------------
    def _crear_panel_citas(self, pestanas) -> ttk.Frame:
        panel = ttk.Frame(pestanas, padding=10)

        formulario = _crear_formulario(panel)
        self._combo_paciente_cita = _poner_en_fila(
            formulario, 0, "Paciente:", ComboObjetos(formulario))
        self._combo_profesional_cita = _poner_en_fila(
            formulario, 1, "Profesional:", ComboObjetos(formulario))
        txt_fecha = _campo_texto(
            formulario, 2, "Fecha (AAAA-MM-DD):", (date.today() + timedelta(days=7)).isoformat())
        txt_hora = _campo_texto(formulario, 3, "Hora (HH:MM):", "10:00")

        marco_tabla, self._tabla_citas = _crear_tabla(
            panel, ("ID", "Paciente", "Profesional", "Fecha", "Hora", "Estado"))

        def registrar_cita() -> None:
            paciente = self._combo_paciente_cita.seleccionado()
            profesional = self._combo_profesional_cita.seleccionado()
            if paciente is None or profesional is None:
                self._avisar("Faltan datos", "Registra al menos un paciente y un profesional primero.")
                return

            cita = self._repo.crear_cita(
                paciente, profesional, txt_fecha.get().strip(), txt_hora.get().strip())
            self._tabla_citas.insert("", tk.END, values=(
                cita.id_cita, _nombre_completo(paciente), _nombre_completo(profesional),
                cita.fecha, cita.hora, cita.estado))

        ttk.Button(formulario, text="Registrar cita", command=registrar_cita).grid(
            row=4, column=1, sticky="ew", padx=5, pady=2)

        panel_botones = ttk.Frame(panel)
        # Evento: cambiar estado de la cita seleccionada en la tabla
        ttk.Button(panel_botones, text="Marcar atendida",
                   command=lambda: self._actualizar_estado_cita_seleccionada(True)).pack(
            side="left", padx=5)
        ttk.Button(panel_botones, text="Cancelar cita",
                   command=lambda: self._actualizar_estado_cita_seleccionada(False)).pack(
            side="left", padx=5)

        formulario.pack(fill="x")
        marco_tabla.pack(fill="both", expand=True, pady=(10, 0))
        panel_botones.pack(pady=(10, 0))
        return panel

    def _actualizar_estado_cita_seleccionada(self, atendida: bool) -> None:
        seleccion = self._tabla_citas.selection()
        if not seleccion:
            self._avisar("Sin selección", "Selecciona una cita de la tabla.")
            return

        fila = self._tabla_citas.index(seleccion[0])
        cita = self._repo.citas[fila]
        if atendida:
            cita.confirmar_atendida()
        else:
            cita.cancelar()
        self._tabla_citas.set(seleccion[0], "Estado", cita.estado)


if __name__ == "__main__":
    VentanaPrincipal().mainloop()
