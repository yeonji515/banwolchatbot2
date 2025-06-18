import streamlit as st

# 선생님 데이터 (이름, 과목, 부서, 담임학급)
teachers = {
    "김대호": {"subject": "역사", "department": "교무기획부", "class": None},
    "서은진": {"subject": "국어", "department": "미래연구부", "class": None},
    "황하늬": {"subject": "음악", "department": "학생안전부", "class": None},
    "정호윤": {"subject": "영어", "department": "교육과정부", "class": None},
    "엄기영": {"subject": "영어", "department": "인문사회부", "class": None},
    "박미정": {"subject": "통과", "department": "자연과학부", "class": None},
    "오정아": {"subject": "체육", "department": "예술체육부", "class": None},
    "배경미": {"subject": "정보", "department": "교육정보부", "class": None},
    "김지현": {"subject": "진로", "department": "진로진학부", "class": None},
    "김혜선": {"subject": "수학", "department": "1학년부", "class": None},
    "송인필": {"subject": "물리", "department": "2학년부", "class": None},
    "유형우": {"subject": "수학", "department": "3학년부", "class": None},
    "편경림": {"subject": "영어", "department": "교무기획부", "class": None},
    "김경희": {"subject": "영어", "department": "미래연구부", "class": None},
    "윤효근": {"subject": "통사", "department": "학생안전부", "class": None},
    "한숙희": {"subject": "지리", "department": "교육과정부", "class": None},
    "박병찬": {"subject": "지리", "department": "인문사회부", "class": None},
    "이지선": {"subject": "생과", "department": "자연과학부", "class": None},
    "임종수": {"subject": "체육", "department": "예술체육부", "class": None},
    "김진옥": {"subject": "화학", "department": "교육정보부", "class": None},
    "어경선": {"subject": "수학", "department": "진로진학부", "class": None},
    "이지수": {"subject": "통사", "department": "1학년부", "class": "1학년 1반"},
    "유의영": {"subject": "수학", "department": "2학년부", "class": "2학년 1반"},
    "최영주": {"subject": "일사", "department": "3학년부", "class": "3학년 1반" },
    "김현미": {"subject": "일사", "department": "교무기획부", "class": None},
    "김지선": {"subject": "수학", "department": "미래연구부", "class": None},
    "김종규": {"subject": "윤리", "department": "학생안전부", "class": None},
    "서은영": {"subject": "일본어", "department": "교육과정부", "class": None},
    "정고은": {"subject": "보건", "department": "예술체육부", "class": None},
    "강자은": {"subject": "음악", "department": "1학년부", "class": "1학년 2반"},
    "김상길": {"subject": "지학", "department": "2학년부", "class": "2학년 2반"},
    "이지우": {"subject": "영어", "department": "3학년부", "class": "3학년 2반"},
    "이수정": {"subject": "영양", "department": "예술체육부", "class": None},
    "안진희": {"subject": "수학", "department": "1학년부", "class": "1학년 3반"},
    "김성혜": {"subject": "생과", "department": "2학년부", "class": "2학년 3반"},
    "신선임": {"subject": "국어", "department": "3학년부", "class": "3학년 3반"},
    "이유진": {"subject": "영어", "department": "교무기획부", "class": None},
    "이보향": {"subject": "영어", "department": "미래연구부", "class": None},
    "유호진": {"subject": "체육", "department": "학생안전부", "class": None},
    "조영은": {"subject": "수학", "department": "교무기획부", "class": None},
    "김아름": {"subject": "상담", "department": "학생안전부", "class": None},
    "송유빈": {"subject": "국어", "department": "1학년부", "class": "1학년 4반"},
    "성지은": {"subject": "영어", "department": "2학년부", "class": "2학년 4반"},
    "장윤경": {"subject": "국어", "department": "3학년부", "class": "3학년 4반"},
    "서산나": {"subject": "특수", "department": "교무기획부", "class": None},
    "조성분": {"subject": "통과", "department": "1학년부", "class": "1학년 5반"},
    "김가희A": {"subject": "국어", "department": "2학년부", "class": "2학년 5반"},
    "남유정": {"subject": "화학", "department": "3학년부", "class": "3학년 5반"},
    "김동건": {"subject": "특수", "department": "교무기획부", "class": None},
    "남현지": {"subject": "미술", "department": "1학년부", "class": "1학년 6반"},
    "성지영": {"subject": "체육", "department": "2학년부", "class": "2학년 6반"},
    "도만구": {"subject": "물리", "department": "3학년부", "class": "3학년 6반"},
    "김나연": {"subject": "국어", "department": "1학년부", "class": "1학년 7반"},
    "강영미": {"subject": "국어", "department": "2학년부", "class": "2학년 7반"},
    "이동현": {"subject": "지학", "department": "3학년부", "class": "3학년 7반"},
    "김지연": {"subject": "역사", "department": "1학년부", "class": "1학년 8반"},
    "조준": {"subject": "중국어", "department": "2학년부", "class": "2학년 8반"},
    "강미현": {"subject": "윤리", "department": "3학년부", "class": "3학년 8반"},
    "김가희B": {"subject": "국어", "department": "1학년부", "class": "1학년 9반"},
    "주효진": {"subject": "일사", "department": "2학년부", "class": "2학년 9반"},
    "문숙희": {"subject": "국어", "department": "3학년부", "class": "3학년 9반"},
    "고태열": {"subject": "기술", "department": "1학년부", "class": "1학년 10반"},
    "문주희": {"subject": "윤리", "department": "2학년부", "class": "2학년 10반"},
    "호가영": {"subject": "수학", "department": "3학년부", "class": "3학년 10반"}
}
import streamlit as st

# 🎉 행사 일정 데이터
events = {
    "2차 지필평가": "6월 26일 ~ 7월 1일",
    "SW·AI 캠프": "7월 2일 ~ 7월 3일",
    "직업탐색 프로그램": "7월 8일",
    "3학년 전국연합학력평가": "7월 10일",
    "학교자율교육과정": "7월 8일 ~ 7월 11일",
    "방학식": "7월 18일"
}

# 📘 담임 검색 함수
def search_by_class(user_input):
    for name, info in teachers.items():
        if info["class"] and info["class"] in user_input:
            return f"{info['class']} 담임선생님은 {name} 선생님입니다. (과목: {info['subject']}, 부서: {info['department']})"
    return None

# 🎯 행사 검색 함수
def search_events(user_input):
    for event_name, event_date in events.items():
        if event_name in user_input:
            return f"🎉 {event_name}: {event_date}"
    return None

# 🖥️ Streamlit UI
st.title("🏫 화성반월고 챗봇")
user_input = st.text_input("무엇이 궁금한가요? (예: 선생님 이름, 과목, 부서, 학급, 행사명)")

if user_input:
    result = None

    # 1. 학급(담임) 검색
    result = search_by_class(user_input)

    # 2. 행사 검색
    if not result:
        result = search_events(user_input)

    # 3. 선생님 이름 검색
    if not result:
        for name, info in teachers.items():
            if name in user_input:
                result = f"{name} 선생님 - 과목: {info['subject']}, 부서: {info['department']}"
                if info["class"]:
                    result += f", 담임학급: {info['class']}"
                break

    # 4. 과목 검색
    if not result:
        subject_matches = []
        for name, info in teachers.items():
            if info["subject"] in user_input:
                line = f"- {name} 선생님 (부서: {info['department']}"
                if info["class"]:
                    line += f", 담임: {info['class']}"
                line += ")"
                subject_matches.append(line)
        if subject_matches:
            result = "📚 해당 과목 담당 선생님:\n" + "\n".join(subject_matches)

    # 출력
    if result:
        st.success(result)
    else:
        st.error("죄송합니다. 해당 정보를 찾을 수 없습니다.")
