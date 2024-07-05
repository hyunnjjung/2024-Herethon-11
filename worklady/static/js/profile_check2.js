document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".menu");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      buttons.forEach((btn) => btn.classList.remove("active"));
      button.classList.add("active");
    });
  });

  const addItemButtons = document.querySelectorAll(".add_item_button");

  addItemButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
      const parentFormGroup = event.target.closest(".form_group");
      const newItem = parentFormGroup.cloneNode(true);
      newItem.querySelector("input").value = "";
      newItem.querySelector("select").value = "";
      parentFormGroup.after(newItem);
    });
  });
});
