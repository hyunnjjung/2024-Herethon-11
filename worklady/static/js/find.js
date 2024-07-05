document.addEventListener("DOMContentLoaded", () => {
  const popup = document.getElementById("popup");

  // Show the popup
  popup.classList.add("show");

  // Hide the popup after 3 seconds
  setTimeout(() => {
    popup.classList.add("hide");

    // Optionally, remove the popup from the DOM after the fade-out transition
    setTimeout(() => {
      popup.style.display = "none";
    }, 1000); // Match the duration of the CSS transition
  }, 2000);
});
