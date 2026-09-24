Algoritmo GestionCentroSalud
	
	// Declaracion de Variables
	Definir prof_id, prof_dni, prof_nom, prof_ape, prof_esp, prof_car Como Cadena
	Definir pac_id, pac_dni, pac_nom, pac_ape, pac_fNac, pac_sexo Como Cadena
	Definir hist_id, hist_fApertura, hist_antec, hist_alergias Como Cadena
	Definir ate_f, ate_mot, ate_diag, ate_trat Como Cadena
	Definir fua_id, fua_f, fua_serv, fua_diag, fua_proc Como Cadena
	Definir rec_id, rec_f, rec_ind, med1, med2 Como Cadena
	Definir cita_id, cita_f, cita_h, cita_est Como Cadena
	
	// Llamada a modulos (Genera un diagrama de flujo compacto y limpio)
	RegistrarProfesional(prof_id, prof_dni, prof_nom, prof_ape, prof_esp, prof_car)
	RegistrarPaciente(pac_id, pac_dni, pac_nom, pac_ape, pac_fNac, pac_sexo)
	AbrirHistoriaClinica(hist_id, hist_fApertura, hist_antec, hist_alergias)
	RegistrarAtencion(ate_f, ate_mot, ate_diag, ate_trat)
	GenerarDocumentos(fua_id, fua_f, fua_serv, fua_diag, fua_proc, rec_id, rec_f, rec_ind, med1, med2)
	RegistrarCitaFutura(cita_id, cita_f, cita_h, cita_est)
	
	// Reporte en pantalla
	MostrarReporte(pac_nom, pac_ape, pac_dni, pac_fNac, prof_nom, prof_ape, prof_dni, prof_esp, hist_id, ate_mot, ate_diag, fua_id, fua_serv, rec_id, rec_f, med1, med2, cita_id, cita_f, cita_h, cita_est)
	
FinAlgoritmo

SubProceso RegistrarProfesional(id Por Referencia, dni Por Referencia, nom Por Referencia, ape Por Referencia, esp Por Referencia, car Por Referencia)
	id <- "PR001"
	dni <- "27654321"
	nom <- "Ana"
	ape <- "Torres Quispe"
	esp <- "Medicina General"
	car <- "Medico"
FinSubProceso

SubProceso RegistrarPaciente(id Por Referencia, dni Por Referencia, nom Por Referencia, ape Por Referencia, fNac Por Referencia, sexo Por Referencia)
	id <- "PA001"
	dni <- "87654321"
	nom <- "Luis"
	ape <- "Ramos Vega"
	fNac <- "1990-05-10"
	sexo <- "M"
FinSubProceso

SubProceso AbrirHistoriaClinica(id Por Referencia, fApertura Por Referencia, antec Por Referencia, alergias Por Referencia)
	id <- "H001"
	fApertura <- "2026-09-12"
	antec <- "Ninguno"
	alergias <- "Ninguna"
FinSubProceso

SubProceso RegistrarAtencion(f Por Referencia, mot Por Referencia, diag Por Referencia, trat Por Referencia)
	f <- "2026-09-12"
	mot <- "Dolor de cabeza intenso"
	diag <- "Migrana"
	trat <- "Reposo y analgesico"
FinSubProceso

SubProceso GenerarDocumentos(fuaId Por Referencia, fuaF Por Referencia, fuaServ Por Referencia, fuaDiag Por Referencia, fuaProc Por Referencia, recId Por Referencia, recF Por Referencia, recInd Por Referencia, m1 Por Referencia, m2 Por Referencia)
	fuaId <- "FUA001"
	fuaF <- "2026-09-12"
	fuaServ <- "Medicina General"
	fuaDiag <- "Migrana"
	fuaProc <- "Consulta ambulatoria"
	
	recId <- "REC001"
	recF <- "2026-09-12"
	recInd <- "Tomar con alimentos, reposo 24h"
	m1 <- "Paracetamol 500mg - cada 8h por 3 dias"
	m2 <- "Ibuprofeno 400mg - solo si persiste el dolor"
FinSubProceso

SubProceso RegistrarCitaFutura(id Por Referencia, f Por Referencia, h Por Referencia, est Por Referencia)
	id <- "CITA001"
	f <- "2026-09-19"
	h <- "10:00"
	est <- "PENDIENTE"
FinSubProceso

SubProceso MostrarReporte(pacNom, pacApe, pacDni, pacFNac, profNom, profApe, profDni, profEsp, histId, ateMot, ateDiag, fuaId, fuaServ, recId, recF, m1, m2, citaId, citaF, citaH, citaEst)
	Escribir "=== Paciente ==="
	Escribir pacNom, " ", pacApe, " (DNI: ", pacDni, ")"
	Escribir "Fecha nacimiento: ", pacFNac
	
	Escribir ""
	Escribir "=== Profesional que atiende ==="
	Escribir profNom, " ", profApe, " (DNI: ", profDni, ")"
	Escribir "Especialidad: ", profEsp
	
	Escribir ""
	Escribir "=== Historia clinica ==="
	Escribir "Id historia: ", histId
	
	Escribir ""
	Escribir "=== Atencion registrada ==="
	Escribir "Motivo: ", ateMot
	Escribir "Diagnostico: ", ateDiag
	Escribir "Atendido por: ", profNom
	
	Escribir ""
	Escribir "=== Documentos generados ==="
	Escribir "FUA id: ", fuaId, " | servicio: ", fuaServ
	
	Escribir ""
	Escribir "=== Receta medica ==="
	Escribir "Receta ", recId, " (", recF, ")"
	Escribir "Medicamentos:"
	Escribir "- ", m1
	Escribir "- ", m2
	
	Escribir ""
	Escribir "=== Cita registrada ==="
	Escribir "Cita ", citaId, " - ", pacNom, " con ", profNom, " (", citaF, " ", citaH, ") [", citaEst, "]"
FinSubProceso