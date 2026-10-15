/* Catalog supplied by the server from arcade.json; stable ids preserve progress. */
window.AtigraArcade = {
  modes: [],
  levels: [],
  load(catalog) {
    this.modes = catalog.modes;
    this.levels = catalog.levels;
  },
  choices(expected, index, language) {
    const alphabet = Array.from(
      language === "es" ? "asdfjklñáéíóúqwerty" : "asdfjklqwertyuio",
    );
    const choices = [expected];
    for (let i = 0; choices.length < 3; i++) {
      const letter = alphabet[(index * 7 + i * 3) % alphabet.length];
      if (!choices.includes(letter)) choices.push(letter);
    }
    const rotation = (index * 7 + 1) % 3;
    return choices.slice(rotation).concat(choices.slice(0, rotation));
  },
};
