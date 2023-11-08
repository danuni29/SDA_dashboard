var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    // mySlides 클래스를 가진 모든 슬라이드 요소 가져오기
    var slides = document.getElementsByClassName("mySlides");

    // 모든 슬라이드 숨기기
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    // 슬라이드 인데스 숫자 증가시키기
    slideIndex++;
    // 현재 슬라이드 인덱스가 슬라이드 요소의 수를 초과하면, 다시 처음으로 돌아가기 위해 slideindex = 1로 설정
    if (slideIndex > slides.length) {
        slideIndex = 0;
    }
    // 슬라이드인덱스에 해당하는 슬라이드 화면에 표시
    slides[slideIndex - 1].style.display = "block";
    // 슬라이드 인덱스 출력
    alert("현재 슬라이드 인덱스: " + slideIndex);

    setTimeout(showSlides, 2000); // 2초마다 이미지가 체인지됩니다
}
