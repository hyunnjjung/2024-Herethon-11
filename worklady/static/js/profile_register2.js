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

  // 추가된 기능 시작
  const profileImageInput = document.getElementById("profile_image");
  const profilePreview = document.getElementById("profile_preview");

  profileImageInput.addEventListener("change", function () {
    const file = profileImageInput.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        profilePreview.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  });

  const profileForm = document.getElementById("profileForm");
  profileForm.addEventListener("submit", function (event) {
    event.preventDefault();
    alert("프로필이 등록되었습니다!");
    // 여기에서 서버로 데이터를 보내는 로직을 추가하세요.
  });
  // 추가된 기능 끝
});
