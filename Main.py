import streamlit as st
import random
import pandas as pd
import base64
import string
from datetime import timedelta

def main():
    # Session state 초기화
    if 'result' not in st.session_state:
        st.session_state.result = {}

    # 변수
    korean_word = ["가","각","간","갇","갈","갉","갊","감","갑","값","갓","갔","강","갖","갗","같","갚","갛","개","객","갠","갵","갬","갭","갯","갰","갱","갸","갹","갼","걀","걑","걍","걔","걘","걭","거","걱","건","걷","거","걸","걺","검","겁","것","것","겅","겆","겉","겊","겋","게","겐","겔","겜","겝","겟","겠","겡","겨","격","격","견","겯","결","겸","겹","겻","겻","경","곁","계","곈","곌","곕","곗","고","곡","곤","곧","골","곪","곬","곯","곰","곱","곳","공","곶","과","곽","관","괄","괆","괌","괍","괏","광","괘","괜","괠","괩","괬","괭","괴","괵","괸","괼","굄","굅","굇","굉","교","굔","굘","굡","굣","구","국","군","굳","굴","굵","굶","굻","굼","굽","굿","궁","궂","궈","궉","괏","굉","교","굔","굘","굡","굣","구","국","군","굳","굴","굵","굶","굻","굼","굽","굿","궁","궂","궈","궉","권","궐","궛","궝","궤","궷","귀","귁","귄","귈","귐","귑","귓","규","균","귤","그","극","근","귿","글","긁","금","급","긋","긍","긔","기","긱","긴","긷","길","긺","김","깁","깃","깅","깆","깊","까","깍","깎","깐","깔","깖","감","깝","깟","갔","강","깥","깨","깩","깬","깰","깸","깹","깻","깼","깽","꺄","꺅","꺌","꺼","꺽","꺾","껀","껄","껌","껍","껏","껐","껑","께","껙","껜","껨","껫","껭","껴","껸","껼","꼇","꼈","꼍","꼐","꼬","꼭","꼰","꼲","꼴","꼼","꼽","꼿","꽁","꽂","꽃","꽈","꽉","꽐","꽜","꽝","꽤","꽥","꽹","꾀","꾄","꾈","꾐","꾑","꾕","꾜","꾸","꾹","꾼","꿀","꿇","꿈","꿉","꿋","꿍","꿎","꿔","꿜","꿨","꿩","꿰","꿱","꿴","꿸","뀀","뀁","뀄","뀌","뀐","뀔","뀜","뀝","뀨","끄","꾝","꾠","꾫","꾤","꾦","꾫","꾬","꾭","꾯","꾱","끝","끼","끽","낀","낄","낌","낍","낏","낑","나","낙","낚","난","낟","날","낡","낢","남","납","낫","났","낭","낮","낯","낱","낳","내","낵","낸","낼","냄","냅","냇","냈","냉","냐","냑","냔","냘","냠","냥","너","넉","넔","넌","널","넒","넓","넘","넙","넛","넜","넝","넣","네","넥","넨","넬","넴","넵","넷","넸","넹","녀","녁","년","녈","념","녑","녔","녕","녘","녜","넨","노","녹","논","놀","놂","놈","놉","놋","농","높","놓","놔","놘","놜","놨","뇌","뇐","뇔","뇜","뇝","뇟","뇨","뇩","뇬","뇰","뇹","뇻","뇽","누","눅","눈","눋","눌","눔","눕","눗","눙","뉘","뉬","눼","뉘","뉜","뉠","뉨","뉩","뉴","뉵","뉼","늄","늅","늉","느","늑","는","늘","늙","늚","늠","늡","늣","능","늦","늪","늬","늰","늴","니","닉","닌","닐","닒","님","닙","닛","닝","닢","다","닥","닦","단","닫","달","닭","닮","닯","닳","담","답","닷","닸","당","닺","닻","닿","대","댁","댄","댈","댐","댑","댓","댔","댕","댜","더","덕","덖","던","덛","덜","덞","덟","덤","덥","덧","덩","덫","덮","데","덱","덴","델","뎀","뎁","뎃","뎃","뎅","뎌","뎐","뎔","뎠","뎡","데","뎬","도","독","돈","돋","돌","돎","돐","돔","돕","돗","동","돛","돝","돠","돤","돨","돼","됐","되","된","될","됨","됩","됫","됴","두","둑","둔","둘","둠","둡","둣","둥","둬","뒀","뒈","뒝","뒤","뒨","뒬","뒵","뒷","뒹","듀","듄","듈","듐","듕","드","득","든","듣","들","듦","듬","듭","듯","등","듸","디","딕","딘","딛","딜","딤","딥","딧","딨","딩","딪","따","딱","단","딸","땀","땁","땃","닸","땅","닿","때","땍","땐","땔","땜","땝","땟","땠","땡","떠","떡","떤","떨","떪","떫","떰","떱","떳","덨","떵","떻","때","떽","뗀","뗄","뗌","뗍","뗏","뗐","뗑","뗘","뗬","또","똑","똔","똘","똥","똬","똴","뙈","뙤","뙨","뚜","뚝","뚠","뚤","뚫","뚬","둥","뛔","뛰","뛴","뛸","뜀","뜁","뜅","뜨","뜩","뜬","뜯","뜰","뜸","뜹","뜻","띄","띈","띌","띔","띕","띠","띤","띨","띰","띱","띳","띵","라","락","란","랄","람","랍","랏","랐","랑","랒","랖","랗","래","랙","랜","랠","램","랩","랫","랬","랭","랴","략","랸","럇","량","러","럭","런","럴","럼","럽","럿","렀","렁","렇","레","렉","렌","렐","렘","렙","렛","렝","려","력","련","렬","렴","렵","렷","렸","령","례","렌","롑","롓","로","록","론","롤","롬","롭","롯","롱","롸","롼","뢍","뢨","뢰","뢴","뢸","룀","룁","룃","룅","료","룐","룔","룝","룟","룡","루","룩","룬","룰","룸","룹","룻","룽","뤄","뤘","뤠","뤼","뤽","륀","륄","륌","륏","륑","류","륙","륜","률","륨","륩","륫","륭","르","륵","른","를","름","릅","릇","릉","릊","릍","릎","리","릭","린","릴","림","립","릿","링","마","막","만","많","맏","말","맑","맒","맘","맙","맛","망","맞","맡","맣","매","맥","맨","맬","맴","맵","맷","맷","맹","맺","먀","먁","먈","먕","머","먹","먼","멀","멂","멈","멉","멋","멍","멎","멓","메","멕","멘","멜","멤","멥","멧","멧","멩","며","멱","면","멸","몃","몄","명","몇","몌","모","목","몫","몬","몰","몲","몸","몹","못","몽","뫄","뫈","뫘","뫼","묀","묄","묍","묏","묑","묘","묜","묠","묩","묫","무","묵","묶","문","묻","물","묽","묾","뭄","뭅","뭇","뭉","뭍","뭏","뭐","뭔","뭘","뭡","뭣","뭬","뮈","뮌","뮐","뮤","뮨","뮬","뮴","뮷","므","믄","믈","믐","믓","미","믹","민","믿","밀","밂","밈","밉","밋","밋","밍","및","밑","바","박","밖","밗","반","받","발","밝","밞","밥","밤","밥","밧","방","밭","배","백","밴","밸","뱀","뱁","뱃","뱃","뱅","뱉","뱌","뱍","뱐","뱝","버","벅","번","벋","벌","벎","범","법","벗","벙","벚","베","벡","벤","벧","벨","벰","벱","벳","벴","벵","벼","벽","변","별","볍","볏","볐","병","볕","베","볜","보","복","복","본","볼","봄","봅","봇","봉","봐","봔","봤","봬","뵀","뵈","뵈","뵉","뵌","뵐","뵘","뵙","뵤","뵨","부","북","분","붇","불","붉","붊","붐","붑","붓","붕","붙","붚","붜","붤","붰","붸","뷔","뷕","뷘","뷜","뷩","뷰","뷴","뷸","븀","븃","븅","브","븍","븐","블","븜","븝","븟","비","빅","빈","빌","빎","빔","빕","빗","빙","빚","빛","빠","빡","빤","빨","빪","빰","빱","빳","빴","방","빻","빼","빽","뺀","뺄","뺌","뺍","뺏","뺐","뺑","뺘","뱍","뺨","뻐","뻑","뻔","뻗","뻘","뻠","뻣","뻤","뻥","뻬","뼁","뼈","뼉","뼘","뼙","뼛","뼜","뼝","뽀","복","뽄","뽈","뽐","뽑","뽕","뾔","뾰","뿅","뿌","뿍","뿐","뿔","뿜","뿟","뿡","쀼","쁑","쁘","븐","쁠","쁨","쁩","삐","삑","삔","삘","삠","삡","삣","삥","사","삭","삯","산","삳","살","삵","삶","삼","삽","삿","샀","상","샅","새","색","샌","샐","샘","샙","샛","샛","생","샤","샥","샨","샬","샴","샵","샷","샹","새","섄","섈","섐","생","서","석","섞","섟","선","섣","설","섦","섧","섬","섭","섯","섰","성","섶","세","섹","센","셀","셈","셉","셋","셌","셍","셔","셕","션","셜","셤","셥","셧","셨","셩","셰","셴","셸","셍","소","속","솎","손","솔","솖","솜","솝","솟","송","솥","솨","솩","솬","솰","솽","쇄","쇈","쇌","쇔","쇗","쇘","쇠","쇤","쇨","쇰","쇱","쇳","쇼","쇽","숀","숄","숌","숍","숏","숑","수","숙","순","숟","술","숨","숩","숫","숭","숯","숱","숲","숴","쉈","쉐","쉑","쉔","쉘","쉠","쉥","쉬","쉭","쉰","쉴","쉼","쉽","쉿","슁","슈","슉","슐","슘","슛","슝","스","슥","슨","슬","슭","슴","습","슷","승","시","식","신","싣","실","싫","심","십","싯","싱","싶","싸","싹","싻","싼","쌀","쌈","쌉","쌌","쌍","쌓","쌔","쌕","쌘","쌜","쌤","쌥","쌨","쌩","썅","써","썩","썬","썰","썲","썸","썹","섰","썽","쎄","쎈","쎌","셴","쏘","쏙","쏜","쏟","쏠","쏢","쏨","쏩","쏭","쏴","쏵","쏸","쐈","쐐","쐤","쐬","쐰","쐴","쐼","쐽","쑈","쑤","숙","쑨","쑬","쑴","쑵","쑹","쒀","쓌","쒜","쒸","쒼","쓩","쓰","쓱","쓴","쓸","슮","쓿","씀","습","씌","씐","씔","씜","씨","씩","씬","씰","씸","씹","씻","씽","아","악","안","앉","않","알","앍","앎","앓","암","압","앗","았","앙","앝","앞","애","액","앤","앨","앰","앱","앳","앴","앵","야","약","얀","얄","얇","얌","얍","얏","양","얕","얗","얘","얜","얠","얩","어","억","언","얹","얻","얼","얽","얾","엄","업","없","엇","었","엉","엊","엌","엎","에","엑","엔","엘","엠","엡","엣","엥","여","역","엮","연","열","엶","엷","염","엽","엾","엿","엿","영","옅","옆","옇","예","옌","옐","옘","엡","옛","옛","오","옥","온","올","옭","옮","옰","옳","옴","옵","옷","옹","옻","와","왁","완","왈","왐","왑","왓","왓","왕","왜","왝","왠","왬","왯","왱","외","왹","왼","욀","욈","욉","욋","욍","요","욕","욘","욜","욤","욥","욧","용","우","욱","운","울","욹","욺","움","웁","웃","웅","워","웍","원","월","웜","웝","웠","웡","웨","웩","웬","웰","웸","웹","웽","위","윅","윈","윌","윔","윕","윗","윙","유","육","윤","율","윰","윱","윳","융","윻","으","윽","은","을","읊","음","읍","읏","응","읒","읓","읔","읕","읖","읗","의","읜","읠","읨","읫","이","익","인","일","읽","읾","잃","임","입","잇","있","잉","잊","잎","자","작","잔","잖","잗","잘","잚","잠","잡","잣","잣","장","잦","재","잭","잰","잴","잼","잽","잿","쟀","쟁","쟈","쟉","쟌","쟎","쟐","쟘","쟝","쟤","쟨","쟬","저","적","전","절","젊","점","접","젓","정","젖","제","젝","젠","젤","젬","젭","젯","젱","져","젼","졀","졈","졉","졌","졍","졔","조","족","존","졸","졺","좀","좁","좃","종","좆","좇","좋","좌","좍","좔","좝","좟","좡","좨","좼","좽","죄","죈","죌","죔","죕","죗","죙","죠","죡","죤","죵","주","죽","준","줄","줅","줆","줌","줍","줏","중","줘","줬","줴","쥐","쥑","쥔","쥘","쥠","쥡","쥣","쥬","쥰","쥴","쥼","즈","즉","즌","즐","즘","즙","즛","증","지","직","진","짇","질","짊","짐","집","짓","징","짖","짙","짚","짜","짝","잔","짢","짤","짭","짬","짭","짯","짰","짱","째","짹","잰","쨀","째","짹","잰","잴","잼","쨉","쨋","쨌","쟁","쟈","쟌","쟝","쩌","적","전","절","쩜","접","쩟","젓","정","쩨","젱","쪄","졌","쪼","족","존","쫄","쫌","좁","쫏","쫑","좇","쫘","쫙","쫠","쫴","좼","쬐","쬔","쬘","쬠","쬡","쭁","쭈","쭉","준","쭐","쭘","쭙","쭝","쭤","쭸","쭹","쮜","쮸","쯔","쯤","쯧","쯩","찌","찍","찐","찔","찜","찝","찡","찢","찧","차","착","찬","찮","찰","참","찹","찻","찼","창","찾","채","책","챈","챌","챔","챕","챗","챘","챙","챠","챤","챦","챨","챰","챵","처","척","천","철","첨","첩","첫","첫","청","체","첵","첸","첼","쳄","쳅","쳇","쳉","쳐","쳔","쳣","체","촁","초","촉","촌","촐","촘","촙","촛","총","촤","촨","촬","촹","최","쵠","쵤","쵬","쵭","쵯","쵱","쵸","춈","추","축","춘","출","춤","춥","춧","충","취","췄","췌","췐","취","췬","췰","췸","췹","췻","췽","츄","츈","츌","츔","츙","츠","측","츤","츨","츰","츱","츳","층","치","칙","친","칟","칠","칡","침","칩","칫","칭","카","칵","칸","칼","캄","캅","캇","캉","캐","캑","캔","캘","캠","캡","캣","캤","캥","캬","캭","컁","커","컥","컨","컫","컬","컴","컵","컷","컸","컹","케","켁","켄","켈","켐","켑","켓","켕","켜","켠","켤","켬","켭","켯","켯","켱","켸","코","콕","콘","콜","콤","콥","콧","콩","콰","콱","콴","콸","쾀","쾅","쾌","쾡","쾨","쾰","쿄","쿠","쿡","쿤","쿨","쿰","쿱","쿳","쿵","쿼","퀀","퀄","퀑","퀘","퀭","퀴","퀵","퀸","퀼","큄","큅","큇","큉","큐","큔","큘","큠","크","큭","큰","클","큼","큽","킁","키","킥","킨","킬","킴","킵","킷","킹","타","탁","탄","탈","탉","탐","탑","탓","탔","탕","태","택","탠","탤","탬","탭","탯","탰","탱","탸","턍","터","턱","턴","털","턺","텀","텁","텃","텄","텅","테","텍","텐","텔","템","텝","텟","텡","텨","텬","텼","톄","톈","토","톡","톤","톨","톰","톱","톳","통","톺","톼","퇀","퇘","퇴","퇸","툇","툉","툐","투","툭","툰","툴","툼","토","톡","톤","톨","톰","톱","톳","통","톺","톼","퇀","퇘","퇴","퇸","툇","툉","툐","투","툭","툰","툴","툼","툽","툿","퉁","퉈","퉜","퉤","튀","튁","튄","튈","튐","튑","튕","튜","튠","튤","튬","튱","트","특","튼","튿","틀","틂","틈","틉","틋","틔","틘","틜","틤","틥","티","틱","틴","틸","팀","팁","팃","팅","파","팍","팍","판","팔","팖","팜","팝","팟","팠","팡","팥","패","팩","팬","팰","팸","팹","팻","팼","팽","퍄","퍅","퍼","퍽","펀","펄","펌","펍","펏","펐","펑","페","펙","펜","펠","펨","펩","펭","펴","편","펼","폄","폅","폈","평","폐","폘","폡","폣","포","폭","폰","폴","폼","폽","폿","퐁","퐈","퐝","푀","푄","표","푠","푤","푭","푯","푸","푹","푼","푿","풀","풂","품","풉","풋","풍","풔","풩","퓌","퓐","퓔","퓜","퓟","퓨","퓬","퓰","퓸","퓻","퓽","프","픈","플","픔","픕","픗","피","픽","핀","필","핌","핍","핏","핑","하","학","한","할","핥","함","합","핫","항","해","핵","핸","핼","햄","햅","햇","햇","행","햐","향","허","헉","헌","헐","헒","험","헙","헝","헤","헥","헨","헬","헴","헵","헷","헹","혀","혁","현","혈","혐","협","혓","혔","형","헤","혠","헬","혭","호","혹","혼","홀","홅","홈","홉","홋","홍","홑","화","확","환","활","홧","황","홰","홱","홴","횃","횅","회","획","횐","횔","횝","횟","횡","효","횬","횰","횹","횻","후","훅","훈","훌","훑","훔","훗","훙","휘","휜","휠","휨","휭","훼","훽","휀","휄","휑","휘","휙","휜","휠","휨","휩","휫","휭","휴","휵","휸","휼","흄","흇","흉","흐","흑","흔","흖","흗","흘","흙","흠","흡","흣","흥","흩","희","흰","흴","흼","흽","힁","히","힉","힌","힐","힘","힙","힛","힝"]
    choseongs = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
    jungsongs = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
    English_first_name_100 = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper', 'Evelyn', 'Abigail', 'Emily', 'Elizabeth', 'Sofia', 'Avery', 'Ella', 'Scarlett', 'Grace', 'Chloe', 'Victoria', 'Riley', 'Aria', 'Lily', 'Aubrey', 'Zoey', 'Penelope', 'Layla', 'Lillian', 'Natalie', 'Hannah', 'Avery', 'Samuel', 'Benjamin', 'Elijah', 'Oliver', 'William', 'James', 'Alexander', 'Henry', 'Michael', 'Daniel', 'Matthew', 'Jackson', 'Sebastian', 'Aiden', 'David', 'Joseph', 'Carter', 'Wyatt', 'Jayden', 'Noah', 'Ethan', 'Luke', 'Jack', 'Owen', 'Caleb', 'Gabriel', 'Isaac', 'Dylan', 'Levi', 'Lucas', 'Alexander', 'Mason', 'Liam', 'Logan', 'Ethan', 'Benjamin', 'James', 'William', 'Henry', 'Oliver', 'Michael', 'Daniel', 'Elijah', 'Matthew', 'Samuel', 'David', 'Joseph', 'Andrew', 'John', 'Anthony', 'Joshua', 'Christopher', 'Jackson', 'Nathan', 'Thomas', 'Carter', 'Caleb', 'Luke', 'Christian', 'Hunter', 'Henry', 'Jonathan', 'Owen', 'Landon', 'Isaac', 'Gabriel', 'Eli']
    English_last_name_100 = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Miller', 'Davis', 'Garcia', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Lewis', 'Robinson', 'Walker', 'Hall', 'Young', 'Allen', 'King', 'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Mitchell', 'Carter', 'Roberts', 'Turner', 'Phillips', 'Campbell', 'Parker', 'Evans', 'Edwards', 'Collins', 'Stewart', 'Sanchez', 'Morris', 'Rogers', 'Reed', 'Cook', 'Morgan', 'Bell', 'Murphy', 'Bailey', 'Cooper', 'Richardson', 'Cox', 'Howard', 'Ward', 'Torres', 'Peterson', 'Gray', 'Ramirez', 'James', 'Watson', 'Brooks', 'Kelly', 'Sanders', 'Price', 'Bennett', 'Wood', 'Barnes', 'Ross', 'Henderson', 'Coleman', 'Jenkins', 'Perry', 'Powell', 'Long', 'Patterson', 'Hughes', 'Flores', 'Washington', 'Butler', 'Simmons', 'Foster', 'Gonzales', 'Bryant', 'Alexander', 'Russell']
    # 함수
    def make_None(input_list, none_count):
        if none_count <= len(input_list):
            indices_to_change = random.sample(range(len(input_list)-1), none_count)
            for index in indices_to_change:
                input_list[index] = None
            return input_list
        else:
            print("숫자가 리스트 길이보다 큽니다.")
    def download_link(df, filename, text):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
        return href
    def fill_df(df):
        max_length = max(len(values) for values in df.values())
        filled_df = {key: values + [None] * (max_length - len(values)) for key, values in df.items()}
        df = pd.DataFrame(filled_df)
        return df

    # 구현
    st.title("원하는 만큼 RAW를 생성하세요")
    RAWS = st.number_input("Raws", 10, 1000000, step=50)
    st.markdown("---")
    col21,col22 =st.columns(2)
    if st.session_state.result is not {}:
        for i in list(st.session_state.result.keys()):
            if col22.button(f"{i}_column_delete"):
                st.session_state.result.pop(i)
                st.experimental_rerun()
        if st.session_state.result != {}:
            col21.write(fill_df(st.session_state.result))

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        column_name = st.text_input("컬럼명 설정")
        options = ["User_Set", "NAME", "DATE", "TIME", "OPTION"]
        ITEM = st.selectbox("Item", options)

        if ITEM == options[0]:  # User_Set 설정
            TYPE = st.selectbox("Type", ["INT", "STRING", "FLOAT"])
            if TYPE == "INT":
                MIN_RANGE = st.number_input("Min Value", 0)
                MAX_RANGE = st.number_input("Max Value", 1)
                # MAX_DUP = st.slider("최대 중복허용(%)", 0, 100, 100)
                NONE_SET = st.number_input("Create missing value", 0)
            if TYPE == "STRING":
                STR_MIN_SIZE = st.number_input("Text Length",0)
                STR_MAX_SIZE = st.number_input("Text Length",1)
                STR_LANGUAGE = st.multiselect("Choose language",["영어_대문자","영어_소문자","한글_자음","한글_모음","한글_글자"])
                NONE_SET = st.number_input("Create missing value", 0)
            if TYPE == "FLOAT":
                DECIMAL_PLACE = st.number_input("decimal_places",0)
                MIN_RANGE = st.number_input("Min Value", 0)
                MAX_RANGE = st.number_input("Max Value", 1)
                # MAX_DUP = st.slider("최대 중복허용(%)", 0, 100, 100)
                NONE_SET = st.number_input("Create missing value", 0)


        if ITEM == options[1]:  # 이름 설정
            NAME_SET = st.selectbox("Choose Name Type", ["First_name", "Last_name", "Full_name"])
            if NAME_SET == "Full_name":
                COUPLER = st.selectbox("Choose Name Coupler",[" ","_","-","/","^"])
            NONE_SET = st.number_input("Create missing value", 0)

        if ITEM == options[2]: # date
            START_DATE = st.date_input("Start Date",)
            END_DATE = st.date_input("End Date")
            NONE_SET = st.number_input("Create missing value", 0)
            
        if ITEM == options[3]: # time
            TIME_UNIT = st.selectbox("Time Unit",["Hour:Minute","Hour:Minute:Second","Minute:Second"])
            if TIME_UNIT == "Hour:Minute":
                c1,c2 = st.columns(2)
                start_Hour = c1.number_input("start_Hour",0,24,0)
                start_Minute = c2.number_input("start_Minute",0,59,0)
                total_start_seconds = start_Hour * 3600 + start_Minute * 60
                end_Hour = c1.number_input("End_Hour",0,24,0)
                end_Minute = c2.number_input("End_Minute",0,59,0)
                total_end_seconds = end_Hour * 3600 + end_Minute * 60
                NONE_SET = st.number_input("Create missing value", 0)
            if TIME_UNIT =="Hour:Minute:Second":
                c1,c2,c3 = st.columns(3)
                start_Hour = c1.number_input("start_Hour",0,24,0)
                start_Minute = c2.number_input("start_Minute",0,59,0)
                start_Second = c3.number_input("start_Second",0,59,0)
                total_start_seconds = start_Hour * 3600 + start_Minute * 60 + start_Second
                end_Hour = c1.number_input("End_Hour",0,24,0)
                end_Minute = c2.number_input("End_Minute",0,59,0)
                end_Second = c3.number_input("End_Second",0,59,0)
                total_end_seconds = end_Hour * 3600 + end_Minute * 60 + end_Second
                NONE_SET = st.number_input("Create missing value", 0)
            if TIME_UNIT =="Minute:Second":
                c2,c3 = st.columns(2)
                start_Minute = c2.number_input("start_Minute",0,59,0)
                start_Second = c3.number_input("start_Second",0,59,0)
                total_start_seconds = start_Minute * 60 + start_Second
                end_Minute = c2.number_input("End_Minute",0,59,0)
                end_Second = c3.number_input("End_Second",0,59,0)
                total_end_seconds = end_Minute * 60 + end_Second
                NONE_SET = st.number_input("Create missing value", 0)
                
                
        if ITEM == options[4]: # option
            OPTION_OPTIONS = st.text_input("List Up Options split by ','")
            option_list = [option.strip() for option in OPTION_OPTIONS.split(',')]
            NONE_SET = st.number_input("Create missing value", 0)
            
        if col2.button("Make column"):  
            data_colum = []
            if ITEM == options[0]:
                if TYPE == "INT":
                    for i in range(RAWS):
                        random_number = random.randint(MIN_RANGE, MAX_RANGE)
                        data_colum.append(random_number)
                            
                if TYPE == "STRING":
                    if STR_LANGUAGE == []:
                        st.warning("Choose language")
                    else:
                        data_colum = []
                        language_list =[]
                        for j in range(RAWS):
                            random_str_size = random.randint(STR_MIN_SIZE,STR_MAX_SIZE)
                            letter = []
                            if random_str_size == 0:
                                result_string = ""
                            else:
                                for i in range(random_str_size):
                                    if len(STR_LANGUAGE) == 1:
                                        random_language = 0
                                    else:
                                        random_language = random.randint(0,len(STR_LANGUAGE)-1)
                                    if STR_LANGUAGE[random_language] == "영어_소문자":
                                        language_list = list(string.ascii_lowercase)
                                    elif STR_LANGUAGE[random_language] == "영어_대문자":
                                        language_list = list(string.ascii_uppercase)
                                    elif STR_LANGUAGE[random_language] == "한글_자음":
                                        language_list = choseongs
                                    elif STR_LANGUAGE[random_language] == "한글_모음":
                                        language_list = jungsongs
                                    elif STR_LANGUAGE[random_language] == "한글_글자":
                                        language_list = korean_word
                                    letter_source = language_list[random.randint(0,len(language_list)-1)]
                                    letter.append(letter_source)
                                    result_string = ''.join(letter)
                            data_colum.append(result_string)
                if TYPE == "FLOAT":
                    for i in range(RAWS):
                        random_number = random.uniform(MIN_RANGE, MAX_RANGE)
                        random_float = f"{random_number:.{DECIMAL_PLACE}f}"
                        data_colum.append(random_float)
            if ITEM == options[1]: # NAME
                if NAME_SET == "First_name":
                    for i in range(RAWS):
                        data_colum.append(English_first_name_100[random.randint(0,99)])
                elif NAME_SET == "Last_name":
                    for i in range(RAWS):
                        data_colum.append(English_last_name_100[random.randint(0,99)])
                elif NAME_SET == "Full_name":
                    for i in range(RAWS):
                        a = English_first_name_100[random.randint(0,99)]
                        b = English_last_name_100[random.randint(0,99)]
                        c = a+f"{COUPLER}"+b
                        data_colum.append(c)
                        
            if ITEM == options[2]: # DATE
                if START_DATE and END_DATE and START_DATE <= END_DATE:
                    for i in range(RAWS):
                        days_between = (END_DATE - START_DATE).days + 1
                        random_days = random.randint(0, days_between - 1)
                        random_date = START_DATE + timedelta(days=random_days)
                        data_colum.append(random_date)
                elif START_DATE and END_DATE:
                    st.write("End Date should be greater than or equal to Start Date")
                    
            if ITEM == options[3]: # TIME
                for i in range(RAWS):
                    random_seconds = random.randint(total_start_seconds, total_end_seconds)
                    random_hour = random_seconds // 3600
                    random_minute = (random_seconds % 3600) // 60
                    random_second = random_seconds % 60
                    if TIME_UNIT == "Hour:Minute":
                        data_colum.append(f"{random_hour:02d}:{random_minute:02d}")
                    if TIME_UNIT =="Hour:Minute:Second":
                        data_colum.append(f"{random_hour:02d}:{random_minute:02d}:{random_second:02d}")
                    if TIME_UNIT =="Minute:Second":
                        data_colum.append(f"{random_minute:02d}:{random_second:02d}")
            
            if ITEM == options[4]: # OPTINON
                for i in range(RAWS):
                    op = option_list[random.randint(0,len(option_list)-1)]
                    data_colum.append(op)
            if data_colum != []:
                if NONE_SET != 0:
                    data_colum = make_None(data_colum,NONE_SET)  
                st.session_state.result[column_name] = data_colum
                st.experimental_rerun()
    st.markdown("---")
    cc1,cc2,cc3,cc4 = st.columns(4)
    couple_start_column = cc1.radio("Start_Column",st.session_state.result)
    couple_coupler = cc2.text_input("Coupler","-")
    couple_end_column = cc3.radio("End_Column",st.session_state.result)
    
    
    new_col_name = cc4.text_input("새로운 이름을 입력하세요")
    if cc4.button("합체"):
        new_col_li = []
        for i in range(RAWS):
            new_col_li.append(f"{st.session_state.result[couple_start_column][i]}{couple_coupler}{st.session_state.result[couple_end_column][i]}")
        st.session_state.result[new_col_name] = new_col_li
        st.experimental_rerun()

    st.markdown("---")
    col11,col12 =st.columns(2)
    FILE_NAME = col11.text_input("File name")
    if FILE_NAME:
        try:
            df = fill_df(st.session_state.result)
            col12.download_button("Download CSV",df.to_csv(index=False),file_name=f"{FILE_NAME}.csv")
        except:
            st.warning("Please Make Columns First")
