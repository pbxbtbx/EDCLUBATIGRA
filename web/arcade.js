/* Free-practice catalog. Assessed assignments and their history remain on the server. */
window.AtigraArcade = (() => {
  const modes = ["castle", "race", "bridge", "dragon", "explore", "portal"];
  const lessons = {
    castle: [
      [
        "Escudo de aprendiz",
        "Apprentice shield",
        "faja sala alas. ¡Hola, ATIBOT!",
        "fall salad lad. Hello, ATIBOT!",
      ],
      [
        "Torres de energía",
        "Energy towers",
        "Activa el escudo. Protege las torres y recupera la energía.",
        "Activate the shield. Protect the towers and recover the energy.",
      ],
      [
        "La fortaleza estelar",
        "The star fortress",
        "¡Alerta, caballeros! Tres meteoritos se acercan al castillo. ATIBOT carga los escudos: ¡misión cumplida!",
        "Alert, knights! Three meteors approach the castle. ATIBOT charges the shields: mission complete!",
      ],
    ],
    race: [
      [
        "Primer despegue",
        "First launch",
        "nave luna ruta luz",
        "ship moon road star",
      ],
      [
        "Circuito de cometas",
        "Comet circuit",
        "La nave cruza los anillos y sigue la ruta de los cometas.",
        "The ship crosses the rings and follows the comet trail.",
      ],
      [
        "Gran premio galáctico",
        "Galactic grand prix",
        "Piloto, prepara el motor 7. Cruza Orión, gira hacia Júpiter y saluda: ¡qué gran viaje!",
        "Pilot, prepare engine 7. Cross Orion, turn toward Jupiter and say: what a great journey!",
      ],
    ],
    bridge: [
      [
        "Las primeras runas",
        "The first runes",
        "as sa da fa ja la",
        "as sa da fa ja la",
      ],
      [
        "El puente de cristal",
        "The crystal bridge",
        "Une cada runa con cuidado. El puente conecta dos islas de cristal.",
        "Join each rune carefully. The bridge connects two crystal islands.",
      ],
      [
        "Camino entre dimensiones",
        "A path between dimensions",
        "ATIBOT descifra: águila, brújula, código. Cada símbolo abre un camino. ¿Podrás llegar al otro lado?",
        "ATIBOT deciphers: eagle, compass, code. Each symbol opens a path. Can you reach the other side?",
      ],
    ],
    dragon: [
      [
        "Taller de engranajes",
        "Gear workshop",
        "pieza rueda ala cola",
        "part wheel wing tail",
      ],
      [
        "Alas de cobre",
        "Copper wings",
        "Repara las alas del dragón. Conecta los cables y ajusta su motor.",
        "Repair the dragon wings. Connect the wires and tune its engine.",
      ],
      [
        "El despertar del dragón",
        "The dragon awakens",
        'El dragón mecánico despertó a las 8:30. "¡Gracias, ATIBOT!", rugió. Sus alas brillan con energía verde.',
        'The mechanical dragon woke at 8:30. "Thank you, ATIBOT!" it roared. Its wings shine with green energy.',
      ],
    ],
    explore: [
      [
        "Paseo por el planeta",
        "Planet walk",
        "roca gema nave base",
        "rock gem ship base",
      ],
      [
        "El bosque de circuitos",
        "The circuit forest",
        "Avanza hasta el bosque. Recoge cinco gemas y vuelve a la base.",
        "Walk to the forest. Collect five gems and return to the base.",
      ],
      [
        "Bitácora de expedición",
        "Expedition log",
        'Día 12: descubrimos un cañón azul. Allí, un pequeño robot señaló una señal: "Explora, imagina y crea".',
        'Day 12: we discovered a blue canyon. A little robot pointed to a sign: "Explore, imagine and create."',
      ],
    ],
    portal: [
      [
        "La primera chispa",
        "The first spark",
        "luz azul abre portal",
        "blue light open portal",
      ],
      [
        "Coordenadas secretas",
        "Secret coordinates",
        "Escribe el código secreto. El portal se ilumina y abre una nueva ruta.",
        "Type the secret code. The portal lights up and opens a new route.",
      ],
      [
        "Destino: imaginación",
        "Destination: imagination",
        "Coordenadas: 42, 17, 9. ¿Destino? ¡La imaginación! Si puedes soñarlo, puedes crearlo y programarlo.",
        "Coordinates: 42, 17, 9. Destination? Imagination! If you can dream it, you can create it and program it.",
      ],
    ],
  };
  const levels = modes.flatMap((mode, index) =>
    lessons[mode].map(([es, en, textES, textEN], i) => ({
      id: `${mode}-${i + 1}`,
      mode,
      tier: i + 1,
      planet_id: index + 1,
      name: { es, en },
      text: { es: textES, en: textEN },
      target_wpm: [10, 18, 28][i],
    })),
  );
  return Object.freeze({ modes, levels });
})();
