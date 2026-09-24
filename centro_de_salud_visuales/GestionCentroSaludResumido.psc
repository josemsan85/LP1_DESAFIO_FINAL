Algoritmo GestionCentroSalud
	Definir profesional, paciente, historia, atencion, fua, receta, cita Como Cadena
	
	// 1. Registrar al profesional que atiende
	profesional <- "Dra. Ana Torres Quispe (Medicina General)"
	
	// 2. Registrar al paciente
	paciente <- "Luis Ramos Vega (DNI: 87654321)"
	
	// 3. Abrir historia clinica
	historia <- "Historia Clinica H001 - Apertura 2026-09-12"
	
	// 4. Registrar atencion medica
	atencion <- "Motivo: Dolor de cabeza | Dx: Migraña"
	
	// 5. Generar documentos (FUA y Receta)
	fua <- "FUA001 - Consulta ambulatoria"
	receta <- "REC001 - Paracetamol 500mg / Ibuprofeno 400mg"
	
	// 6. Registrar cita futura de control
	cita <- "CITA001 - Control para 2026-09-19 a las 10:00"
	
	// 7. Mostrar resultados
	Escribir "=== PACIENTE Y PROFESIONAL ==="
	Escribir paciente, " | ", profesional
	
	Escribir "=== HISTORIA Y ATENCION ==="
	Escribir historia
	Escribir atencion
	
	Escribir "=== DOCUMENTOS Y CITA ==="
	Escribir fua
	Escribir receta
	Escribir cita
FinAlgoritmo