document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".filter button");
  const questions = document.querySelectorAll(".myquestion");

  buttons.forEach((button) => {
    button.addEventListener("click", function () {
      // 모든 버튼에서 active 클래스 제거
      buttons.forEach((btn) => {
        btn.classList.remove("active");
        btn.querySelector("img").src = "../image/Vector.png"; // 기본 이미지 경로
      });

      // 클릭된 버튼에 active 클래스 추가
      this.classList.add("active");
      this.querySelector("img").src = "../image/Vector_selected.png"; // 활성화된 이미지 경로

      // 클릭된 버튼의 data-filter 값 가져오기
      const filterValue = this.getAttribute("data-filter");

      // 질문 목록 필터링
      questions.forEach((question) => {
        const typeValue = question
          .querySelector("h3")
          .getAttribute("data-type");

        if (filterValue === "*" || filterValue === typeValue) {
          question.style.display = "block"; // 일치하는 질문 보이기
        } else {
          question.style.display = "none"; // 일치하지 않는 질문 숨기기
        }
      });
    });
  });
});
