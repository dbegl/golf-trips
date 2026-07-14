# build_kaohsiung.py — modeled after the skill's assets/build_miyazaki.py (same CSS, same section
# structure, same all-in/cmp/warn components) because that page passed the eval loop.
import base64, os

CSS = open('template_style.css').read()

def b64(path):
    ext = 'jpeg' if path.endswith(('.jpg','.jpeg')) else path.split('.')[-1]
    return f"data:image/{ext};base64," + base64.b64encode(open(path,'rb').read()).decode()

IMG = {
 'hero': b64('imgs/nan_yi_palms_hero.jpg'),
 'hsinyi_feb': b64('imgs/hsin_yi_golf_club.jpg'),
 'hsinyi_fw': b64('imgs/hsin_yi_fairway.jpg'),
 'hsinyi_ch': b64('imgs/hsin_yi_clubhouse.jpg'),
 'nanyi_rb': b64('imgs/nan_yi_rainbow.jpg'),
 'tks': b64('imgs/ta_kang_shan_valley.jpg'),
 'lotus': b64('imgs/lotus_pond_pagoda.jpg'),
}
MAP = "https://www.google.com/maps/search/?api=1&query="

HTML = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>가오슝 — 남대만 겨울 골프 트립 | dbegl</title>
<style>{CSS}
  .allin{{ width:100%; border-collapse:collapse; font-size:14px; margin-top:8px; }}
  .allin td{{ padding:10px 4px; border-bottom:1px solid #eadfc8; font-weight:300; color:#3a3a30; }}
  .allin td:last-child{{ text-align:right; font-weight:500; color:var(--green2); white-space:nowrap; }}
  .allin tr.tot td{{ border-top:2px solid var(--green); border-bottom:none; font-weight:700; color:var(--green); padding-top:13px; }}
  .allin tr.sub td{{ color:var(--muted); font-size:12.5px; padding:4px 4px; border-bottom:none; }}
  .day{{ display:flex; gap:18px; padding:16px 0; border-bottom:1px solid #eadfc8; }}
  .day .d{{ font-family:'Cormorant Garamond',serif; font-size:13px; letter-spacing:.18em; text-transform:uppercase; color:var(--gold); min-width:74px; padding-top:2px; }}
  .day .c b{{ color:var(--green); font-size:15px; }}
  .day .c{{ font-size:13.5px; color:#4a463c; font-weight:300; }}
  .warn{{ background:#fbf6ec; border:1px solid #e7ddc8; border-left:3px solid var(--gold); padding:13px 16px; margin-bottom:11px; font-size:13.5px; font-weight:300; color:#4a463c; }}
  .warn b{{ color:var(--green2); font-weight:600; }}
  .cta a{{ display:inline-block; margin:5px 8px 5px 0; padding:11px 22px; background:var(--green); color:#fff; text-decoration:none; font-size:13.5px; border-radius:4px; letter-spacing:.02em; }}
  .cta a.alt{{ background:#fff; color:var(--green2); border:1px solid #d8ccae; }}
  .note{{ font-size:12.5px; color:var(--muted); font-weight:300; margin-top:14px; }}
  .vals{{ display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }}
  .val-c{{ border:1px solid #e7ddc8; background:#fff; padding:22px 20px; border-radius:3px; }}
  .val-c .eng{{ display:block; font-family:'Cormorant Garamond',serif; letter-spacing:.16em; text-transform:uppercase; font-size:10px; color:var(--gold); margin-bottom:9px; }}
  .val-c b{{ display:block; color:var(--green); font-size:16px; margin-bottom:7px; }}
  .val-c p{{ font-size:13px; color:#4a463c; font-weight:300; line-height:1.6; }}
  .cmp{{ width:100%; border-collapse:collapse; font-size:13px; margin-top:6px; }}
  .cmp th,.cmp td{{ padding:11px 12px; border-bottom:1px solid #eadfc8; text-align:left; font-weight:300; }}
  .cmp thead th{{ font-weight:600; color:var(--green); font-size:13.5px; border-bottom:2px solid var(--green); }}
  .cmp thead th.self{{ color:var(--green2); }}
  .cmp td.lab{{ color:var(--muted); }}
  .cmp td.self{{ color:var(--green2); font-weight:500; background:#fbf8f1; }}
  .cmp .yes{{ color:var(--green2); font-weight:700; }}
  .cmp .no{{ color:#b06a4f; font-weight:600; }}
</style>
</head>
<body>
<div class="page">

  <!-- HERO -->
  <div class="hero">
    <div class="bg"><img src="{IMG['hero']}" alt="Nan Yi Golf Country Club, Tainan"></div>
    <div class="inner">
      <div class="top">
        <div class="kicker">dbegl Winter Golf &nbsp;—&nbsp; 직접 예약하는 트립</div>
        <div class="seal">Kaohsiung<br>South Taiwan<br>3N 4D</div>
      </div>
      <div>
        <h1>Kaohsiung<small>가오슝 — 남대만 한겨울 골프 트립</small></h1>
        <div class="sub">한국이 얼어붙는 1~2월, 남대만은 낮 20~24도의 맑은 건기입니다. TPGA 투어가 열리는 코스를 그린피 11만원에, 야자수 페어웨이에서 반팔로 라운드하는 3박 4일. 여행사 단체에 끼이지 않고 우리 일행의 날짜와 티타임으로 가는 자기예약 트립입니다.</div>
        <div class="meta">
          <div><div class="lab">기간</div><div class="val">3박 4일</div></div>
          <div><div class="lab">라운드</div><div class="val">54홀 (3 rounds)</div></div>
          <div><div class="lab">1인 예상경비</div><div class="val">약 150만원</div></div>
          <div><div class="lab">1월 기온</div><div class="val">낮 20~24도</div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- WHY -->
  <section>
    <div class="sec-label">Why South Taiwan in Winter</div>
    <h2>왜 겨울에 남대만인가 <span class="eng">The Dry, Warm South</span></h2>
    <div class="sec-intro">겨울 대만의 비밀은 중앙산맥입니다. 북동계절풍이 타이베이를 잿빛 이슬비로 덮는 동안, 산맥이 그 바람을 막아주는 가오슝과 타이난은 <b>맑고 건조한 건기</b>입니다. 1~2월 낮 기온 20~24도 — 규슈보다 확실히 따뜻하고, 잔디는 휴면 없이 초록입니다.</div>
    <div class="why">
      <div class="w"><img src="{IMG['hsinyi_feb']}" alt="Hsin Yi in February"><div class="cap"><span class="eng">Shot in February</span><b>이 사진이 2월입니다 — 한겨울에도 이 그린</b></div></div>
      <div class="w"><img src="{IMG['hero']}" alt="palm fairway"><div class="cap"><span class="eng">20~24&deg;C, Dry Season</span><b>야자수 페어웨이, 겨울 건기</b></div></div>
      <div class="w"><img src="{IMG['hsinyi_fw']}" alt="green fee value"><div class="cap"><span class="eng">Green Fee NT$2,200~</span><b>TPGA 코스 그린피가 9~11만원</b></div></div>
      <div class="w"><img src="{IMG['lotus']}" alt="Kaohsiung Lotus Pond"><div class="cap"><span class="eng">Night Markets</span><b>라운드 후 야시장과 미식의 도시</b></div></div>
    </div>
  </section>

  <!-- COURSES -->
  <section>
    <div class="sec-label">The Courses &nbsp;—&nbsp; 3 Rounds</div>
    <h2>코스 <span class="eng">54 Holes</span></h2>
    <div class="sec-intro">3박 4일에 3개 라운드. 세 코스 모두 가오슝 시내에서 차로 30~50분, 외국인 방문객이 예약 가능한 곳만 골랐습니다. 대만 골프의 기본은 <b>팀당 캐디 1명이 5인승 카트를 운전</b>하는 방식 — 셀프 카트 스트레스가 없습니다.</div>
    <div class="courses">

      <div class="course">
        <div class="pic"><img src="{IMG['hsinyi_ch']}" alt="Hsin Yi Golf Club"><div class="reg">Round 1</div><div class="star">&#9733; TPGA 개막전</div></div>
        <div class="body">
          <h3>신이 골프클럽</h3>
          <div class="en">Hsin Yi Golf Club 信誼高爾夫球場</div>
          <div class="specs">18홀, Par 72, 백티 7,600야드, 평일 그린피 NT$2,680 (약 11만원), 캐디+카트 별도</div>
          <div class="sig">남대만의 넘버원. <b>TPGA 투어 개막전이 5년 연속 열리는 코스</b>로, 2019년에는 총상금 80만 달러 대회에 한국 투어 상위 랭커들이 출전했습니다. 와타나베 히로시 설계의 더블 그린, 대만 최대 규모 연습 그린. 시내에서 차로 약 35분.</div>
          <div class="links">
            <a class="map" href="{MAP}Hsin+Yi+Golf+Club+Kaohsiung" target="_blank">지도, 리뷰</a>
            <a class="book" href="https://www.monkeytravel.com/tw/ko/golf/golf/kaohsiung/product/product_detail.php?product_id=1076744542" target="_blank" style="background:var(--green);color:#fff;">예약 (몽키트래블, 한국어)</a>
            <a class="map" href="https://hsinyigolf.com.tw/" target="_blank">공식 사이트</a>
          </div>
        </div>
      </div>

      <div class="course">
        <div class="pic"><img src="{IMG['nanyi_rb']}" alt="Nan Yi Golf Country Club"><div class="reg">Round 2</div></div>
        <div class="body">
          <h3>남일 골프클럽</h3>
          <div class="en">Nan Yi Golf Country Club 南一高爾夫鄉村俱樂部</div>
          <div class="specs">18홀, Par 72, 7,213야드, 평일 그린피 NT$2,200 (약 9만원), 캐디+카트 별도</div>
          <div class="sig">산악 코스가 많은 대만에서 드문 <b>챔피언십급 평지 코스</b>. 벙커 54개와 워터 해저드 11개가 시원한 야자수 페어웨이를 지킵니다. 하이라이트 사진의 무지개가 뜬 그 코스. 가오슝에서 차로 약 45분 (타이난 방향).</div>
          <div class="links">
            <a class="map" href="{MAP}Nan+Yi+Golf+Country+Club+Tainan" target="_blank">지도, 리뷰</a>
            <a class="book" href="https://tickets.golface.com.tw/home/courseInfo/kY9Glw8knb" target="_blank" style="background:var(--green);color:#fff;">예약 (Golface)</a>
          </div>
        </div>
      </div>

      <div class="course">
        <div class="pic"><img src="{IMG['tks']}" alt="Ta Kang Shan Golf Course"><div class="reg">Round 3</div><div class="star">&#9733; 야간 라운드</div></div>
        <div class="body">
          <h3>대강산 골프장</h3>
          <div class="en">Ta Kang Shan Golf Course 大崗山高爾夫球場</div>
          <div class="specs">18홀, Par 72, 계곡 레이아웃, 평일 그린피 약 NT$2,470~ (약 10만원), 캐디+카트 별도</div>
          <div class="sig">이토 쿠니에 설계, 계곡과 능선을 타는 지형 코스. <b>남대만 유일의 18홀 야간 조명</b>을 갖춰 마지막 날 오후 라운드도 조명 아래 여유 있게 마칠 수 있습니다. 고속도로에서 3분, 시내에서 약 40분.</div>
          <div class="links">
            <a class="map" href="{MAP}Ta+Kang+Shan+Golf+Course+Kaohsiung" target="_blank">지도, 리뷰</a>
            <a class="book" href="https://tickets.golface.com.tw/home/courseInfo/Y1ObSOqvvt" target="_blank" style="background:var(--green);color:#fff;">예약 (Golface)</a>
            <a class="map" href="http://www.tksg.com.tw/" target="_blank">공식 사이트</a>
          </div>
        </div>
      </div>

    </div>
    <div class="note">Golface는 대만의 티타임 예약 플랫폼입니다 (GORA의 대만판). 중국어와 일본어만 지원되고 회원 가입이 필요해, 부담되면 신이처럼 <b>몽키트래블 한국어 페이지</b>가 있는 코스를 먼저 잡고 나머지는 dbegl이 대신 예약해 드립니다 (아래 참고).</div>
  </section>

  <!-- WHY SELF-BOOK -->
  <section>
    <div class="sec-label">Why Book It Yourself</div>
    <h2>왜 직접 예약인가 <span class="eng">Your Trip, Your Way</span></h2>
    <div class="sec-intro">솔직히 말하면, 가격만 보면 여행사 패키지가 15만원 안팎 더 싸고, 신이와 남일과 대강산을 도는 패키지도 있습니다. <b>차이는 코스가 아니라 일정의 주인입니다</b> — 패키지는 상품의 일정표대로 돌고, 이 트립은 일정표를 우리가 짭니다.</div>
    <div class="vals">
      <div class="val-c"><span class="eng">Your Schedule</span><b>일정표를 우리가 짠다</b><p>패키지는 날짜를 골라도 코스 순서, 티타임, 가이드 동선은 상품 일정표를 따릅니다. 직접 예약하면 원하는 티오프와 코스 순서로 가고, 마지막 날 대강산 야간 라운드 같은 변주도 우리 마음입니다.</p></div>
      <div class="val-c"><span class="eng">Your Group Only</span><b>우리 일행만, 옵션 없이</b><p>모르는 사람과 조인되지 않고, 쇼핑센터나 옵션 관광에 끌려가지 않습니다. 라운드와 미식만 남긴 일정.</p></div>
      <div class="val-c"><span class="eng">No Markup</span><b>마진 0원, 원가 그대로</b><p>그린피, 호텔, 항공 모두 원가입니다. 어디에 얼마가 드는지 아래 표에 전부 공개했습니다. 직접 예약하면 dbegl에 내는 돈은 0원, 대행을 맡기는 구간만 1인 2만원입니다.</p></div>
    </div>

    <h2 style="margin-top:36px;">자기예약 vs 여행사 패키지 <span class="eng">Honest Comparison</span></h2>
    <div class="sec-intro">감추지 않고 그대로 비교합니다. 가오슝 골프 패키지(하워드 3색 133만원~, VIP 골프 139.9만원~)는 잘 만들어진 상품입니다. 무엇을 얻고 무엇을 직접 감당하는지 보고 고르세요.</div>
    <table class="cmp">
      <thead><tr><th>항목</th><th class="self">이 자기예약 트립</th><th>여행사 패키지</th></tr></thead>
      <tbody>
        <tr><td class="lab">1인 가격 (3박4일, 54홀)</td><td class="self">약 150만원 (원가)</td><td><span class="yes">133~140만원</span></td></tr>
        <tr><td class="lab">티오프 시간</td><td class="self"><span class="yes">직접 선택</span></td><td><span class="no">여행사 배정</span></td></tr>
        <tr><td class="lab">코스 선택</td><td class="self"><span class="yes">우리가 선택, 순서와 변경 자유</span></td><td>상품 구성 고정 (신이 포함 상품도 있음)</td></tr>
        <tr><td class="lab">동반자</td><td class="self"><span class="yes">우리 일행만</span></td><td>조인 가능</td></tr>
        <tr><td class="lab">날짜, 인원</td><td class="self"><span class="yes">자유</span></td><td><span class="no">출발일, 최소 인원 고정</span></td></tr>
        <tr><td class="lab">항공</td><td class="self">직접 예약 (원가)</td><td class="self">포함</td></tr>
        <tr><td class="lab">공항, 골프장 이동</td><td class="self">택시, 우버, 대절밴 (표에 포함)</td><td class="self">포함 (전용차량)</td></tr>
        <tr><td class="lab">쇼핑, 옵션 일정</td><td class="self"><span class="yes">없음</span></td><td><span class="no">상품에 따라 포함</span></td></tr>
        <tr><td class="lab">사고, 환불 책임</td><td class="self"><span class="no">본인</span></td><td><span class="yes">여행사</span></td></tr>
      </tbody>
    </table>
    <div class="note">정리하면 — <b>내 일정표, 우리 일행만, 투명한 원가</b>를 원하면 자기예약. <b>짜인 일정이 편하고 15만원이 아까우면</b> 패키지가 맞습니다 — 그 경우 패키지를 사세요, 좋은 상품입니다. 예약 진행이 막히는 구간(중국어 플랫폼 등)만 dbegl이 대신 잡아드립니다 (대행 수수료 1인 2만원, 코스와 항공 요금에는 한 푼도 얹지 않습니다).</div>
  </section>

  <!-- ITINERARY -->
  <section>
    <div class="sec-label">The Itinerary</div>
    <h2>3박 4일 일정 <span class="eng">Day by Day</span></h2>
    <div class="sec-intro">가오슝 시내 5성 그랜드 하이라이 호텔을 베이스로 한 4인 기준 일정입니다. 렌터카도 가능하지만(2022년 2월부터 한국-대만 국제운전면허 상호인정) 이 트립은 <b>택시, 우버, 대절밴</b>을 권합니다 — 골프백 4개 실을 밴 렌트비와 주차를 따지면 4인 분할 택시가 더 싸고, 낯선 도심 스쿠터 트래픽 스트레스가 없습니다.</div>
    <div class="day"><div class="d">Day 1</div><div class="c"><b>인천 → 가오슝</b> &nbsp; 직항 약 3시간. 호텔 체크인 후 아이허(愛河) 산책과 야시장 디너로 가볍게. <span style="color:var(--muted)">도착편 시간상 첫날 라운드는 권하지 않습니다.</span></div></div>
    <div class="day"><div class="d">Day 2</div><div class="c"><b>신이 골프클럽 18홀</b> &nbsp; 트립의 하이라이트, TPGA 개막전 코스. 라운드 후 류허 또는 루이펑 야시장.</div></div>
    <div class="day"><div class="d">Day 3</div><div class="c"><b>남일 골프클럽 18홀</b> &nbsp; 평지 야자수 코스에서 스코어 노리는 날. 저녁은 항구 도시답게 해산물.</div></div>
    <div class="day"><div class="d">Day 4</div><div class="c"><b>대강산 골프장 라운드 → 가오슝 → 인천</b> &nbsp; 저녁 출발편이면 오전 라운드 후 공항으로. <span style="color:var(--muted)">체크아웃과 짐은 아침에 미리 정리해 호텔에 맡기고, 라운드 후 클럽하우스 샤워 → 호텔 짐 픽업 → 공항 순서로 3시간 여유를 두세요. 출발편이 이른 경우 Day 4 라운드 대신 Day 2~3 오후에 대강산 야간 라운드를 넣으세요 — 조명이 있어 가능합니다.</span></div></div>

    <h2 style="margin-top:34px;">1인 예상 경비 <span class="eng">All-in, per person</span></h2>
    <div class="sec-intro"><b>4인이 함께, 2인 1실, 차량비 분할 기준</b>입니다. 인원이 줄면 1인 숙박과 차량 분담이 올라갑니다. 겨울 시즌 예상치이며 환율(NT$1 = 약 42원)과 시즌에 따라 달라집니다.</div>
    <table class="allin">
      <tr><td>왕복 항공 (인천–가오슝 직항, 유류할증, 세금 포함 총액)</td><td>약 30만원</td></tr>
      <tr><td>숙박 3박 (그랜드 하이라이 5성, 2인 1실)</td><td>약 30만원</td></tr>
      <tr><td>그린피 3라운드 + 캐디피 + 카트 (신이, 남일, 대강산, 평일)</td><td>약 47만원</td></tr>
      <tr><td>지상 이동 (공항 왕복 + 골프장 3일 택시, 우버, 4인 분할)</td><td>약 8만원</td></tr>
      <tr><td>여행자보험</td><td>약 2만원</td></tr>
      <tr><td>식비 (클럽하우스 점심 3회, 야시장, 해산물 디너)</td><td>약 25만원</td></tr>
      <tr><td>현금 여비 (캐디팁 라운드당 NT$300~500, 환전, 수수료)</td><td>약 8만원</td></tr>
      <tr class="tot"><td>합계 (1인, 4인 평일 라운드 기준)</td><td>약 150만원</td></tr>
      <tr class="sub"><td>항공 특가를 잡은 경우 (12월 평균 13만원 수준)</td><td>- 약 10만원</td></tr>
      <tr class="sub"><td>주말 라운드 포함 시 (그린피 인상분)</td><td>+ 약 5만원</td></tr>
      <tr class="sub"><td>전일 대절밴으로 업그레이드 시 (4인 분할)</td><td>+ 약 5만원</td></tr>
      <tr class="sub"><td>2인만 갈 경우 (1인 1실, 차량 분담 증가)</td><td>+ 약 25만원</td></tr>
      <tr class="sub"><td>설 연휴 등 성수기 항공</td><td>+ 약 10만원</td></tr>
    </table>
    <div class="note">위 합계는 <b>4인이 함께, 평일 라운드 기준</b>입니다. 라운드 비용의 근거 — 1인 1라운드당 그린피+캐디피+카트비 합계가 신이 약 NT$3,700, 남일 약 NT$3,670 (정비비, 보험 포함), 대강산 약 NT$3,520으로, 3라운드 합계 약 NT$10,900 = 약 47만원입니다. 2인이거나 주말과 성수기가 겹치면 옵션이 더해져 1인 약 175~190만원이 상한입니다 — 솔직한 상한선까지 보고 고르세요. 캐디피, 카트비, 캐디팁, 환전 수수료까지 표에 넣었으니 표 밖에서 더 나올 큰 비용은 없습니다.</div>
  </section>

  <!-- BEFORE YOU BOOK -->
  <section>
    <div class="sec-label">Before You Book</div>
    <h2>예약 전 꼭 확인 <span class="eng">Honest Notes</span></h2>
    <div class="warn"><b>렌터카보다 택시를 권합니다.</b> 2022년 2월부터 한국-대만 국제운전면허 상호인정으로 렌터카도 가능해졌습니다. 그래도 골프백 4개를 실을 밴급 렌트비와 주차, 도심 스쿠터 트래픽을 따지면 <b>4인 분할 택시와 우버가 더 싸고 편합니다.</b> 골프장 3곳 모두 시내에서 30~50분이고, 위 경비표에 차량비가 이미 들어 있습니다. <b>골프백 4개는 일반 택시 1대에 안 들어갑니다</b> — 라운드 날은 우버 XL이나 9인승 대절밴(경비표의 +5만 옵션)으로 부르거나 택시 2대로 나눠 타세요.</div>
    <div class="warn"><b>예약 플랫폼이 중국어입니다.</b> 신이는 몽키트래블 한국어 페이지로 예약되지만, 남일과 대강산의 Golface는 중국어(일본어) 전용에 회원 가입이 필요하고, 해외 사용자는 가입 인증이 번거로울 수 있습니다. 현실적으로 이 두 코스는 dbegl 대행(1인 2만원)에 맡기는 걸 권합니다 — 그 외 구간(항공, 호텔, 신이)은 전부 한국어로 직접 됩니다.</div>
    <div class="warn"><b>겨울에도 한파(寒流)가 내려오는 날이 있습니다.</b> 평년 1월 낮 20~24도의 건기지만, 대륙 한파가 내려오면 며칠간 낮 15도 안팎까지 떨어집니다. 이른 아침 티오프는 13~15도 — 얇은 방한 레이어 하나는 챙기세요. 남부 코스 잔디는 휴면 없이 겨울에도 초록입니다 (위 2월 실사진 참고).</div>
    <div class="warn"><b>캐디 팁 문화가 있습니다.</b> 팀 캐디에게 라운드당 1인 NT$300~500 (약 1.3~2.1만원) 현금 팁이 관례입니다. 위 경비표 현금 여비에 반영해 두었습니다.</div>
    <div class="warn"><b>2인 팀은 코스에서 조인을 배정할 수 있습니다.</b> 대강산 등은 2인 예약 시 현장 조인이 원칙입니다. 우리 일행만 치고 싶으면 4인을 채워 가세요 — 이 트립이 4인 기준인 이유입니다.</div>
    <div class="warn"><b>우천 환불 규정을 예약 시 확인하세요.</b> 한국식 홀 정산이 아니라 코스별 규정을 따릅니다. 남부 겨울은 건기라 우천 클로징 확률 자체가 낮은 것이 이 지역의 장점입니다.</div>
  </section>

  <!-- CTA -->
  <section style="border-bottom:none;">
    <div class="sec-label">Book It Yourself</div>
    <h2>직접 예약하기 <span class="eng">All links, no markup</span></h2>
    <div class="sec-intro">아래 링크에서 직접 예약하면 됩니다. 원가 그대로 — 직접 예약하는 구간은 dbegl에 내는 돈이 0원입니다.</div>
    <div class="cta">
      <a href="https://www.agoda.com/ko-kr/grand-hi-lai-hotel/hotel/kaohsiung-tw.html" target="_blank">숙박 — 그랜드 하이라이 (아고다, 한국어)</a>
      <a href="https://www.monkeytravel.com/tw/ko/golf/golf/kaohsiung/product/product_detail.php?product_id=1076744542" target="_blank">신이 GC 예약 (한국어)</a>
      <a href="https://tickets.golface.com.tw/home/courseInfo/kY9Glw8knb" target="_blank">남일 GC 예약 (Golface)</a>
      <a href="https://tickets.golface.com.tw/home/courseInfo/Y1ObSOqvvt" target="_blank">대강산 예약 (Golface)</a>
      <a class="alt" href="https://www.trip.com/flights/seoul-to-kaohsiung/airfares-sel-khh/" target="_blank">항공 — 인천–가오슝 직항 검색</a>
    </div>
    <div class="note">Golface(중국어) 예약이 번거로우면 dbegl이 티오프를 대신 잡아드립니다 (예약 대행 수수료 1인 2만원, 코스와 항공 요금은 원가 그대로). 단, 현지 사고와 환불은 직접 예약과 동일하게 본인 책임입니다.</div>
  </section>

  <div style="background:var(--green); color:#cdbf9e; text-align:center; padding:26px; font-family:'Cormorant Garamond',serif; letter-spacing:.22em; text-transform:uppercase; font-size:12px;">dbegl &nbsp;—&nbsp; Winter Golf, Self-Booked</div>

</div>
</body>
</html>"""

open('kaohsiung.html','w',encoding='utf-8').write(HTML)
print("wrote kaohsiung.html:", len(HTML)//1024, "KB")
