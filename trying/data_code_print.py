import requests

# 요청을 보낼 URL 설정
url = "https://sobi.chonbuk.ac.kr/menu/week_menu.php"  # 실제 서버 URL로 변경해야 합니다
data = {"code": "your_desired_value"}

# POST 요청 보내기
response = requests.post(url, data=data)

# 응답 확인
if response.status_code == 200:  # HTTP 상태 코드 200은 성공을 나타냅니다
    print("요청 성공")
    print("서버 응답:", response.text)  # 응답 데이터 출력
else:
    print("요청 실패")
    print("HTTP 상태 코드:", response.status_code)

