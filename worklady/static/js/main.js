document.addEventListener("DOMContentLoaded", function () {
  var menuTrigger = document.getElementById("menu-trigger");
  var sidebar = document.getElementById("sidebar");
  var overlay = document.getElementById("overlay");
  var hamTopMenuLinks = document.querySelectorAll(".ham-top-menu > li > a");

  menuTrigger.addEventListener("click", function () {
    this.classList.toggle("active-1");
    sidebar.classList.toggle("active");
    overlay.classList.toggle("active");
  });

  overlay.addEventListener("click", function () {
    this.classList.remove("active");
    sidebar.classList.remove("active");
    menuTrigger.classList.remove("active-1");
  });

  hamTopMenuLinks.forEach(function (link) {
    link.addEventListener("click", function () {
      var subMenu = this.nextElementSibling;
      var img = this.querySelector("img");

      if (subMenu && subMenu.classList.contains("ham-sub-menu")) {
        subMenu.classList.toggle("active");
        if (subMenu.classList.contains("active")) {
          subMenu.style.display = "block";
          img.src = "static/img/sidebar_up.png"; // 이미지 변경
        } else {
          subMenu.style.display = "none";
          img.src = "static/img/sidebar_down.png"; // 원래 이미지로 복구
        }
      }
    });
  });
});
