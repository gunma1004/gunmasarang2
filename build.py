import os

BASE_URL = "https://gunmasarang2.netlify.app"
BRAND_NAME = "건마사랑"
REP_PHONE = "0507-1280-3344"

# 4대 제휴 업체 정보
SHOPS = [
    {"name": "퀸즈홈테라피", "phone": "0507-1280-3296", "score": "4.9", "tags": "타이전문 · 아로마 · 예약금없음"},
    {"name": "오늘밤테라피", "phone": "0507-1280-3199", "score": "4.8", "tags": "스웨디시 · 아로마 · 후불제"},
    {"name": "주주테라피",   "phone": "0507-1280-3197", "score": "4.8", "tags": "감성힐링 · 여성전용 · 카드가능"},
    {"name": "한국골든테라피", "phone": "0507-1280-3360", "score": "4.7", "tags": "프리미엄 · 집중케어 · 24시운영"}
]

# 전체 세부 지역 데이터
REGIONS = {
    "seoul": [
        ("gangnam-gu", "강남"), ("gangdong-gu", "강동"), ("gangbuk-gu", "강북"), ("gangseo-gu", "강서"),
        ("gwanak-gu", "관악"), ("gwangjin-gu", "광진"), ("guro-gu", "구로"), ("geumcheon-gu", "금천"),
        ("nowon-gu", "노원"), ("dobong-gu", "도봉"), ("dongdaemun-gu", "동대문"), ("dongjak-gu", "동작"),
        ("mapo-gu", "마포"), ("seodaemun-gu", "서대문"), ("seocho-gu", "서초"), ("seongdong-gu", "성동"),
        ("seongbuk-gu", "성북"), ("songpa-gu", "송파"), ("yangcheon-gu", "양천"), ("yeongdeungpo-gu", "영등포"),
        ("yongsan-gu", "용산"), ("eunpyeong-gu", "은평"), ("jongno-gu", "종로"), ("jung-gu", "중구"),
        ("jungnang-gu", "중랑")
    ],
    "gyeonggi": [
        ("gapyeong-gun", "가평"), ("goyang-si", "고양"), ("gwacheon-si", "과천"), ("gwangmyeong-si", "광명"),
        ("gwangju-si", "광주"), ("guri-si", "구리"), ("gunpo-si", "군포"), ("gimpo-si", "김포"),
        ("namyangju-si", "남양주"), ("dongducheon-si", "동두천"), ("bucheon-si", "부천"), ("seongnam-si", "성남"),
        ("suwon-si", "수원"), ("siheung-si", "시흥"), ("ansan-si", "안산"), ("anseong-si", "안성"),
        ("anyang-si", "안양"), ("yangju-si", "양주"), ("yangpyeong-gun", "양평"), ("yeoju-si", "여주"),
        ("yeoncheon-gun", "연천"), ("osan-si", "오산"), ("yongin-si", "용인"), ("uiwang-si", "의왕"),
        ("uijeongbu-si", "의정부"), ("icheon-si", "이천"), ("paju-si", "파주"), ("pyeongtaek-si", "평택"),
        ("pocheon-si", "포천"), ("hanam-si", "하남"), ("hwaseong-si", "화성")
    ],
    "incheon": [
        ("ganghwa-gun", "강화"), ("geomdan-gu", "검단"), ("gyeyang-gu", "계양"), ("namdong-gu", "남동"),
        ("michuhol-gu", "미추홀"), ("bupyeong-gu", "부평"), ("seohae-gu", "서해"), ("yeonsu-gu", "연수"),
        ("yeongjong-gu", "영종"), ("ongjin-gun", "옹진"), ("jemulpo-gu", "제물포")
    ]
}

PROV_INFO = {
    "seoul": ("서울특별시", "서울", "/"),
    "gyeonggi": ("경기도", "경기", "/gyeonggi/"),
    "incheon": ("인천광역시", "인천", "/incheon/")
}

def build_shop_cards(loc_name):
    cards = []
    for idx, shop in enumerate(SHOPS, 1):
        clean_phone = shop["phone"].replace("-", "")
        card = f"""          <article class="provider-card">
            <div class="rank">{idx}<small>위</small></div>
            <div class="provider-main">
              <div class="provider-head">
                <h3>{shop['name']}</h3>
                <span>★ {shop['score']}</span>
              </div>
              <div class="tags">
                <span>{shop['tags']}</span>
              </div>
              <p>{loc_name} 인근 신속 이동 동선 확인 후 방문 관리합니다. 선입금 없는 정직한 안내입니다.</p>
              <div class="provider-prices"><span>건식 60분 · 8만</span> / <span>오일 90분 · 11만</span></div>
            </div>
            <a class="provider-phone-btn" href="tel:{clean_phone}">
              <b>전화 상담</b>
              <small>{shop['phone']}</small>
            </a>
          </article>"""
        cards.append(card)
    return "\n".join(cards)

def run():
    total_count = 0
    for prov_key, districts in REGIONS.items():
        prov_full, prov_short, prov_hub_url = PROV_INFO[prov_key]
        
        # 인근 세부 지역 링크 목록
        links = []
        for slug, name in districts:
            label = f"{prov_short} {name}" if prov_key == "seoul" else name
            links.append(f'          <a class="region-link" href="/areas/{prov_key}/{slug}/"><b>{label}</b><span>출장 케어 안내</span></a>')
        nearby_html = "\n".join(links)

        for slug, name in districts:
            district_title = f"{prov_short} {name}" if prov_key == "seoul" else name
            dir_path = os.path.join("areas", prov_key, slug)
            os.makedirs(dir_path, exist_ok=True)
            
            canonical_url = f"{BASE_URL}/areas/{prov_key}/{slug}/"
            
            html = f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
  <meta name="description" content="{BRAND_NAME} {prov_full} {district_title} 안내. 선입금 없이 현장에서 확인하는 출장마사지·홈타이 코스와 직통 제휴 매장 리스트입니다.">
  <meta name="keywords" content="{district_title}출장마사지, {district_title}홈타이, {district_title}출장타이, {district_title}스웨디시">
  <link rel="canonical" href="{canonical_url}">
  <title>{prov_full} {district_title} 출장 케어 마사지 | 추천 업체 비교 - {BRAND_NAME}</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body data-page-type="target-district-hub">
  <a class="skip-link" href="#content">본문으로 이동</a>
  
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-text-logo" aria-label="{BRAND_NAME} 홈">
        <span class="brand-badge">건</span>
        <span class="brand-name">{BRAND_NAME}</span>
      </a>
      <a class="header-consult" href="#consult">상담 안내</a>
    </div>
  </header>

  <nav class="breadcrumb" aria-label="현재 위치">
    <div class="container">
      <a href="/">홈</a><i>›</i><a href="{prov_hub_url}">{prov_short}</a><i>›</i><a href="{canonical_url}">{district_title}</a>
    </div>
  </nav>

  <main id="content">
    <section class="directory-head">
      <div class="container">
        <p class="intro-line">이동 시간을 줄이고 충분히 쉴 수 있도록 희망 시간대와 이용 목적을 간단히 정리해 주세요.</p>
        <h1>{prov_full} {district_title} 출장 케어 한눈에</h1>
        <p>{district_title} 생활권에서 즉시 배정 가능한 4대 전문 업체를 안내해 드립니다.</p>
        <div class="filter-pills">
          <span>스웨디시</span><span>아로마</span><span>타이</span><span>여성전용</span>
        </div>
        <div class="feature-panels">
          <article><b>🏨 호텔·숙소</b><p>출입 방법과 객실 정보를 미리 확인합니다.</p></article>
          <article><b>🏠 주거 공간</b><p>주차와 공동현관 안내를 함께 전달합니다.</p></article>
          <article><b>📍 생활권 안내</b><p>인접 지역 이동 시간까지 고려합니다.</p></article>
          <article><b>🗓 일정 배정</b><p>희망 시각과 코스를 차례대로 확인합니다.</p></article>
        </div>
      </div>
    </section>

    <!-- 4대 제휴 업체 리스트 -->
    <section class="section providers">
      <div class="container">
        <div class="section-row">
          <h2 class="section-title">{district_title} 추천 제휴 매장</h2>
          <span>희망 매장 직통 번호로 빠른 배정</span>
        </div>
        <div class="provider-list">
{build_shop_cards(district_title)}
        </div>
      </div>
    </section>

    <!-- 코스 안내 -->
    <section class="section course-section" id="courses">
      <div class="container">
        <h2 class="section-title">{district_title} 코스 &amp; 요금 안내</h2>
        <p class="section-note">상담과 현장에서 시간·범위·비용을 다시 확인하고 선입금 없이 진행합니다.</p>
        <div class="course-grid">
          <article class="course-card">
            <span class="course-icon">🧘</span>
            <h3>건식 밸런스</h3>
            <p>오일 없이 전신의 긴장과 스트레칭 범위를 차분히 조율합니다.</p>
            <div class="price-list">
              <div class="price-row"><span>60분</span><b>80,000원</b></div>
              <div class="price-row"><span>90분</span><b>100,000원</b></div>
              <div class="price-row"><span>120분</span><b>120,000원</b></div>
            </div>
          </article>
          <article class="course-card">
            <span class="course-icon">🌿</span>
            <h3>아로마 릴렉스</h3>
            <p>오일 선호와 집중 부위를 먼저 확인하는 부드러운 관리입니다.</p>
            <div class="price-list">
              <div class="price-row"><span>60분</span><b>90,000원</b></div>
              <div class="price-row"><span>90분</span><b>110,000원</b></div>
              <div class="price-row"><span>120분</span><b>130,000원</b></div>
            </div>
          </article>
          <article class="course-card">
            <span class="course-icon">💧</span>
            <h3>스웨디시 오일</h3>
            <p>일정한 리듬과 편안한 압으로 전신 흐름을 맞춥니다.</p>
            <div class="price-list">
              <div class="price-row"><span>60분</span><b>100,000원</b></div>
              <div class="price-row"><span>90분</span><b>120,000원</b></div>
              <div class="price-row"><span>120분</span><b>140,000원</b></div>
            </div>
          </article>
          <article class="course-card">
            <span class="course-icon">👑</span>
            <h3>프리미엄 케어</h3>
            <p>전신 관리와 요청 부위의 비중을 세밀하게 구성합니다.</p>
            <div class="price-list">
              <div class="price-row"><span>90분</span><b>130,000원</b></div>
              <div class="price-row"><span>120분</span><b>150,000원</b></div>
            </div>
          </article>
          <article class="course-card">
            <span class="course-icon">✨</span>
            <h3>여성전용 방문 케어</h3>
            <p>개인 경계와 관리 범위, 제외 부위를 방문 전에 분명히 확인합니다.</p>
            <div class="price-list">
              <div class="price-row"><span>90분</span><b>120,000원</b></div>
              <div class="price-row"><span>120분</span><b>150,000원</b></div>
              <div class="price-row"><span>150분</span><b>180,000원</b></div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- 인근 세부 지역 링크 -->
    <section class="section region-section" id="regions">
      <div class="container">
        <h2 class="section-title">{prov_short} 세부 지역 둘러보기</h2>
        <div class="region-grid">
{nearby_html}
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section soft">
      <div class="container">
        <h2 class="section-title">자주 묻는 질문</h2>
        <div class="faq-list">
          <details open>
            <summary>{district_title} 방문 가능 시간은 어떻게 확인하나요?</summary>
            <p>희망 시간과 주소를 알려주면 이동 동선과 당일 배정 상황을 확인해 안내합니다.</p>
          </details>
          <details>
            <summary>선입금이 필요한가요?</summary>
            <p>선입금을 요구하지 않으며 관리 범위와 최종 비용을 현장에서 다시 확인합니다.</p>
          </details>
        </div>
      </div>
    </section>

    <!-- 상담 안내 -->
    <section class="section consult" id="consult">
      <div class="container">
        <div class="consult-card">
          <div>
            <b>운영 안내</b>
            <p>희망 시간과 코스를 상단 제휴 매장 직통 번호로 알려주세요.</p>
          </div>
          <div>
            <b>결제 안내</b>
            <p>선입금 없이 관리 범위와 비용을 현장에서 다시 확인합니다.</p>
          </div>
          <a href="#courses">코스 다시 보기</a>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-logo-text">{BRAND_NAME}</div>
      <p>{district_title} 출장 케어 마사지 제휴 안내 플랫폼</p>
      <nav>
        <a href="/">서울</a>
        <a href="/gyeonggi/">경기</a>
        <a href="/incheon/">인천</a>
      </nav>
      <small>© 2026 {BRAND_NAME}. All rights reserved.</small>
    </div>
  </footer>

  <a class="fixed-phone-cta" href="tel:{REP_PHONE.replace('-', '')}" aria-label="대표 전화 상담">대표 {REP_PHONE}</a>
</body>
</html>"""
            
            with open(os.path.join(dir_path, "index.html"), "w", encoding="utf-8") as f:
                f.write(html)
            total_count += 1
            
    print(f"생성 완료! 총 {total_count}개의 세부 지역 페이지가 생성되었습니다.")

if __name__ == "__main__":
    run()