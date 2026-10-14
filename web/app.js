"use strict";
const dictionary = {
  es: {
    missingLogin: "Escribe tu usuario y tu contraseña para entrar.",
    signingIn: "Entrando…",
    backendUnavailable:
      "No se puede conectar con la academia. Abre INICIAR_WINDOWS.bat y mantén su ventana abierta. Usa la dirección que abra el programa, no el archivo HTML ni GitHub Pages.",
    requestTimeout:
      "El servidor no responde. Comprueba que la ventana de inicio siga abierta y vuelve a intentarlo.",
    space: "ESPACIO",
    level_has_history:
      "Esta misión tiene asignaciones o historial. Consérvala como borrador.",
    deleteConfirm:
      "¿Eliminar definitivamente esta misión sin uso? No se puede deshacer.",
    academy: "Academia espacial",
    tagline: "MAKERS · APRENDER CREANDO",
    loginTitle: "Tu próxima aventura empieza con una tecla.",
    loginIntro:
      "Explora nuevos mundos junto a ATIBOT. Aprende a escribir, misión a misión, a tu ritmo.",
    welcomeBack: "¡Bienvenido a bordo!",
    loginSubtitle: "Accede a tu academia de mecanografía.",
    login: "Entrar en la academia",
    username: "Usuario o correo",
    password: "Contraseña",
    demo: "CUENTAS DE DEMOSTRACIÓN",
    demoInfo: "Datos ficticios. Contraseña común: AtigraDemo2026!",
    teacher: "Docente",
    student: "Alumno",
    physical: "Las misiones requieren un teclado físico.",
    provisional: "ATIBOT provisional · recurso sustituible",
    map: "Mi universo",
    progress: "Mi progreso",
    ranking: "Clasificación",
    classes: "Mis clases",
    levels: "Misiones",
    reports: "Seguimiento",
    mission: "Misión",
    logout: "Cerrar sesión",
    journey: "TU VIAJE ESPACIAL",
    hello: "¡Hola, {name}!",
    helloSub: "Cada tecla cuenta. ¿Listo para descubrir un nuevo mundo?",
    heroTitle: "Pequeñas teclas. Grandes aventuras.",
    heroSub:
      "Tu misión es aprender con calma. La precisión te llevará más lejos que la velocidad.",
    continue: "Continuar misión",
    noNext: "Todas las misiones completadas",
    bots: "ATIBOTS",
    accuracy: "Precisión",
    wpm: "PPM netas",
    completed: "Misiones completadas",
    totalTime: "Tiempo de práctica",
    universe: "Explora tu universo",
    universeSub: "Seis planetas. Un viaje lleno de descubrimientos.",
    planet: "PLANETA",
    available: "Disponible",
    locked: "Bloqueado",
    finished: "Completado",
    missionsCount: "{n} misiones asignadas",
    weekly: "Reto semanal",
    viewAll: "Ver todo →",
    noRanking:
      "La aventura acaba de empezar. Completa una misión del reto para aparecer aquí.",
    noLevels: "Tu docente todavía no ha asignado misiones.",
    week: "Semana del",
    badges: "Tus insignias",
    precisionBadge: "Manos de precisión",
    precisionDesc: "Completa una misión con un 97% de precisión.",
    explorerBadge: "Explorador espacial",
    explorerDesc: "Completa seis misiones diferentes.",
    steadyBadge: "Constancia estelar",
    steadyDesc: "Practica en tres días diferentes.",
    earned: "Conseguida",
    pending: "En camino",
    tip: "Un consejo de ATIBOT",
    tipText:
      "Coloca tus índices en F y J. Respira, mira el texto y escribe sin prisa.",
    privacy:
      "Un espacio de aprendizaje seguro. Sin publicidad ni perfiles públicos.",
    missionTitle: "Tu misión",
    practice: "Práctica libre",
    evaluated: "Misión evaluada",
    start: "Comenzar",
    back: "Volver al mapa",
    pause: "Pausar",
    resume: "Reanudar",
    paused: "En pausa. Reanuda cuando estés listo.",
    typeHere: "Escribe aquí para comenzar…",
    typeHint:
      "Empieza con la primera letra. Retroceso corrige; los errores cuentan. No se admite pegar.",
    practiceHint:
      "Sin presión ni puntuación. La práctica se guarda, pero no desbloquea misiones.",
    time: "Tiempo activo",
    target: "Objetivo",
    resultTitle: "¡Misión completada!",
    practiceResult: "¡Práctica completada!",
    resultSub: "Cada intento es un paso hacia un nuevo mundo.",
    errors: "Teclas para practicar",
    noErrors: "¡Sin errores! Buen trabajo.",
    previous: "Comparación con tu mejor intento",
    firstAttempt: "Este es tu primer intento evaluado.",
    accuracyAdvice:
      "Practica despacio las teclas destacadas. La precisión es lo primero.",
    speedAdvice:
      "¡Buena precisión! Sigue practicando con ritmo para alcanzar el objetivo.",
    greatAdvice: "¡Excelente equilibrio entre precisión y ritmo!",
    repeat: "Repetir misión",
    next: "Siguiente misión",
    abandon: "Salir de la misión",
    abandonConfirm:
      "¿Salir? El intento incompleto se guardará sin valoración ni puntos.",
    saving: "Guardando…",
    saved: "Cambios guardados",
    history: "Historial de intentos",
    date: "Fecha",
    level: "Nivel",
    language: "Idioma del ejercicio",
    status: "Estado",
    abandoned: "Incompleto",
    best: "Mejores resultados",
    allAttempts: "Todos los intentos",
    evolution: "Tu evolución",
    accuracyEvolution: "Precisión de los últimos intentos",
    wpmEvolution: "PPM de los últimos intentos",
    noHistory: "Todavía no hay intentos. Tu primera misión te espera.",
    personal: "Reconocimientos personales",
    improvement: "Superación",
    improvementDesc:
      "Mejora la precisión de una misión respecto al primer intento.",
    constancy: "Constancia",
    constancyDesc: "Tu tiempo de práctica también merece reconocimiento.",
    precision: "Precisión",
    precisionRecognition: "Aprende a tu ritmo, con calma y atención.",
    rankingOff:
      "Tu docente ha ocultado la clasificación. Tu progreso sigue contando.",
    weeklyRules:
      "Cada misión aporta su mejor intento de la semana. Solo cuentan las misiones del reto. Desempate: precisión y menor tiempo.",
    timezone: "Lunes a domingo · Europe/Madrid",
    position: "Posición",
    alias: "Alias",
    points: "Puntos",
    createClass: "Crear clase",
    className: "Nombre de la clase",
    edit: "Editar",
    archive: "Archivar",
    restore: "Restaurar",
    archived: "Archivada",
    students: "Alumnos",
    newStudent: "Crear alumno",
    email: "Correo (opcional)",
    accountName: "Nombre de usuario",
    class: "Clase",
    noClass: "Sin clase",
    save: "Guardar",
    cancel: "Cancelar",
    resetPassword: "Restablecer contraseña",
    newPassword: "Nueva contraseña (mínimo 8 caracteres)",
    move: "Mover / retirar",
    assign: "Asignar misiones",
    sequence: "Secuencia de misiones",
    addLevel: "Añadir misión",
    remove: "Retirar",
    reorder: "Orden",
    unlock: "Precisión para desbloquear (%)",
    prerequisite: "Requisito explícito",
    automatic: "Misión anterior (automático)",
    weeklyChallenge: "Incluida en el reto semanal",
    leaderboardEnabled: "Mostrar clasificación semanal",
    scoreRules: "Parámetros de valoración",
    weight: "Peso de precisión (0–1)",
    thresholds: "Umbrales 2, 3, 4 y 5 ATIBOTS",
    cap2: "Precisión mínima para superar 2 ATIBOTS",
    cap3: "Precisión mínima para superar 3 ATIBOTS",
    five: "Precisión mínima para 5 ATIBOTS",
    assignmentNote:
      "Retirar una misión conserva su historial. Cada misión exige la precisión indicada en su requisito previo.",
    newLevel: "Crear misión",
    clone: "Copiar y editar",
    name: "Nombre",
    mode: "Modalidad",
    text: "Texto que practicar",
    publish: "Publicada",
    draft: "Borrador",
    contentLanguage: "Idioma del contenido",
    targetWpm: "Objetivo de PPM",
    all: "Todos",
    from: "Desde",
    to: "Hasta",
    filter: "Filtrar",
    export: "Exportar CSV",
    assigned: "Asignadas",
    lastActivity: "Última actividad",
    mostErrors: "Errores frecuentes",
    attempts: "Intentos",
    reportNote:
      "Promedios: todos los intentos evaluados completados. Mejores: un resultado por misión, elegido por puntuación. Prácticas e incompletos se muestran aparte.",
    classSummary: "Resumen por alumno",
    assignmentFor: "Asignación para",
    personalAssign: "Asignar individualmente",
    none: "Ninguno",
    deleteContent:
      "El contenido con historial se conserva; puedes dejarlo en borrador.",
    score: "Puntuación",
    sound: "Sonido",
    motion: "Reducir movimiento",
    loading: "Cargando…",
    error: "No se pudo completar la operación.",
    invalid_login: "Usuario o contraseña incorrectos.",
    unauthenticated: "Tu sesión ha terminado. Vuelve a entrar.",
    forbidden: "No tienes permiso para esta acción.",
    level_locked: "Esta misión no está disponible.",
    password_length: "La contraseña debe tener entre 8 y 200 caracteres.",
    conflict:
      "El usuario o correo ya existe, o el registro entra en conflicto.",
    invalid_input: "Revisa los campos del formulario.",
    invalid_level: "Revisa el texto, idioma y objetivos de la misión.",
    invalid_rules: "Revisa los parámetros de valoración.",
    rate_limited: "Demasiados intentos. Espera cinco minutos.",
    incomplete: "Completa el texto antes de enviar.",
    invalid_time: "El tiempo de actividad no es válido.",
    implausible_speed: "La velocidad registrada no es plausible.",
    invalid_events: "No se pudieron validar las pulsaciones.",
    invalid_run: "Este intento ya se ha enviado o no es válido.",
    shared_level_readonly: "Copia esta misión para editarla.",
    server_error: "Error del servidor. Consulta el registro.",
    castle: "Defensa del castillo orbital",
    race: "Carrera de naves",
    bridge: "Puente de runas",
    dragon: "Dragón mecánico",
    explore: "Exploración planetaria",
    portal: "Portal galáctico",
    castleInstruction:
      "Completa palabras para cargar los escudos y alejar el meteorito.",
    raceInstruction: "Cada palabra completa impulsa tu nave hacia la meta.",
    bridgeInstruction:
      "Cada secuencia correcta construye otra runa del puente.",
    dragonInstruction:
      "Recupera piezas al completar palabras y devuelve el color al dragón.",
    exploreInstruction:
      "Escribe las instrucciones y recoge recursos para tu expedición.",
    portalInstruction:
      "Cada carácter correcto carga el portal. Completa el texto para abrirlo.",
    ready: "Preparado",
    personalBest: "Mejor marca",
    recognitionProgress: "{n} días de práctica",
    noData: "Sin datos",
    challenge: "RETO DE LA SEMANA",
    active: "Activa",
    bestBots: "Mejor valoración",
    allModes: "SEIS FORMAS DE APRENDER",
    clear: "Limpiar",
    go: "Vamos allá",
    exportNote:
      "CSV incluye los resultados filtrados, las prácticas y los intentos incompletos.",
    weekStart: "Lunes de la semana",
    assignmentSaved: "Asignación guardada. El historial se conserva.",
    usernameHelp:
      "Comparte estas credenciales de forma privada. La contraseña no se podrá consultar después.",
    orderHelp:
      "El orden es numérico. Puedes usar posiciones intermedias para reordenar.",
    assignmentLanguage:
      "La interfaz y el idioma del ejercicio son independientes.",
    credentials: "Credenciales",
    sessionExpired: "La sesión terminó; el intento local no se ha enviado.",
    retry: "Reintentar envío",
    errorsCorrected:
      "Los errores corregidos también se incluyen en la precisión.",
    loginDemoWarning:
      "Demostración local. Cambia las contraseñas antes de exponer el servicio.",
    activeStudents: "Alumnos inscritos",
    delete: "Eliminar",
    levelsDone: "Completadas",
    help: "Ayuda",
    studentDetail: "Seguimiento del alumno",
    exerciseOnly: "Texto asignado",
    rulesHint: "Para 5 ATIBOTS también se exige alcanzar el objetivo de PPM.",
    unitMinutes: "min",
    backspaceHint:
      "Puedes corregir con Retroceso. Las teclas mantenidas no se repiten.",
    practiceWithoutPressure: "Practica sin reloj regresivo",
    weekHistory: "Historial semanal",
    hide: "Ocultar",
    reportTime: "Tiempo activo (s)",
    badgeProgress: "Completa misiones para ganar reconocimientos.",
  },
  en: {
    missingLogin: "Enter your username and password to sign in.",
    signingIn: "Signing in…",
    backendUnavailable:
      "Cannot connect to the academy. Run the local launcher and keep its window open. Use the address opened by the launcher, not the HTML file or GitHub Pages.",
    requestTimeout:
      "The server is not responding. Check that the launcher window is still open and try again.",
    space: "SPACE",
    level_has_history:
      "This mission has assignments or history. Keep it as a draft.",
    deleteConfirm:
      "Permanently delete this unused mission? This cannot be undone.",
    academy: "Space academy",
    tagline: "MAKERS · LEARN BY CREATING",
    loginTitle: "Your next adventure starts with a key.",
    loginIntro:
      "Explore new worlds with ATIBOT. Learn to type, mission by mission, at your own pace.",
    welcomeBack: "Welcome aboard!",
    loginSubtitle: "Sign in to your typing academy.",
    login: "Enter the academy",
    username: "Username or email",
    password: "Password",
    demo: "DEMONSTRATION ACCOUNTS",
    demoInfo: "Fictional data. Shared password: AtigraDemo2026!",
    teacher: "Teacher",
    student: "Student",
    physical: "Missions require a physical keyboard.",
    provisional: "Provisional ATIBOT · replaceable asset",
    map: "My universe",
    progress: "My progress",
    ranking: "Leaderboard",
    classes: "My classes",
    levels: "Missions",
    reports: "Reports",
    mission: "Mission",
    logout: "Sign out",
    journey: "YOUR SPACE JOURNEY",
    hello: "Hello, {name}!",
    helloSub: "Every key counts. Ready to discover a new world?",
    heroTitle: "Small keys. Big adventures.",
    heroSub:
      "Your mission is to learn calmly. Accuracy will take you further than speed.",
    continue: "Continue mission",
    noNext: "All missions completed",
    bots: "ATIBOTS",
    accuracy: "Accuracy",
    wpm: "Net WPM",
    completed: "Completed missions",
    totalTime: "Practice time",
    universe: "Explore your universe",
    universeSub: "Six planets. A journey full of discoveries.",
    planet: "PLANET",
    available: "Available",
    locked: "Locked",
    finished: "Completed",
    missionsCount: "{n} assigned missions",
    weekly: "Weekly challenge",
    viewAll: "View all →",
    noRanking:
      "The adventure is just starting. Complete a challenge mission to appear here.",
    noLevels: "Your teacher has not assigned any missions yet.",
    week: "Week of",
    badges: "Your badges",
    precisionBadge: "Hands of accuracy",
    precisionDesc: "Complete a mission with 97% accuracy.",
    explorerBadge: "Space explorer",
    explorerDesc: "Complete six different missions.",
    steadyBadge: "Star consistency",
    steadyDesc: "Practice on three different days.",
    earned: "Earned",
    pending: "In progress",
    tip: "A tip from ATIBOT",
    tipText:
      "Place your index fingers on F and J. Breathe, look at the text and type calmly.",
    privacy: "A safe learning space. No advertising or public profiles.",
    missionTitle: "Your mission",
    practice: "Free practice",
    evaluated: "Assessed mission",
    start: "Start",
    back: "Back to map",
    pause: "Pause",
    resume: "Resume",
    paused: "Paused. Resume when you are ready.",
    typeHere: "Type here to begin…",
    typeHint:
      "Start with the first letter. Backspace corrects; mistakes count. Pasting is blocked.",
    practiceHint:
      "No pressure or score. Practice is saved, but does not unlock missions.",
    time: "Active time",
    target: "Target",
    resultTitle: "Mission accomplished!",
    practiceResult: "Practice complete!",
    resultSub: "Every attempt is a step towards a new world.",
    errors: "Keys to practice",
    noErrors: "No mistakes! Well done.",
    previous: "Compared with your previous best",
    firstAttempt: "This is your first assessed attempt.",
    accuracyAdvice:
      "Slowly practice the highlighted keys. Accuracy comes first.",
    speedAdvice:
      "Great accuracy! Keep practicing your rhythm to reach the target.",
    greatAdvice: "Excellent balance between accuracy and rhythm!",
    repeat: "Repeat mission",
    next: "Next mission",
    abandon: "Leave mission",
    abandonConfirm:
      "Leave? This incomplete attempt will be saved without a rating or points.",
    saving: "Saving…",
    saved: "Changes saved",
    history: "Attempt history",
    date: "Date",
    level: "Level",
    language: "Exercise language",
    status: "Status",
    abandoned: "Incomplete",
    best: "Best results",
    allAttempts: "All attempts",
    evolution: "Your progress",
    accuracyEvolution: "Accuracy in recent attempts",
    wpmEvolution: "WPM in recent attempts",
    noHistory: "No attempts yet. Your first mission awaits.",
    personal: "Personal recognitions",
    improvement: "Improvement",
    improvementDesc:
      "Improve a mission’s accuracy compared with your first attempt.",
    constancy: "Consistency",
    constancyDesc: "Your practice time deserves recognition too.",
    precision: "Accuracy",
    precisionRecognition: "Learn at your own pace, calmly and carefully.",
    rankingOff:
      "Your teacher has hidden the leaderboard. Your progress still counts.",
    weeklyRules:
      "Each mission contributes its best attempt of the week. Only challenge missions count. Ties: accuracy, then less active time.",
    timezone: "Monday to Sunday · Europe/Madrid",
    position: "Position",
    alias: "Alias",
    points: "Points",
    createClass: "Create class",
    className: "Class name",
    edit: "Edit",
    archive: "Archive",
    restore: "Restore",
    archived: "Archived",
    students: "Students",
    newStudent: "Create student",
    email: "Email (optional)",
    accountName: "Username",
    class: "Class",
    noClass: "No class",
    save: "Save",
    cancel: "Cancel",
    resetPassword: "Reset password",
    newPassword: "New password (at least 8 characters)",
    move: "Move / remove",
    assign: "Assign missions",
    sequence: "Mission sequence",
    addLevel: "Add mission",
    remove: "Remove",
    reorder: "Order",
    unlock: "Unlock accuracy (%)",
    prerequisite: "Explicit prerequisite",
    automatic: "Previous mission (automatic)",
    weeklyChallenge: "Included in weekly challenge",
    leaderboardEnabled: "Show weekly leaderboard",
    scoreRules: "Rating parameters",
    weight: "Accuracy weight (0–1)",
    thresholds: "Thresholds for 2, 3, 4 and 5 ATIBOTS",
    cap2: "Minimum accuracy to exceed 2 ATIBOTS",
    cap3: "Minimum accuracy to exceed 3 ATIBOTS",
    five: "Minimum accuracy for 5 ATIBOTS",
    assignmentNote:
      "Removing a mission preserves its history. Each mission requires the stated accuracy in its prerequisite.",
    newLevel: "Create mission",
    clone: "Copy and edit",
    name: "Name",
    mode: "Game mode",
    text: "Text to practice",
    publish: "Published",
    draft: "Draft",
    contentLanguage: "Content language",
    targetWpm: "Target WPM",
    all: "All",
    from: "From",
    to: "To",
    filter: "Filter",
    export: "Export CSV",
    assigned: "Assigned",
    lastActivity: "Last activity",
    mostErrors: "Frequent errors",
    attempts: "Attempts",
    reportNote:
      "Averages: all completed assessed attempts. Best: one result per mission, selected by score. Practices and incomplete attempts are shown separately.",
    classSummary: "Student summary",
    assignmentFor: "Assignment for",
    personalAssign: "Assign individually",
    none: "None",
    deleteContent: "Content with history is retained; you can make it a draft.",
    score: "Score",
    sound: "Sound",
    motion: "Reduce motion",
    loading: "Loading…",
    error: "The operation could not be completed.",
    invalid_login: "Incorrect username or password.",
    unauthenticated: "Your session has ended. Please sign in again.",
    forbidden: "You do not have permission for this action.",
    level_locked: "This mission is not available.",
    password_length: "Password must contain 8 to 200 characters.",
    conflict: "Username or email already exists, or the record conflicts.",
    invalid_input: "Check the form fields.",
    invalid_level: "Check the mission text, language and targets.",
    invalid_rules: "Check the rating parameters.",
    rate_limited: "Too many attempts. Wait five minutes.",
    incomplete: "Complete the text before submitting.",
    invalid_time: "Active time is invalid.",
    implausible_speed: "The recorded speed is implausible.",
    invalid_events: "The keystrokes could not be validated.",
    invalid_run: "This attempt has already been sent or is invalid.",
    shared_level_readonly: "Copy this mission to edit it.",
    server_error: "Server error. Check the log.",
    castle: "Orbital castle defense",
    race: "Spacecraft race",
    bridge: "Rune bridge",
    dragon: "Mechanical dragon",
    explore: "Planet exploration",
    portal: "Galactic portal",
    castleInstruction:
      "Complete words to charge the shields and push the meteor away.",
    raceInstruction: "Each completed word propels your ship toward the finish.",
    bridgeInstruction:
      "Each correct sequence builds another rune in the bridge.",
    dragonInstruction:
      "Recover parts by completing words and restore the dragon’s color.",
    exploreInstruction:
      "Type the instructions and gather resources for your expedition.",
    portalInstruction:
      "Each correct character charges the portal. Complete the text to open it.",
    ready: "Ready",
    personalBest: "Personal best",
    recognitionProgress: "{n} practice days",
    noData: "No data",
    challenge: "WEEKLY CHALLENGE",
    active: "Active",
    bestBots: "Best rating",
    allModes: "SIX WAYS TO LEARN",
    clear: "Clear",
    go: "Let’s go",
    exportNote:
      "CSV includes filtered results, practices and incomplete attempts.",
    weekStart: "Monday of the week",
    assignmentSaved: "Assignment saved. History is preserved.",
    usernameHelp:
      "Share these credentials privately. The password cannot be viewed afterwards.",
    orderHelp: "Order is numeric. Use intermediate positions to reorder.",
    assignmentLanguage: "Interface and exercise language are independent.",
    credentials: "Credentials",
    sessionExpired: "Your session ended; the local attempt was not submitted.",
    retry: "Retry submission",
    errorsCorrected: "Corrected mistakes also count towards accuracy.",
    loginDemoWarning:
      "Local demo. Change passwords before exposing this service.",
    activeStudents: "Enrolled students",
    delete: "Delete",
    levelsDone: "Completed",
    help: "Help",
    studentDetail: "Student report",
    exerciseOnly: "Assigned text",
    rulesHint: "5 ATIBOTS also requires reaching the WPM target.",
    unitMinutes: "min",
    backspaceHint: "Backspace corrects. Held keys do not repeat.",
    practiceWithoutPressure: "Practice without a countdown",
    weekHistory: "Weekly history",
    hide: "Hide",
    reportTime: "Active time (s)",
    badgeProgress: "Complete missions to earn recognitions.",
  },
};
const $ = (selector) => document.querySelector(selector);
const esc = (value) =>
  String(value ?? "").replace(
    /[&<>"']/g,
    (ch) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        ch
      ],
  );
const state = {
  language: localStorage.getItem("atigra-language") || "es",
  sound: localStorage.getItem("atigra-sound") === "true",
  motion:
    localStorage.getItem("atigra-motion") === "true" ||
    matchMedia("(prefers-reduced-motion: reduce)").matches,
  user: null,
  csrf: null,
  page: "map",
  teacherTab: "classes",
  student: null,
  teacher: null,
  planets: [],
  game: null,
  reportRows: [],
  reportFilters: {},
  week: null,
  demo: true,
};
const t = (key, args = {}) => {
  let text = dictionary[state.language][key] || key;
  for (const [k, v] of Object.entries(args))
    text = text.replaceAll("{" + k + "}", v);
  return text;
};
const number = (n, d = 1) =>
  Number(n || 0).toLocaleString(state.language, { maximumFractionDigits: d });
const date = (value) =>
  value
    ? new Date(value).toLocaleString(state.language, {
        timeZone: "Europe/Madrid",
        dateStyle: "short",
        timeStyle: "short",
      })
    : "—";
const duration = (ms) =>
  `${Math.floor(ms / 60000)}:${String(Math.floor(ms / 1000) % 60).padStart(2, "0")}`;
function bot(size = "") {
  return `<span class="bot ${size}" aria-hidden="true"><span class="antenna"></span><span class="head"><span class="face"><span class="eye"></span><span class="eye"></span></span></span><span class="body"></span><span class="arm"></span><span class="arm right"></span><span class="foot"></span><span class="foot right"></span></span>`;
}
function bots(n) {
  return `<span class="bots" role="img" aria-label="${n} ${t("bots")}">${Array.from({ length: 5 }, (_, i) => `<span class="bot-slot ${i < n ? "" : "empty"}">${bot("tiny")}</span>`).join("")}</span>`;
}
function badge(label, kind = "") {
  return `<span class="badge ${kind}">${esc(label)}</span>`;
}
function stat(value, label, icon) {
  return `<div class="stat"><span class="stat-icon" aria-hidden="true">${icon}</span><div><div class="stat-value pixel">${value}</div><div class="stat-label">${t(label)}</div></div></div>`;
}
function field(key, html, full = false) {
  return `<label class="${full ? "full" : ""}">${t(key)}${html}</label>`;
}
function input(name, value = "", type = "text", extra = "") {
  return `<input name="${name}" type="${type}" value="${esc(value)}" ${extra}>`;
}
function select(name, options, value = "", extra = "") {
  return `<select name="${name}" ${extra}>${options.map(([v, l]) => `<option value="${esc(v)}" ${String(v) === String(value) ? "selected" : ""}>${esc(l)}</option>`).join("")}</select>`;
}
function check(name, value, label) {
  return `<label class="checkbox"><input type="checkbox" name="${name}" ${value ? "checked" : ""}>${t(label)}</label>`;
}
function languagePicker() {
  return `<div class="language" aria-label="Language / Idioma"><button data-language="es" class="${state.language === "es" ? "active" : ""}" aria-pressed="${state.language === "es"}">ES</button><button data-language="en" class="${state.language === "en" ? "active" : ""}" aria-pressed="${state.language === "en"}">EN</button></div>`;
}
function toast(message) {
  $("#toast").textContent = message;
  $("#toast").classList.add("visible");
  clearTimeout(toast.timer);
  toast.timer = setTimeout(() => $("#toast").classList.remove("visible"), 4500);
}
async function api(path, data) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 15000);
  try {
    let response;
    try {
      response = await fetch(path, {
        credentials: "same-origin",
        method: data === undefined ? "GET" : "POST",
        headers:
          data === undefined
            ? {}
            : {
                "Content-Type": "application/json",
                "X-CSRF-Token": state.csrf || "",
              },
        body: data === undefined ? undefined : JSON.stringify(data),
        signal: controller.signal,
      });
    } catch (error) {
      throw new Error(
        t(
          error.name === "AbortError" ? "requestTimeout" : "backendUnavailable",
        ),
      );
    }
    if (
      !(response.headers.get("Content-Type") || "").includes("application/json")
    ) {
      throw new Error(t("backendUnavailable"));
    }
    let result;
    try {
      result = await response.json();
    } catch (error) {
      throw new Error(
        t(
          error.name === "AbortError" ? "requestTimeout" : "backendUnavailable",
        ),
      );
    }
    if (!response.ok) {
      const error = new Error(t(result.error) || t("error"));
      error.code = result.error;
      throw error;
    }
    return result;
  } finally {
    clearTimeout(timeout);
  }
}

function errorMessage(error) {
  toast(error.message || t("error"));
}
function brand() {
  return `<div class="brand-wrap"><div class="brand">ati<span>gra</span><span class="small" style="color:inherit"> /</span></div><div class="brand-sub">${t("tagline")}</div></div>`;
}
function setPage(page) {
  if (state.game) {
    if (!confirm(t("abandonConfirm"))) return;
    abandon(page);
    return;
  }
  state.page = page;
  refresh().catch(errorMessage);
}
async function refresh() {
  if (state.user.role === "student")
    state.student = await api(
      "/api/student" + (state.week ? "?week=" + state.week : ""),
    );
  else state.teacher = await api("/api/teacher");
  render();
}
function render() {
  document.documentElement.lang = state.language;
  document.body.classList.toggle("reduced", state.motion);
  if (!state.user) return renderLogin();
  const teacher = state.user.role === "teacher";
  const nav = teacher
    ? [
        ["classes", "▦"],
        ["levels", "◇"],
        ["reports", "▥"],
      ]
    : [
        ["map", "⊙"],
        ["progress", "↗"],
        ["ranking", "♜"],
      ];
  $("#app").innerHTML =
    `<div class="shell"><aside class="sidebar">${brand()}<div class="nav-label">${t(teacher ? "academy" : "journey")}</div><nav class="nav" aria-label="${t("academy")}">${nav.map(([page, icon]) => `<button data-page="${page}" class="${state.page === page ? "active" : ""}" ${state.page === page ? 'aria-current="page"' : ""}><span class="nav-icon" aria-hidden="true">${icon}</span>${t(page)}</button>`).join("")}</nav><div class="sidebar-bottom"><div class="bot-help">${bot()}<div><strong>${t("tip")}</strong><p>${t("tipText")}</p></div></div><div class="userbox"><div class="avatar">${esc(state.user.alias.slice(0, 1))}</div><div><div class="name">${esc(state.user.alias)}</div><div class="small muted">${t(state.user.role)}</div></div><button data-action="logout" class="toggle" title="${t("logout")}" aria-label="${t("logout")}">⇥</button></div></div></aside><div class="main-wrap"><header class="topbar"><span class="breadcrumb">ATIBOT Academy <span aria-hidden="true"> / </span> ${t(state.game ? "mission" : state.page)}</span><div class="top-actions"><span class="badge purple">✦ ${t("academy")}</span>${languagePicker()}<button class="toggle" data-action="sound" aria-label="${t("sound")}" title="${t("sound")}" aria-pressed="${state.sound}">${state.sound ? "♫" : "♪̸"}</button><button class="toggle" data-action="motion" aria-label="${t("motion")}" title="${t("motion")}" aria-pressed="${state.motion}">◌</button><button class="toggle" data-action="logout" aria-label="${t("logout")}" title="${t("logout")}">⇥</button></div></header><main id="main" tabindex="-1">${state.game ? gameView() : teacher ? teacherView() : studentView()}<footer class="footnote"><span>⌨ ${t("physical")}</span><span>${t("provisional")}</span></footer></main></div></div>`;
  bindCommon();
  if (state.game) bindGame();
  else if (teacher) {
    bindTeacher();
    if (state.page === "reports") loadReports();
  } else bindStudent();
}
function renderLogin() {
  document.documentElement.lang = state.language;
  $("#app").innerHTML =
    `<div class="login"><section class="login-space">${brand()}<div class="login-copy"><span class="eyebrow" style="color:#9edf9f">ATIBOT ACADEMY</span><h1>${t("loginTitle")}</h1><p>${t("loginIntro")}</p></div><div class="login-art">${bot("big")}</div><div class="footnote"><span>${t("physical")}</span><span>${t("provisional")}</span></div></section><main id="main" class="login-form-wrap"><div class="login-language">${languagePicker()}</div><div class="login-form"><span class="eyebrow">${t("academy")}</span><h2>${t("welcomeBack")}</h2><p>${t("loginSubtitle")}</p><form id="login-form" novalidate>${field("username", input("login", "", "text", 'required autocomplete="username"'))}${field("password", input("password", "", "password", 'required autocomplete="current-password" maxlength="200"'))}<p class="error" id="login-error" role="alert"></p><button class="primary" type="submit">${t("login")} <span aria-hidden="true">→</span></button></form>${state.demo ? `<div class="demo-box"><span class="eyebrow">${t("demo")}</span><p>${t("demoInfo")}</p><button data-demo="nova.demo">${t("student")} · Nova</button><button data-demo="profe.demo">${t("teacher")}</button><p>${t("loginDemoWarning")}</p></div>` : ""}<p class="small">⌨ ${t("physical")}</p></div></main></div>`;
  bindCommon();
  $("#login-form").onsubmit = async (event) => {
    event.preventDefault();
    const form = event.currentTarget;
    const errorLabel = form.querySelector("#login-error");
    const button = form.querySelector("button[type=submit]");
    const credentials = Object.fromEntries(new FormData(form));
    credentials.login = credentials.login.trim();
    errorLabel.textContent = "";
    if (!credentials.login || !credentials.password) {
      errorLabel.textContent = t("missingLogin");
      form.elements[!credentials.login ? "login" : "password"].focus();
      return;
    }
    button.disabled = true;
    button.textContent = t("signingIn");
    form.setAttribute("aria-busy", "true");
    try {
      const result = await api("/api/login", credentials);
      state.user = result.user;
      state.csrf = result.csrf;
      state.page = state.user.role === "teacher" ? "classes" : "map";
      state.planets = await api("/api/planets");
      await refresh();
    } catch (error) {
      // The original form stays usable if any request fails during startup.
      if (form.isConnected) {
        state.user = null;
        state.csrf = null;
        errorLabel.textContent = error.message;
      } else errorMessage(error);
    } finally {
      button.disabled = false;
      button.textContent = t("login");
      form.removeAttribute("aria-busy");
    }
  };
  document.querySelectorAll("[data-demo]").forEach(
    (button) =>
      (button.onclick = () => {
        const form = $("#login-form");
        form.elements.login.value = button.dataset.demo;
        form.elements.password.value = "AtigraDemo2026!";
        form.requestSubmit();
      }),
  );
}
function bindCommon() {
  document.querySelectorAll("[data-language]").forEach(
    (button) =>
      (button.onclick = () => {
        state.language = button.dataset.language;
        localStorage.setItem("atigra-language", state.language);
        if (state.game) pauseGame();
        render();
      }),
  );
  document
    .querySelectorAll("[data-page]")
    .forEach((button) => (button.onclick = () => setPage(button.dataset.page)));
  document.querySelectorAll("[data-action]").forEach(
    (button) =>
      (button.onclick = async () => {
        const action = button.dataset.action;
        if (action === "logout") {
          if (state.game) {
            if (!confirm(t("abandonConfirm"))) return;
            await abandon(null, false);
          }
          try {
            await api("/api/logout", {});
            state.user = null;
            state.game = null;
            state.week = null;
            render();
          } catch (e) {
            errorMessage(e);
          }
        }
        if (action === "sound" || action === "motion") {
          state[action] = !state[action];
          localStorage.setItem("atigra-" + action, state[action]);
          if (state.game) pauseGame();
          render();
        }
      }),
  );
}
function completedAttempts(rows) {
  return rows.filter((a) => a.completed && !a.practice);
}
function bestAttempts(rows) {
  const best = new Map();
  completedAttempts(rows).forEach((a) => {
    const key = a.student_id + ":" + a.level_id;
    const prev = best.get(key);
    if (!prev || a.score > prev.score) best.set(key, a);
  });
  return [...best.values()];
}
function mean(rows, key) {
  return rows.length
    ? rows.reduce((sum, row) => sum + row[key], 0) / rows.length
    : 0;
}
function achievements(rows) {
  const completed = completedAttempts(rows),
    best = bestAttempts(rows);
  const days = new Set(
    rows
      .filter((a) => a.active_ms > 0)
      .map((a) =>
        new Date(a.created_at).toLocaleDateString("en-CA", {
          timeZone: "Europe/Madrid",
        }),
      ),
  ).size;
  return {
    precision: completed.some((a) => a.accuracy >= 97),
    explorer: best.length >= 6,
    steady: days >= 3,
    days,
  };
}
function studentStats() {
  const rows = state.student.attempts,
    completed = completedAttempts(rows),
    best = bestAttempts(rows);
  return `<div class="stats">${stat(
    best.reduce((s, a) => s + a.bots, 0),
    "bots",
    "♟",
  )}${stat(number(mean(completed, "accuracy")) + "%", "accuracy", "◎")}${stat(number(mean(completed, "wpm")), "wpm", "↯")}${stat(best.length + "/" + state.student.levels.length, "completed", "⚑")}</div>`;
}
function studentView() {
  if (state.page === "progress") return progressView();
  if (state.page === "ranking") return rankingView();
  return mapView();
}
function nextLevel() {
  return (
    state.student.levels.find((l) => l.unlocked && !l.best) ||
    state.student.levels.find((l) => l.unlocked)
  );
}
function rankingRows(rows, limit = Infinity) {
  return rows
    .slice(0, limit)
    .map(
      (r, i) =>
        `<div class="ranking-row"><span class="ranking-place">${String(i + 1).padStart(2, "0")}</span><div class="avatar">${esc(r.alias.slice(0, 1))}</div><strong>${esc(r.alias)}</strong><span class="ranking-score pixel">${number(r.score, 0)}</span></div>`,
    )
    .join("");
}
function mapView() {
  const s = state.student,
    next = nextLevel(),
    earned = achievements(s.attempts);
  return `<section class="welcome"><div><span class="eyebrow">${t("journey")}</span><h1 style="margin:8px 0 0">${t("hello", { name: esc(state.user.alias) })} <span aria-hidden="true">✧</span></h1><p>${t("helloSub")}</p></div>${s.class ? badge(s.class.name, "green") : ""}</section><section class="hero"><div class="hero-content"><span class="eyebrow">${t("allModes")}</span><h2>${t("heroTitle")}</h2><p>${t("heroSub")}</p><button class="primary" data-start="${next?.level_id || ""}" ${next ? "" : "disabled"}>${t("continue")} <span aria-hidden="true">→</span></button></div><div class="hero-art" aria-hidden="true"><span class="orbit"></span><span class="orbit two"></span><span class="mini-planet"></span>${bot("big")}</div></section>${studentStats()}<div class="section-head"><div><h2>${t("universe")}</h2><p>${t("universeSub")}</p></div>${badge("◎ " + s.levels.filter((l) => l.best).length + " / " + s.levels.length, "purple")}</div><div class="world-layout"><section class="planet-grid">${
    s.levels.length
      ? state.planets
          .map((planet, index) => {
            const levels = s.levels.filter((l) => l.planet_id === planet.id),
              complete = levels.filter((l) => l.best).length,
              available = levels.some((l) => l.unlocked),
              current = next && next.planet_id === planet.id;
            return `<article class="planet-card ${available ? "" : "locked"} ${current ? "current" : ""}"><span class="planet-number">${t("planet")} ${String(index + 1).padStart(2, "0")}</span><div class="planet-art" aria-hidden="true"><span class="planet-ball">${planet.icon}</span></div><h3>${esc(planet["name_" + state.language])}</h3><p>${t("missionsCount", { n: levels.length })}</p><div class="row" style="justify-content:space-between;margin-bottom:10px">${badge(t(complete && complete === levels.length ? "finished" : available ? "available" : "locked"), complete ? "green" : "")}<span class="small muted">${complete}/${levels.length}</span></div><div class="progress"><span data-progress="${levels.length ? (complete / levels.length) * 100 : 0}"></span></div><div class="mission-list">${levels.map((l, i) => `<button class="mission-chip ${l.best ? "done" : l.unlocked ? "available" : ""}" data-start="${l.level_id}" ${l.unlocked ? "" : "disabled"} aria-label="${esc(l.name)} · ${t(l.best ? "finished" : l.unlocked ? "available" : "locked")}" title="${esc(l.name)}">${l.best ? "✓" : l.unlocked ? String(i + 1).padStart(2, "0") : "⌑"}</button>`).join("")}</div>${levels.some((l) => l.best) ? `<div style="margin-top:12px">${bots(Math.max(...levels.map((l) => l.best?.bots || 0)))}</div>` : ""}</article>`;
          })
          .join("")
      : `<div class="panel">${t("noLevels")}</div>`
  }</section><aside class="world-side"><section class="side-card"><div class="row" style="justify-content:space-between"><h3>${t("weekly")}</h3><span class="badge green">✦</span></div><p class="small muted">${t("week")} ${esc(s.week)}</p>${s.class?.leaderboard ? (s.leaderboard.length ? rankingRows(s.leaderboard, 3) : `<div class="empty-state">${t("noRanking")}</div>`) : `<p class="small muted">${t("rankingOff")}</p>`}<button data-page="ranking" class="small" style="color:var(--pink);font-weight:700;margin-top:14px">${t("viewAll")}</button></section><section class="side-card"><h3>${t("badges")}</h3>${[
    ["precision", "◎", "precisionBadge", "precisionDesc"],
    ["explorer", "✧", "explorerBadge", "explorerDesc"],
    ["steady", "♜", "steadyBadge", "steadyDesc"],
  ]
    .map(
      ([key, icon, title, desc]) =>
        `<div class="badge-row"><span class="badge-medal" ${earned[key] ? "" : 'style="filter:grayscale(1);opacity:.55"'} aria-hidden="true">${icon}</span><div><strong>${t(title)} ${earned[key] ? "✓" : ""}</strong><p>${t(desc)}</p></div></div>`,
    )
    .join("")}</section></aside></div>`;
}
function chart(rows, key) {
  const recent = completedAttempts(rows).slice(0, 14).reverse(),
    max = key === "accuracy" ? 100 : Math.max(30, ...recent.map((a) => a[key]));
  return recent.length
    ? `<div class="chart" role="img" aria-label="${t(key)}: ${recent.map((a) => number(a[key])).join(", ")}">${recent.map((a, i) => `<div class="chart-bar" data-height="${Math.max(1, (a[key] / max) * 100)}" title="${date(a.created_at)}: ${number(a[key])}"><span>${number(a[key], 0)}</span></div>`).join("")}</div>`
    : `<div class="empty-state">${t("noHistory")}</div>`;
}
function attemptTable(rows, teacher = false) {
  return `<div class="table-wrap"><table><thead><tr>${(teacher ? ["alias"] : [])
    .concat([
      "date",
      "level",
      "language",
      "status",
      "accuracy",
      "wpm",
      "time",
      "score",
      "bots",
      "errors",
    ])
    .map((k) => `<th>${t(k)}</th>`)
    .join(
      "",
    )}</tr></thead><tbody>${rows.map((a) => `<tr>${teacher ? `<td>${esc(a.alias)}</td>` : ""}<td>${date(a.created_at)}</td><td>${esc(a.name || a.level_name)}</td><td>${esc(a.language).toUpperCase()}</td><td>${badge(t(!a.completed ? "abandoned" : a.practice ? "practice" : "finished"), a.completed ? "green" : "")}</td><td>${number(a.accuracy)}%</td><td>${number(a.wpm)}</td><td>${duration(a.active_ms)}</td><td>${a.score === null ? "—" : number(a.score)}</td><td>${a.bots === null ? "—" : bots(a.bots)}</td><td>${errorKeys(a.errors)}</td></tr>`).join("")}</tbody></table></div>`;
}
function errorKeys(errors) {
  const object = typeof errors === "string" ? JSON.parse(errors) : errors;
  return (
    Object.entries(object || {})
      .sort((a, b) => b[1] - a[1])
      .slice(0, 6)
      .map(([key, count]) => `${esc(key === " " ? "␣" : key)} ×${count}`)
      .join(" · ") || "—"
  );
}
function progressView() {
  const s = state.student;
  return `<div class="welcome"><div><span class="eyebrow">ATIBOT ACADEMY</span><h1>${t("progress")}</h1><p>${t("reportNote")}</p></div></div>${studentStats()}<div class="form-grid"><section class="panel"><h2>${t("accuracyEvolution")}</h2>${chart(s.attempts, "accuracy")}</section><section class="panel"><h2>${t("wpmEvolution")}</h2>${chart(s.attempts, "wpm")}</section></div><section class="panel"><h2>${t("best")}</h2>${attemptTable(bestAttempts(s.attempts))}</section><section class="panel"><h2>${t("history")}</h2>${s.attempts.length ? attemptTable(s.attempts) : `<p class="muted">${t("noHistory")}</p>`}</section>`;
}
function rankingView() {
  const s = state.student,
    earned = achievements(s.attempts),
    first = {};
  [...completedAttempts(s.attempts)].reverse().forEach((a) => {
    first[a.level_id] ??= a;
  });
  const improved = bestAttempts(s.attempts).some(
    (a) => a.accuracy > first[a.level_id].accuracy,
  );
  return `<div class="welcome"><div><span class="eyebrow">${t("challenge")}</span><h1>${t("ranking")}</h1><p>${t("timezone")}</p></div>${s.class ? badge(s.class.name, "green") : ""}</div><section class="panel"><div class="section-head" style="margin-top:0"><h2>${t("weekly")}</h2><label>${t("weekHistory")}<select id="week-selector">${[
    ...new Set([s.week, ...s.weeks]),
  ]
    .sort()
    .reverse()
    .map(
      (w) =>
        `<option value="${w}" ${w === s.week ? "selected" : ""}>${w}</option>`,
    )
    .join(
      "",
    )}</select></label></div><p class="small muted">${t("weeklyRules")}</p>${!s.class?.leaderboard ? `<div class="empty-state">${t("rankingOff")}</div>` : s.leaderboard.length ? `<div class="table-wrap"><table><thead><tr>${["position", "alias", "points", "accuracy", "time"].map((k) => `<th>${t(k)}</th>`).join("")}</tr></thead><tbody>${s.leaderboard.map((r, i) => `<tr><td>${i + 1}</td><td><strong>${esc(r.alias)}</strong></td><td class="pixel">${number(r.score)}</td><td>${number(r.accuracy)}%</td><td>${duration(r.active_ms)}</td></tr>`).join("")}</tbody></table></div>` : `<div class="empty-state">${t("noRanking")}</div>`}</section><div class="section-head"><h2>${t("personal")}</h2></div><div class="recognitions">${[
    ["✧", "improvement", improved ? t("earned") : t("improvementDesc")],
    ["♜", "constancy", t("recognitionProgress", { n: earned.days })],
    [
      "◎",
      "precision",
      earned.precision ? t("earned") : t("precisionRecognition"),
    ],
  ]
    .map(
      ([icon, title, desc]) =>
        `<article class="recognition"><span class="medal" aria-hidden="true">${icon}</span><h3>${t(title)}</h3><p>${desc}</p></article>`,
    )
    .join("")}</div>`;
}
function bindProgress() {
  document
    .querySelectorAll("[data-progress]")
    .forEach((el) => (el.style.width = el.dataset.progress + "%"));
  document
    .querySelectorAll("[data-height]")
    .forEach((el) => (el.style.height = el.dataset.height + "%"));
}
function bindStudent() {
  bindProgress();
  document
    .querySelectorAll("[data-start]")
    .forEach(
      (button) =>
        (button.onclick = () => missionModal(Number(button.dataset.start))),
    );
  if ($("#week-selector"))
    $("#week-selector").onchange = (event) => {
      state.week = event.target.value;
      refresh().catch(errorMessage);
    };
}
function modal(title, content, onSubmit) {
  const backdrop = document.createElement("div");
  backdrop.className = "modal-backdrop";
  backdrop.innerHTML = `<section class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title"><header><h2 id="modal-title">${esc(title)}</h2><button class="modal-close" aria-label="${t("cancel")}">×</button></header>${content}</section>`;
  const previous = document.activeElement;
  document.body.append(backdrop);
  const close = () => {
    backdrop.remove();
    previous?.focus();
  };
  backdrop.querySelector(".modal-close").onclick = close;
  backdrop.querySelectorAll("[data-close]").forEach((b) => (b.onclick = close));
  backdrop.addEventListener("keydown", (event) => {
    if (event.key === "Escape") close();
    if (event.key === "Tab") {
      const nodes = [
        ...backdrop.querySelectorAll("button,input,textarea,select,a"),
      ].filter((n) => !n.disabled);
      if (event.shiftKey && document.activeElement === nodes[0]) {
        event.preventDefault();
        nodes.at(-1).focus();
      } else if (!event.shiftKey && document.activeElement === nodes.at(-1)) {
        event.preventDefault();
        nodes[0].focus();
      }
    }
  });
  const form = backdrop.querySelector("form");
  if (form && onSubmit)
    form.onsubmit = async (event) => {
      event.preventDefault();
      const submit = form.querySelector("[type=submit]");
      submit.disabled = true;
      try {
        await onSubmit(form, close);
      } catch (e) {
        const error = backdrop.querySelector(".form-error");
        if (error) error.textContent = e.message;
        else errorMessage(e);
      } finally {
        submit.disabled = false;
      }
    };
  (backdrop.querySelector("input,select,textarea,button") || backdrop).focus();
  return { element: backdrop, close };
}
function formShell(content) {
  return `<form><div class="form-grid">${content}</div><p class="error form-error" role="alert"></p><div class="row end form-actions"><button type="button" class="secondary" data-close>${t("cancel")}</button><button class="primary" type="submit">${t("save")}</button></div></form>`;
}
function missionModal(lid) {
  const level = state.student.levels.find((l) => l.level_id === lid);
  if (!level || !level.unlocked) return;
  const m = modal(
    level.name,
    `<div class="row">${badge(t(level.mode), "purple")}${badge(level.language.toUpperCase())}</div><p style="margin-top:20px">${t(level.mode + "Instruction")}</p><p class="notice">${t("physical")} · ${t("assignmentLanguage")}</p><div class="stats" style="grid-template-columns:1fr 1fr">${stat(number(level.target_wpm), "target", "↯")}${stat(level.unlock_accuracy + "%", "unlock", "◎")}</div><p class="small muted">${t("practiceWithoutPressure")}</p><div class="row"><button class="primary" id="assessed-start">${t("start")} →</button><button class="secondary" id="practice-start">${t("practice")}</button></div>`,
  );
  m.element.querySelector("#assessed-start").onclick = () => {
    m.close();
    startGame(lid, false);
  };
  m.element.querySelector("#practice-start").onclick = () => {
    m.close();
    startGame(lid, true);
  };
}
async function startGame(lid, practice) {
  try {
    const run = await api("/api/run", { level_id: lid, practice });
    state.game = {
      ...run,
      practice,
      events: [],
      buffer: [],
      elapsed: 0,
      started: null,
      paused: false,
      saving: false,
      result: null,
      composition: false,
    };
    state.page = "mission";
    render();
    $("#type-input").focus();
  } catch (error) {
    errorMessage(error);
  }
}
function activeTime() {
  const g = state.game;
  return g
    ? Math.round(
        g.elapsed + (g.started !== null ? performance.now() - g.started : 0),
      )
    : 0;
}
function pauseGame() {
  const g = state.game;
  if (!g || g.result || g.saving) return;
  if (g.started !== null) {
    g.elapsed += performance.now() - g.started;
    g.started = null;
  }
  g.paused = true;
  if ($("#type-input")) {
    $("#type-input").disabled = true;
    $("#pause-button").textContent = t("resume");
    $("#typing-status").textContent = t("paused");
  }
  updateGameStats();
}
function resumeGame() {
  const g = state.game;
  if (!g || g.result || g.saving) return;
  g.paused = false;
  if (g.events.length) g.started = performance.now();
  $("#type-input").disabled = false;
  $("#pause-button").textContent = t("pause");
  $("#typing-status").textContent = t(g.practice ? "practiceHint" : "typeHint");
  $("#type-input").focus();
}
function scene(mode) {
  const label = `<div class="scene-label">${t(mode)}</div>`,
    ground = '<div class="scene-ground"></div>';
  const contents = {
    castle: `${ground}<div class="castle"><span class="castle-door"></span><span class="shield"></span></div><div class="meteor">☄</div><div class="scene-bot">${bot()}</div>`,
    race: '<div class="race-track"></div><div class="race-ship">🚀</div><div class="finish">⚑</div>',
    bridge: `${ground}<div class="bridge-blocks">${Array.from({ length: 10 }, () => '<span class="rune">✧</span>').join("")}</div><div class="bridge-traveler">${bot()}</div>`,
    dragon: `${ground}<div class="dragon">🐉</div><div class="dragon-parts">${["⚙", "⌁", "⚙", "✦", "⚙"].map((x) => `<span>${x}</span>`).join("")}</div>`,
    explore: `${ground}<div class="resource-grid">${["◇", "✦", "◇", "✦", "◇"].map((x) => `<span>${x}</span>`).join("")}</div><div class="explorer">${bot()}</div>`,
    portal: `<div class="portal-ring"></div><div class="portal-bot">${bot()}</div><div class="charge"><span></span></div>`,
  };
  return `<div class="game-scene" id="game-scene" aria-label="${t(mode)}">${label}${contents[mode]}</div>`;
}
function gameView() {
  const g = state.game,
    l = g.level;
  if (g.result) return resultView();
  return `<div class="game-layout"><header class="game-heading"><div><span class="eyebrow">${t(g.practice ? "practice" : "evaluated")} · ${l.language.toUpperCase()}</span><h1 style="margin:8px 0 0">${esc(l.name)}</h1></div><button class="secondary" id="leave-button">${t("abandon")}</button></header><p class="small muted" style="margin:12px 0">${t(l.mode + "Instruction")}</p>${scene(l.mode)}<div class="game-stats"><div><strong id="game-accuracy" class="pixel">100%</strong><span>${t("accuracy")}</span></div><div><strong id="game-wpm" class="pixel">0</strong><span>${t("wpm")}</span></div><div><strong id="game-time" class="pixel">0:00</strong><span>${t("time")}</span></div><div><strong class="pixel">${l.target_wpm}</strong><span>${t("target")}</span></div></div><section class="typing-card"><div class="row" style="justify-content:space-between">${badge(t(g.practice ? "practice" : "evaluated"), g.practice ? "green" : "")}<button class="secondary" id="pause-button">${t(g.paused ? "resume" : "pause")}</button></div><div id="typing-text" class="typing-text" aria-label="${t("exerciseOnly")}"></div><label class="small muted" for="type-input">${t("typeHere")}</label><input id="type-input" class="type-input" type="text" autocomplete="off" autocorrect="off" spellcheck="false" autocapitalize="off" aria-describedby="typing-status" ${g.paused || g.saving ? "disabled" : ""}><p id="typing-status" class="small muted" role="status">${t(g.saving ? "saving" : g.paused ? "paused" : g.practice ? "practiceHint" : "typeHint")}</p><p class="small muted">${t("backspaceHint")}</p><div id="retry-area"></div></section><div id="keyboard" class="keyboard" aria-hidden="true"></div></div>`;
}
function progressRatio() {
  const g = state.game;
  let prefix = 0;
  while (
    prefix < g.buffer.length &&
    g.buffer[prefix] === Array.from(g.level.text)[prefix]
  )
    prefix++;
  if (g.level.mode === "portal")
    return prefix / Array.from(g.level.text).length;
  const text = g.level.text,
    boundaries = [...text.matchAll(/\s/g)]
      .map((m) => m.index + 1)
      .concat(text.length);
  return boundaries.filter((n) => n <= prefix).length / boundaries.length;
}
function updateGame() {
  const g = state.game;
  if (!g || g.result) return;
  const text = Array.from(g.level.text);
  $("#typing-text").innerHTML = text
    .map(
      (ch, i) =>
        `<span class="${i < g.buffer.length ? (g.buffer[i] === ch ? "correct" : "wrong") : i === g.buffer.length ? "cursor" : ""}">${esc(ch)}</span>`,
    )
    .join("");
  $("#type-input").value = g.buffer.join("");
  const next = text[g.buffer.length] || "";
  const rows =
    g.level.language === "es"
      ? ["qwertyuiop", "asdfghjklñ", "zxcvbnm"]
      : ["qwertyuiop", "asdfghjkl", "zxcvbnm"];
  $("#keyboard").innerHTML =
    rows
      .map(
        (row) =>
          `<div class="keyboard-row">${Array.from(row)
            .map(
              (ch) =>
                `<span class="key ${["f", "j"].includes(ch) ? "home" : ""} ${ch === next.toLowerCase() ? "next" : ""}">${ch.toUpperCase()}</span>`,
            )
            .join("")}</div>`,
      )
      .join("") +
    `<div class="keyboard-row"><span class="key space ${next === " " ? "next" : ""}">${t("space")}</span></div>`;
  const ratio = progressRatio(),
    scene = $("#game-scene");
  scene.style.setProperty("--progress", ratio * 100 + "%");
  scene.style.setProperty("--ship", 8 + ratio * 72 + "%");
  scene.style.setProperty("--shield", 0.15 + ratio * 0.85);
  scene.style.setProperty("--meteor", 65 + ratio * 25 + "%");
  scene.style.setProperty("--damage", 1 - ratio);
  scene.style.setProperty("--glow", ratio * 40 + "px");
  scene.style.setProperty("--portal-scale", 0.8 + ratio * 0.25);
  scene
    .querySelectorAll(".rune")
    .forEach((el, i) =>
      el.classList.toggle("built", i < Math.floor(ratio * 10)),
    );
  scene
    .querySelectorAll(".dragon-parts span")
    .forEach((el, i) =>
      el.classList.toggle("repaired", i < Math.floor(ratio * 5)),
    );
  scene
    .querySelectorAll(".resource-grid span")
    .forEach((el, i) =>
      el.classList.toggle("collected", i < Math.floor(ratio * 5)),
    );
  updateGameStats();
}
function localStats() {
  const g = state.game;
  let buffer = [],
    correct = 0,
    typed = 0;
  for (const e of g.events) {
    if (e.kind === "backspace") {
      buffer.pop();
      continue;
    }
    if (e.char === Array.from(g.level.text)[buffer.length]) correct++;
    typed++;
    buffer.push(e.char);
  }
  const good = buffer.filter(
    (ch, i) => ch === Array.from(g.level.text)[i],
  ).length;
  return {
    accuracy: typed ? (correct / typed) * 100 : 100,
    wpm: activeTime() ? good / 5 / (activeTime() / 60000) : 0,
  };
}
function updateGameStats() {
  if (!state.game || state.game.result || !$("#game-time")) return;
  const s = localStats();
  $("#game-time").textContent = duration(activeTime());
  $("#game-accuracy").textContent = number(s.accuracy, 0) + "%";
  $("#game-wpm").textContent = number(s.wpm, 0);
}
function recordChar(char) {
  const g = state.game;
  if (!g || g.paused || g.saving || g.result) return;
  char = char.normalize("NFC");
  if (
    Array.from(char).length !== 1 ||
    g.buffer.length >= Array.from(g.level.text).length
  )
    return;
  if (g.started === null) g.started = performance.now();
  g.events.push({ kind: "char", char, t: activeTime() });
  g.buffer.push(char);
  if (g.events.length > 20000) {
    pauseGame();
    toast(t("invalid_events"));
    return;
  }
  updateGame();
  if (g.buffer.join("") === g.level.text) {
    stopClock();
    finishGame();
  }
}
function recordBackspace() {
  const g = state.game;
  if (!g || g.paused || g.saving || !g.buffer.length) return;
  g.events.push({ kind: "backspace", t: activeTime() });
  g.buffer.pop();
  updateGame();
}
function stopClock() {
  const g = state.game;
  if (g?.started !== null) {
    g.elapsed += performance.now() - g.started;
    g.started = null;
  }
}
function bindGame() {
  const g = state.game;
  if (g.result) {
    $("#result-repeat").onclick = () => {
      const { level, practice } = g;
      state.game = null;
      startGame(level.level_id, practice);
    };
    $("#result-back").onclick = () => {
      state.game = null;
      state.page = "map";
      refresh().catch(errorMessage);
    };
    if ($("#result-next"))
      $("#result-next").onclick = () => {
        const next = nextLevel();
        state.game = null;
        if (next) startGame(next.level_id, false);
        else {
          state.page = "map";
          render();
        }
      };
    return;
  }
  const input = $("#type-input");
  input.onkeydown = (event) => {
    if (event.repeat) {
      event.preventDefault();
      return;
    }
    if (event.key === "Escape") {
      event.preventDefault();
      pauseGame();
      $("#pause-button").focus();
      return;
    }
    if (event.key === "Backspace") {
      event.preventDefault();
      recordBackspace();
      return;
    }
    if (event.ctrlKey || event.metaKey || event.altKey) return;
    if (
      !event.isComposing &&
      !g.composition &&
      Array.from(event.key).length === 1
    ) {
      event.preventDefault();
      recordChar(event.key);
    }
  };
  input.onpaste = (event) => event.preventDefault();
  input.ondrop = (event) => event.preventDefault();
  input.addEventListener("compositionstart", () => {
    g.composition = true;
  });
  input.addEventListener("compositionend", (event) => {
    g.composition = false;
    recordChar(event.data);
    input.value = g.buffer.join("");
  });
  input.onbeforeinput = (event) => {
    if (!event.isComposing && !g.composition) {
      event.preventDefault();
      if (event.inputType === "insertText" && event.data)
        recordChar(event.data);
    }
  };
  input.oninput = () => {
    if (!g.composition) input.value = g.buffer.join("");
  };
  input.onblur = () => {
    if (!g.saving && !g.result) pauseGame();
  };
  // Keep the input focused until the explicit pause action runs.
  // Otherwise its blur handler pauses first and the click resumes immediately.
  $("#pause-button").onpointerdown = (event) => event.preventDefault();
  $("#pause-button").onclick = () => (g.paused ? resumeGame() : pauseGame());
  $("#leave-button").onclick = () => {
    if (confirm(t("abandonConfirm"))) abandon("map");
  };
  updateGame();
}
async function finishGame() {
  const g = state.game;
  g.saving = true;
  $("#type-input").disabled = true;
  $("#typing-status").textContent = t("saving");
  try {
    g.result = await api("/api/attempt", {
      run_id: g.run_id,
      events: g.events,
      active_ms: Math.max(1, activeTime()),
    });
    g.saving = false;
    state.student = await api("/api/student");
    rewardSound();
    render();
    $("#main").focus();
  } catch (error) {
    g.saving = false;
    $("#typing-status").textContent = error.message;
    $("#retry-area").innerHTML =
      `<button class="primary" id="retry-submit">${t("retry")}</button>`;
    $("#retry-submit").onclick = finishGame;
  }
}
async function abandon(page = "map", rerender = true) {
  const g = state.game;
  if (!g) return;
  stopClock();
  if (!g.result) {
    try {
      await api("/api/attempt", {
        run_id: g.run_id,
        events: g.events,
        active_ms: activeTime(),
        abandoned: true,
      });
    } catch (error) {
      errorMessage(error);
      return;
    }
  }
  state.game = null;
  if (page) state.page = page;
  if (rerender) await refresh();
}
function resultView() {
  const g = state.game,
    { attempt: a, previous } = g.result;
  const errors = JSON.parse(a.errors);
  const advice =
    a.accuracy < 90
      ? "accuracyAdvice"
      : a.wpm < g.level.target_wpm
        ? "speedAdvice"
        : "greatAdvice";
  return `<section class="result game-layout"><span class="eyebrow">${esc(g.level.name)} · ${g.level.language.toUpperCase()}</span><h1>${t(g.practice ? "practiceResult" : "resultTitle")}</h1><p class="muted">${t("resultSub")}</p>${g.practice ? `<div class="hero-art" style="margin:auto">${bot()}</div>` : bots(a.bots)}<div class="stats">${stat(number(a.accuracy) + "%", "accuracy", "◎")}${stat(number(a.wpm), "wpm", "↯")}${stat(duration(a.active_ms), "time", "◷")}${stat(a.score === null ? "—" : number(a.score), "score", "✧")}</div><p class="result-message">${t(advice)}</p><div class="form-grid"><section class="panel"><h2>${t("errors")}</h2><p class="pixel">${Object.keys(errors).length ? errorKeys(errors) : t("noErrors")}</p><p class="small muted">${t("errorsCorrected")}</p></section><section class="panel"><h2>${t("previous")}</h2>${previous ? `<p>${t("accuracy")}: <strong>${number(a.accuracy - previous.accuracy)} pp</strong><br>${t("wpm")}: <strong>${number(a.wpm - previous.wpm)}</strong></p>` : `<p class="muted">${t("firstAttempt")}</p>`}</section></div><div class="row" style="justify-content:center"><button class="secondary" id="result-back">${t("back")}</button><button class="secondary" id="result-repeat">${t("repeat")}</button>${!g.practice ? `<button class="primary" id="result-next">${t("next")} →</button>` : ""}</div></section>`;
}
function rewardSound() {
  if (!state.sound) return;
  try {
    const context = new AudioContext();
    [523, 659, 784].forEach((f, i) => {
      const oscillator = context.createOscillator(),
        gain = context.createGain();
      oscillator.connect(gain);
      gain.connect(context.destination);
      oscillator.frequency.value = f;
      gain.gain.setValueAtTime(0.035, context.currentTime + i * 0.12);
      gain.gain.exponentialRampToValueAtTime(
        0.001,
        context.currentTime + i * 0.12 + 0.2,
      );
      oscillator.start(context.currentTime + i * 0.12);
      oscillator.stop(context.currentTime + i * 0.12 + 0.2);
    });
    setTimeout(() => context.close(), 1000);
  } catch {}
}
window.addEventListener("blur", pauseGame);
document.addEventListener("visibilitychange", () => {
  if (document.hidden) pauseGame();
});
window.addEventListener("beforeunload", (event) => {
  if (state.game && !state.game.result) {
    event.preventDefault();
    event.returnValue = "";
  }
});
setInterval(updateGameStats, 250);
function teacherView() {
  const data = state.teacher;
  if (state.page === "levels") return levelsView();
  if (state.page === "reports") return reportsView();
  return `<div class="welcome"><div><span class="eyebrow">${t("teacher")} · ATIBOT ACADEMY</span><h1>${t("classes")}</h1><p>${t("hello", { name: esc(state.user.alias) })}</p></div><button class="primary" id="create-class">＋ ${t("createClass")}</button></div><div class="stats">${stat(data.classes.filter((c) => !c.archived).length, "classes", "▦")}${stat(data.students.length, "students", "♧")}${stat(data.levels.filter((l) => l.published).length, "levels", "◇")}${stat(
    data.classes.reduce(
      (s, c) => s + c.assignments.filter((a) => a.active).length,
      0,
    ),
    "assigned",
    "⚑",
  )}</div>${data.classes
    .map(
      (cls) =>
        `<section class="panel"><div class="section-head" style="margin-top:0"><div><h2>${esc(cls.name)} ${cls.archived ? badge(t("archived")) : badge(t("active"), "green")}</h2><p>${data.students.filter((s) => s.class_id === cls.id).length} ${t("students")} · ${cls.assignments.filter((a) => a.active).length} ${t("levels")} · ${t("weekly")}: ${t(cls.leaderboard ? "active" : "hide")}</p></div><div class="row"><button class="secondary" data-edit-class="${cls.id}">${t("edit")}</button><button class="secondary" data-archive="${cls.id}">${t(cls.archived ? "restore" : "archive")}</button><button class="primary" data-sequence="${cls.id}">${t("assign")}</button></div></div><div class="table-wrap"><table><thead><tr>${["alias", "accountName", "credentials", "class", "reports"].map((k) => `<th>${t(k)}</th>`).join("")}</tr></thead><tbody>${data.students
          .filter((s) => s.class_id === cls.id)
          .map(studentRow)
          .join(
            "",
          )}</tbody></table></div><button class="secondary" data-new-student="${cls.id}" style="margin-top:16px">＋ ${t("newStudent")}</button></section>`,
    )
    .join(
      "",
    )}<section class="panel"><div class="section-head" style="margin-top:0"><h2>${t("students")} · ${t("noClass")}</h2><button class="secondary" data-new-student="">＋ ${t("newStudent")}</button></div><div class="table-wrap"><table><tbody>${data.students
    .filter((s) => !s.class_id)
    .map(studentRow)
    .join(
      "",
    )}</tbody></table></div></section><p class="notice">${t("assignmentNote")}</p>`;
}
function studentRow(s) {
  return `<tr><td><strong>${esc(s.alias)}</strong></td><td>${esc(s.username)}</td><td><button class="secondary" data-password="${s.id}">${t("resetPassword")}</button></td><td><button class="secondary" data-move="${s.id}">${t("move")}</button><button class="secondary" data-individual="${s.id}">${t("personalAssign")}</button></td><td><button class="secondary" data-report-student="${s.id}">${t("reports")} →</button></td></tr>`;
}
function levelsView() {
  const levels = state.teacher.levels;
  return `<div class="welcome"><div><span class="eyebrow">${t("teacher")}</span><h1>${t("levels")}</h1><p>${t("assignmentLanguage")}</p></div><button class="primary" id="new-level">＋ ${t("newLevel")}</button></div><div class="row"><label>${t("language")}${select(
    "filter-language",
    [
      ["", t("all")],
      ["es", "ES"],
      ["en", "EN"],
    ],
  )}</label></div><section class="panel"><div class="table-wrap"><table id="levels-table"><thead><tr>${["name", "planet", "mode", "language", "targetWpm", "unlock", "status", "edit"].map((k) => `<th>${t(k)}</th>`).join("")}</tr></thead><tbody>${levels.map((l) => `<tr data-level-lang="${l.language}"><td><strong>${esc(l.name)}</strong><br><span class="small muted">${esc(l.text.slice(0, 60))}</span></td><td>${esc(state.planets.find((p) => p.id === l.planet_id)?.["name_" + state.language])}</td><td>${t(l.mode)}</td><td>${l.language.toUpperCase()}</td><td>${l.target_wpm}</td><td>${l.unlock_accuracy}%</td><td>${badge(t(l.published ? "publish" : "draft"), l.published ? "green" : "")}</td><td><button class="secondary" data-edit-level="${l.id}">${t(l.owner_id ? "edit" : "clone")}</button>${l.owner_id ? `<button class="secondary" data-clone-level="${l.id}">${t("clone")}</button><button class="secondary danger" data-delete-level="${l.id}">${t("delete")}</button>` : ""}</td></tr>`).join("")}</tbody></table></div></section><p class="notice">${t("deleteContent")}</p>`;
}
function reportsView() {
  const d = state.teacher,
    f = state.reportFilters;
  return `<div class="welcome"><div><span class="eyebrow">${t("teacher")}</span><h1>${t("reports")}</h1><p>${t("reportNote")}</p></div><button class="secondary" id="export-csv">↓ ${t("export")}</button></div><section class="panel"><form id="report-filters"><div class="form-grid">${field("class", select("class_id", [["", t("all")], ...d.classes.map((c) => [c.id, c.name])], f.class_id))}${field("student", select("student_id", [["", t("all")], ...d.students.map((s) => [s.id, s.alias])], f.student_id))}${field("level", select("level_id", [["", t("all")], ...d.levels.map((l) => [l.id, l.name + " · " + l.language.toUpperCase()])], f.level_id))}${field(
    "language",
    select(
      "language",
      [
        ["", t("all")],
        ["es", "ES"],
        ["en", "EN"],
      ],
      f.language,
    ),
  )}${field("from", input("from", f.from || "", "date"))}${field("to", input("to", f.to || "", "date"))}</div><button class="primary form-actions" type="submit">${t("filter")}</button></form></section><div id="report-body"><p class="loading">${t("loading")}</p></div><section class="panel"><h2>${t("weekHistory")}</h2><form id="teacher-ranking"><div class="form-grid">${field(
    "class",
    select(
      "class_id",
      d.classes.map((c) => [c.id, c.name]),
    ),
  )}${field("weekStart", input("week", madridMonday(), "date", "required"))}</div><button class="secondary form-actions" type="submit">${t("ranking")}</button></form><div id="teacher-ranking-body"></div></section>`;
}
function madridMonday() {
  const parts = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Europe/Madrid",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).formatToParts(new Date());
  const get = (type) => parts.find((p) => p.type === type).value;
  const d = new Date(`${get("year")}-${get("month")}-${get("day")}T12:00:00Z`);
  d.setUTCDate(d.getUTCDate() - ((d.getUTCDay() + 6) % 7));
  return d.toISOString().slice(0, 10);
}
async function loadReports() {
  try {
    state.reportRows = await api(
      "/api/reports?" + new URLSearchParams(state.reportFilters),
    );
    if (!$("#report-body")) return;
    const rows = state.reportRows,
      complete = completedAttempts(rows),
      best = bestAttempts(rows),
      errors = {};
    rows.forEach((a) =>
      Object.entries(JSON.parse(a.errors)).forEach(
        ([k, v]) => (errors[k] = (errors[k] || 0) + v),
      ),
    );
    $("#report-body").innerHTML =
      `<div class="stats">${stat(complete.length, "attempts", "↻")}${stat(number(mean(complete, "accuracy")) + "%", "accuracy", "◎")}${stat(number(mean(complete, "wpm")), "wpm", "↯")}${stat(number(rows.reduce((s, r) => s + r.active_ms, 0) / 60000) + " " + t("unitMinutes"), "totalTime", "◷")}</div><section class="panel"><h2>${t("classSummary")}</h2><div class="table-wrap"><table><thead><tr>${["alias", "assigned", "levelsDone", "accuracy", "wpm", "totalTime", "lastActivity", "mostErrors"].map((k) => `<th>${t(k)}</th>`).join("")}</tr></thead><tbody>${state.teacher.students
        .filter(
          (s) =>
            !state.reportFilters.student_id ||
            String(s.id) === state.reportFilters.student_id,
        )
        .filter(
          (s) =>
            !state.reportFilters.class_id ||
            String(s.class_id) === state.reportFilters.class_id,
        )
        .map((s) => {
          const all = rows.filter((a) => a.student_id === s.id),
            c = completedAttempts(all),
            classAssignments =
              state.teacher.classes.find((cls) => cls.id === s.class_id)
                ?.assignments || [],
            personal = state.teacher.individual.filter(
              (a) => a.student_id === s.id,
            ),
            assigned = new Set(
              [...classAssignments, ...personal]
                .filter((a) => a.active)
                .map((a) => a.level_id),
            ),
            keys = {};
          all.forEach((a) =>
            Object.entries(JSON.parse(a.errors)).forEach(
              ([k, v]) => (keys[k] = (keys[k] || 0) + v),
            ),
          );
          return `<tr><td>${esc(s.alias)}</td><td>${assigned.size}</td><td>${bestAttempts(c).length}</td><td>${number(mean(c, "accuracy"))}%</td><td>${number(mean(c, "wpm"))}</td><td>${duration(all.reduce((sum, a) => sum + a.active_ms, 0))}</td><td>${date(all[0]?.created_at)}</td><td>${errorKeys(keys)}</td></tr>`;
        })
        .join(
          "",
        )}</tbody></table></div></section><div class="form-grid"><section class="panel"><h2>${t("accuracyEvolution")}</h2>${chart(rows, "accuracy")}</section><section class="panel"><h2>${t("wpmEvolution")}</h2>${chart(rows, "wpm")}</section></div><section class="panel"><h2>${t("mostErrors")}</h2><p class="pixel">${errorKeys(errors)}</p></section><section class="panel"><h2>${t("best")}</h2><p class="small muted">${t("accuracy")}: ${number(mean(best, "accuracy"))}% · ${t("wpm")}: ${number(mean(best, "wpm"))}</p>${attemptTable(best, true)}</section><section class="panel"><h2>${t("history")}</h2>${rows.length ? attemptTable(rows, true) : `<p class="muted">${t("noHistory")}</p>`}<p class="small muted">${t("exportNote")}</p></section>`;
    bindProgress();
  } catch (error) {
    errorMessage(error);
  }
}
function bindTeacher() {
  bindProgress();
  if ($("#create-class")) $("#create-class").onclick = () => classModal();
  if ($("#new-level")) $("#new-level").onclick = () => levelModal();
  document
    .querySelectorAll("[data-edit-class]")
    .forEach(
      (b) =>
        (b.onclick = () =>
          classModal(
            state.teacher.classes.find(
              (c) => c.id === Number(b.dataset.editClass),
            ),
          )),
    );
  document.querySelectorAll("[data-archive]").forEach(
    (b) =>
      (b.onclick = async () => {
        const c = state.teacher.classes.find(
          (c) => c.id === Number(b.dataset.archive),
        );
        try {
          await api("/api/class", { ...c, archived: !c.archived });
          await refresh();
          toast(t("saved"));
        } catch (e) {
          errorMessage(e);
        }
      }),
  );
  document
    .querySelectorAll("[data-new-student]")
    .forEach((b) => (b.onclick = () => studentModal(b.dataset.newStudent)));
  document
    .querySelectorAll("[data-password]")
    .forEach(
      (b) => (b.onclick = () => passwordModal(Number(b.dataset.password))),
    );
  document
    .querySelectorAll("[data-move]")
    .forEach((b) => (b.onclick = () => moveModal(Number(b.dataset.move))));
  document
    .querySelectorAll("[data-sequence]")
    .forEach(
      (b) =>
        (b.onclick = () =>
          sequenceModal("class_id", Number(b.dataset.sequence))),
    );
  document
    .querySelectorAll("[data-individual]")
    .forEach(
      (b) =>
        (b.onclick = () =>
          sequenceModal("student_id", Number(b.dataset.individual))),
    );
  document.querySelectorAll("[data-report-student]").forEach(
    (b) =>
      (b.onclick = () => {
        state.reportFilters = { student_id: b.dataset.reportStudent };
        setPage("reports");
      }),
  );
  document.querySelectorAll("[data-edit-level]").forEach(
    (b) =>
      (b.onclick = () => {
        const l = state.teacher.levels.find(
          (l) => l.id === Number(b.dataset.editLevel),
        );
        levelModal(l, !l.owner_id);
      }),
  );
  document.querySelectorAll("[data-delete-level]").forEach(
    (b) =>
      (b.onclick = async () => {
        if (!confirm(t("deleteConfirm"))) return;
        try {
          await api("/api/delete-level", { id: Number(b.dataset.deleteLevel) });
          await refresh();
          toast(t("saved"));
        } catch (e) {
          errorMessage(e);
        }
      }),
  );
  document.querySelectorAll("[data-clone-level]").forEach(
    (b) =>
      (b.onclick = () =>
        levelModal(
          state.teacher.levels.find(
            (l) => l.id === Number(b.dataset.cloneLevel),
          ),
          true,
        )),
  );
  const filter = $("[name=filter-language]");
  if (filter)
    filter.onchange = () =>
      document
        .querySelectorAll("[data-level-lang]")
        .forEach(
          (row) =>
            (row.hidden =
              !!filter.value && filter.value !== row.dataset.levelLang),
        );
  if ($("#report-filters"))
    $("#report-filters").onsubmit = (event) => {
      event.preventDefault();
      state.reportFilters = Object.fromEntries(new FormData(event.target));
      loadReports();
    };
  if ($("#export-csv"))
    $("#export-csv").onclick = () => {
      const link = document.createElement("a");
      link.href = "/api/export?" + new URLSearchParams(state.reportFilters);
      link.download = "atigra-results.csv";
      link.click();
    };
  if ($("#teacher-ranking"))
    $("#teacher-ranking").onsubmit = async (event) => {
      event.preventDefault();
      try {
        const result = await api(
          "/api/ranking?" + new URLSearchParams(new FormData(event.target)),
        );
        $("#teacher-ranking-body").innerHTML = result.results.length
          ? rankingRows(result.results)
          : `<div class="empty-state">${t("noRanking")}</div>`;
      } catch (e) {
        errorMessage(e);
      }
    };
}
function classModal(cls) {
  const rules = cls?.rules || {
    accuracy_weight: 0.75,
    thresholds: [50, 65, 80, 95],
    cap2_accuracy: 80,
    cap3_accuracy: 90,
    five_accuracy: 97,
  };
  modal(
    t(cls ? "edit" : "createClass"),
    formShell(
      `${field("className", input("name", cls?.name || "", "text", 'required maxlength="100"'), true)}<div class="full">${check("leaderboard", cls ? cls.leaderboard : true, "leaderboardEnabled")}</div><h3 class="full">${t("scoreRules")}</h3>${field("weight", input("accuracy_weight", rules.accuracy_weight, "number", 'min="0" max="1" step="0.01" required'))}${field("thresholds", input("thresholds", rules.thresholds.join(", "), "text", "required"))}${field("cap2", input("cap2_accuracy", rules.cap2_accuracy, "number", 'min="0" max="100" required'))}${field("cap3", input("cap3_accuracy", rules.cap3_accuracy, "number", 'min="0" max="100" required'))}${field("five", input("five_accuracy", rules.five_accuracy, "number", 'min="0" max="100" required'))}<p class="notice full">${t("rulesHint")}</p>`,
    ),
    async (form, close) => {
      const f = Object.fromEntries(new FormData(form));
      await api("/api/class", {
        id: cls?.id,
        name: f.name,
        archived: cls?.archived || false,
        leaderboard: form.elements.leaderboard.checked,
        rules: {
          accuracy_weight: Number(f.accuracy_weight),
          thresholds: f.thresholds.split(",").map(Number),
          cap2_accuracy: Number(f.cap2_accuracy),
          cap3_accuracy: Number(f.cap3_accuracy),
          five_accuracy: Number(f.five_accuracy),
        },
      });
      close();
      await refresh();
      toast(t("saved"));
    },
  );
}
function studentModal(cid) {
  modal(
    t("newStudent"),
    formShell(
      `${field("alias", input("alias", "", "text", 'required maxlength="60"'))}${field("accountName", input("username", "", "text", 'required minlength="3" maxlength="60" autocomplete="off"'))}${field("email", input("email", "", "email", 'autocomplete="off"'))}${field("password", input("password", "", "password", 'required minlength="8" maxlength="200" autocomplete="new-password"'))}${field("class", select("class_id", [["", t("noClass")], ...state.teacher.classes.filter((c) => !c.archived).map((c) => [c.id, c.name])], cid), true)}<p class="notice full">${t("usernameHelp")}</p>`,
    ),
    async (form, close) => {
      const data = Object.fromEntries(new FormData(form));
      data.class_id = data.class_id ? Number(data.class_id) : null;
      await api("/api/student-account", data);
      close();
      await refresh();
      toast(t("saved"));
    },
  );
}
function passwordModal(sid) {
  const student = state.teacher.students.find((s) => s.id === sid);
  modal(
    t("resetPassword") + " · " + student.alias,
    formShell(
      field(
        "newPassword",
        input(
          "password",
          "",
          "password",
          'required minlength="8" maxlength="200" autocomplete="new-password"',
        ),
        true,
      ),
    ),
    async (form, close) => {
      await api("/api/password", {
        student_id: sid,
        password: form.elements.password.value,
      });
      close();
      toast(t("saved"));
    },
  );
}
function moveModal(sid) {
  const s = state.teacher.students.find((s) => s.id === sid);
  modal(
    t("move") + " · " + s.alias,
    formShell(
      field(
        "class",
        select(
          "class_id",
          [
            ["", t("noClass")],
            ...state.teacher.classes
              .filter((c) => !c.archived)
              .map((c) => [c.id, c.name]),
          ],
          s.class_id,
        ),
        true,
      ),
    ),
    async (form, close) => {
      await api("/api/enrollment", {
        student_id: sid,
        class_id: Number(form.elements.class_id.value) || null,
      });
      close();
      await refresh();
      toast(t("saved"));
    },
  );
}
function levelModal(level, clone = false) {
  modal(
    t(level && !clone ? "edit" : "newLevel"),
    formShell(
      `${field("name", input("name", level?.name || "", "text", 'required maxlength="100"'))}${field(
        "planet",
        select(
          "planet_id",
          state.planets.map((p) => [p.id, p["name_" + state.language]]),
          level?.planet_id || 1,
        ),
      )}${field(
        "mode",
        select(
          "mode",
          ["castle", "race", "bridge", "dragon", "explore", "portal"].map(
            (m) => [m, t(m)],
          ),
          level?.mode || "castle",
        ),
      )}${field(
        "contentLanguage",
        select(
          "language",
          [
            ["es", "Español"],
            ["en", "English"],
          ],
          level?.language || "es",
        ),
      )}${field("text", `<textarea name="text" required maxlength="2000">${esc(level?.text || "")}</textarea>`, true)}${field("targetWpm", input("target_wpm", level?.target_wpm || 15, "number", 'required min="1" max="150" step="0.1"'))}${field("unlock", input("unlock_accuracy", level?.unlock_accuracy ?? 90, "number", 'required min="0" max="100" step="0.1"'))}${field("reorder", input("position", level?.position ?? 0, "number", "required"))}<div>${check("published", level ? level.published : true, "publish")}</div><p class="notice full">${t("assignmentLanguage")}</p>`,
    ),
    async (form, close) => {
      const d = Object.fromEntries(new FormData(form));
      d.published = form.elements.published.checked;
      if (level && !clone) d.id = level.id;
      await api("/api/level", d);
      close();
      await refresh();
      toast(t("saved"));
    },
  );
}
function sequenceModal(target, id) {
  const individual = target === "student_id",
    entity = individual
      ? state.teacher.students.find((s) => s.id === id)
      : state.teacher.classes.find((c) => c.id === id);
  const assignments = (
    individual
      ? state.teacher.individual.filter((a) => a.student_id === id)
      : entity.assignments
  ).filter((a) => a.active);
  const m = modal(
    t("sequence") + " · " + (entity.name || entity.alias),
    `<p class="notice">${t("assignmentNote")}</p><p class="small muted">${t("orderHelp")}</p><div class="table-wrap"><table><thead><tr>${["level", "reorder", "unlock", "weekly", "edit"].map((k) => `<th>${t(k)}</th>`).join("")}</tr></thead><tbody>${assignments.map((a) => `<tr><td>${esc(a.name)} · ${a.language.toUpperCase()}</td><td>${a.position}</td><td>${a.unlock_accuracy}%</td><td>${a.weekly ? "✓" : "—"}</td><td><button class="secondary" data-config-assignment="${a.level_id}">${t("edit")}</button><button class="secondary danger" data-remove-assignment="${a.level_id}">${t("remove")}</button></td></tr>`).join("")}</tbody></table></div><button class="primary form-actions" id="assignment-add">＋ ${t("addLevel")}</button>`,
  );
  m.element.querySelector("#assignment-add").onclick = () => {
    m.close();
    assignmentModal(target, id);
  };
  m.element.querySelectorAll("[data-config-assignment]").forEach(
    (b) =>
      (b.onclick = () => {
        const a = assignments.find(
          (a) => a.level_id === Number(b.dataset.configAssignment),
        );
        m.close();
        assignmentModal(target, id, a);
      }),
  );
  m.element.querySelectorAll("[data-remove-assignment]").forEach(
    (b) =>
      (b.onclick = async () => {
        try {
          const a = assignments.find(
            (a) => a.level_id === Number(b.dataset.removeAssignment),
          );
          await api("/api/assignment", {
            ...a,
            [target]: id,
            class_id: individual ? null : id,
            student_id: individual ? id : null,
            active: false,
          });
          m.close();
          await refresh();
          sequenceModal(target, id);
          toast(t("assignmentSaved"));
        } catch (e) {
          errorMessage(e);
        }
      }),
  );
}
function assignmentModal(target, id, a) {
  const levels = state.teacher.levels.filter((l) => l.published),
    options = levels.map((l) => [
      l.id,
      l.name + " · " + l.language.toUpperCase(),
    ]);
  const m = modal(
    t(a ? "edit" : "addLevel"),
    formShell(
      `${field("level", select("level_id", options, a?.level_id || levels[0]?.id), true)}${field("reorder", input("position", a?.position ?? 0, "number", "required"))}${field("unlock", input("unlock_accuracy", a?.unlock_accuracy ?? 90, "number", 'min="0" max="100" step="0.1" required'))}${field("prerequisite", select("prerequisite_id", [["", t("automatic")], ...options], a?.prerequisite_id), true)}<div class="full">${check("weekly", a ? a.weekly : true, "weeklyChallenge")}</div><p class="notice full">${t("assignmentNote")}</p>`,
    ),
    async (form, close) => {
      const d = Object.fromEntries(new FormData(form));
      d[target] = id;
      d.level_id = Number(d.level_id);
      d.position = Number(d.position);
      d.unlock_accuracy = Number(d.unlock_accuracy);
      d.prerequisite_id = Number(d.prerequisite_id) || null;
      d.weekly = form.elements.weekly.checked;
      d.active = true;
      await api("/api/assignment", d);
      close();
      await refresh();
      sequenceModal(target, id);
      toast(t("assignmentSaved"));
    },
  );
  if (a) m.element.querySelector("[name=level_id]").disabled = true;
  const form = m.element.querySelector("form");
  if (a) {
    const hidden = document.createElement("input");
    hidden.type = "hidden";
    hidden.name = "level_id";
    hidden.value = a.level_id;
    form.append(hidden);
  } else
    m.element.querySelector("[name=level_id]").onchange = (event) => {
      const level = levels.find((l) => l.id === Number(event.target.value));
      form.elements.position.value = level.position;
      form.elements.unlock_accuracy.value = level.unlock_accuracy;
    };
}
(async () => {
  try {
    state.demo = (await api("/api/config")).demo;
    const me = await api("/api/me");
    state.user = me.user;
    state.csrf = me.csrf;
    state.page = state.user.role === "teacher" ? "classes" : "map";
    state.planets = await api("/api/planets");
    await refresh();
  } catch (error) {
    if (error.code !== "unauthenticated") errorMessage(error);
    renderLogin();
  }
})();
