// Kleine Interaktionen im Browser. Die eigentliche Empfehlung läuft in Python.
document.addEventListener('DOMContentLoaded', () => {
  const interestInputs = [...document.querySelectorAll('input[name="interests"]')];
  const counter = document.getElementById('interest-counter');
  function updateCounter() {
    if (!counter) return;
    const checked = interestInputs.filter(input => input.checked).length;
    counter.textContent = `${checked} ausgewählt`;
  }
  interestInputs.forEach(input => input.addEventListener('change', updateCounter));
  updateCounter();

  const budget = document.getElementById('budget');
  document.querySelectorAll('[data-budget]').forEach(button => {
    button.addEventListener('click', () => {
      if (budget) budget.value = button.dataset.budget;
      budget?.focus();
    });
  });

  document.querySelectorAll('[data-copy]').forEach(button => {
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(button.dataset.copy);
        const original = button.innerHTML;
        button.textContent = 'Kopiert ✓';
        setTimeout(() => { button.innerHTML = original; }, 1500);
      } catch (_) {
        button.textContent = 'Kopieren nicht möglich';
      }
    });
  });
});
