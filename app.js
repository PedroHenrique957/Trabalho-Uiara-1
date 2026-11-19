const state = {
  A: { gols: 0, amarelos: 0, vermelhos: 0 },
  B: { gols: 0, amarelos: 0, vermelhos: 0 },
};

const loginScreen = document.querySelector("#login-screen");
const panelScreen = document.querySelector("#panel-screen");
const loginForm = document.querySelector("#login-form");
const loginError = document.querySelector("#login-error");

function atualizarPainel() {
  document.querySelector("#score").textContent =
    `${state.A.gols} x ${state.B.gols}`;
  document.querySelector("#cards-a").textContent =
    `🟨 ${state.A.amarelos}   |   🟥 ${state.A.vermelhos}`;
  document.querySelector("#cards-b").textContent =
    `🟨 ${state.B.amarelos}   |   🟥 ${state.B.vermelhos}`;
}

function entrar() {
  loginScreen.hidden = true;
  panelScreen.hidden = false;
  loginError.textContent = "";
}

loginForm.addEventListener("submit", (event) => {
  event.preventDefault();
  entrar();
});

document.querySelector(".login-button").addEventListener("click", entrar);

document.querySelectorAll(".controls button").forEach((button) => {
  button.addEventListener("click", () => {
    const team = button.dataset.team;
    const action = button.dataset.action;
    let status;

    if (action === "goal") {
      state[team].gols += 1;
      status = `Gol ⚽ registrado para o Time ${team}`;
    } else if (action === "yellow") {
      state[team].amarelos += 1;
      status = `Cartão Amarelo registrado para o Time ${team}`;
    } else {
      state[team].vermelhos += 1;
      status = `Cartão Vermelho registrado para o Time ${team}`;
    }

    atualizarPainel();
    document.querySelector("#status").textContent =
      `Último evento: ${status} (Enviado para a Nuvem ☁️)`;
  });
});

