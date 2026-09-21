from __future__ import annotations

import base64
from pathlib import Path
from textwrap import dedent

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
ASSETS = BASE_DIR / "assets"

st.set_page_config(
    page_title="Abraham Gizaw General Construction | AGGC",
    page_icon=str(ASSETS / "favicon.png"),
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------------------------
# COMPANY CONFIGURATION
# Add the verified details below before publishing. Leave blank to hide a field.
# -----------------------------------------------------------------------------
COMPANY = {
    "name": "ABRAHAM GIZAW GENERAL CONSTRUCTION",
    "short_name": "AGGC",
    "email": "",          # e.g. info@example.com
    "phone": "",          # e.g. +251 ...
    "whatsapp": "",       # international digits only, e.g. 2519XXXXXXXX
    "address": "",        # verified business address
    "facebook": "",
    "linkedin": "",
}

LANGS = {
    "English": "en",
    "አማርኛ": "am",
    "Afaan Oromoo": "om",
}

T = {
    "en": {
        "brand": "ABRAHAM GIZAW",
        "brand2": "GENERAL CONSTRUCTION",
        "tagline": "Quality Construction for a Better Tomorrow",
        "nav_about": "About",
        "nav_services": "Services",
        "nav_values": "Why AGGC",
        "nav_process": "How We Work",
        "nav_contact": "Contact",
        "hero_kicker": "Integrated construction & infrastructure services",
        "hero_title": "Building infrastructure that connects communities and supports growth.",
        "hero_text": "AGGC provides road, bridge, irrigation, WASH, electrical installation and building construction services with a focus on quality workmanship, safe delivery and practical engineering solutions.",
        "hero_cta": "Explore our services",
        "hero_cta2": "Request a quotation",
        "trust": ["Quality workmanship", "On-time delivery", "Safety first", "Sustainable infrastructure"],
        "about_kicker": "About AGGC",
        "about_title": "One construction partner across civil, water, electrical and building works.",
        "about_text": "Abraham Gizaw General Construction is a multidisciplinary construction company serving infrastructure and building needs across the project lifecycle. Our capabilities combine civil works, water and sanitation infrastructure, electrical installation and building construction under one delivery team.",
        "about_note": "Capability imagery is illustrative. Replace it with verified project photography as the company portfolio grows.",
        "services_kicker": "Our capabilities",
        "services_title": "Construction services built around essential infrastructure.",
        "services_intro": "From access roads and bridges to water systems, irrigation, electrical works and buildings, AGGC is positioned to support integrated construction packages.",
        "services": [
            {"title": "Road Construction", "image": "road.webp", "desc": "Road works for access, mobility and durable transport infrastructure.", "bullets": ["Gravel roads", "Concrete roads", "Asphalt pavement roads"]},
            {"title": "Bridge & Culvert Construction", "image": "bridge.webp", "desc": "Structural crossing solutions designed for safe and reliable movement.", "bullets": ["Steel-structure bridges", "Reinforced-concrete bridges", "Culverts and drainage crossings"]},
            {"title": "Irrigation Structures & Canals", "image": "irrigation.webp", "desc": "Water conveyance and irrigation infrastructure for productive landscapes.", "bullets": ["Irrigation structures", "Canal construction", "Associated water-control structures"]},
            {"title": "WASH & Water Supply Works", "image": "wash.webp", "desc": "Water, sanitation and utility works for communities, buildings and institutions.", "bullets": ["Water supply systems", "Reservoirs and pump houses", "Groundwater development", "Stream / surface-water development", "Sewerage lines", "Public tap-water facilities", "Building water supply and sanitary works"]},
            {"title": "Electrical Installation Works", "image": "electrical.webp", "desc": "Electrical installation services integrated with industrial and building projects.", "bullets": ["Factories", "Buildings", "Organizations and institutions"]},
            {"title": "Building Construction", "image": "building.webp", "desc": "Building delivery for commercial, residential and logistics requirements.", "bullets": ["Mixed-use complexes", "Residential buildings", "Warehouse construction"]},
        ],
        "values_kicker": "Why work with AGGC",
        "values_title": "A delivery approach centred on quality, safety and accountability.",
        "values": [
            ("01", "Quality workmanship", "Careful execution, appropriate materials and attention to durable construction details."),
            ("02", "Safety first", "A site culture that puts people, safe working practices and responsible delivery at the centre."),
            ("03", "On-time delivery", "Planning, coordination and practical sequencing to keep work progressing toward agreed milestones."),
            ("04", "Integrated capability", "Civil, water, electrical and building works can be coordinated through one construction partner."),
        ],
        "process_kicker": "How we work",
        "process_title": "A clear path from project brief to handover.",
        "process": [
            ("01", "Understand the requirement", "Review the brief, site conditions, scope, priorities and expected outputs."),
            ("02", "Plan the work", "Develop the construction approach, resources, schedule, safety controls and delivery sequence."),
            ("03", "Build & manage", "Coordinate site activities, quality checks, materials, workforce and progress reporting."),
            ("04", "Complete & hand over", "Close outstanding works, verify completion and prepare the project for handover."),
        ],
        "contact_kicker": "Start a conversation",
        "contact_title": "Tell us what you need to build.",
        "contact_text": "Share the project type, location and a short description. The form creates a clean quotation request you can send to AGGC once the verified contact details are added to this website.",
        "form_name": "Your name",
        "form_org": "Company / organization",
        "form_email": "Email",
        "form_phone": "Phone",
        "form_service": "Service required",
        "form_location": "Project location",
        "form_message": "Project description",
        "form_submit": "Prepare quotation request",
        "form_success": "Your quotation request is ready.",
        "form_download": "Download enquiry",
        "contact_pending": "Verified phone, email and address have not yet been added. Update the COMPANY section at the top of app.py before public launch.",
        "footer": "Building infrastructure for sustainable development.",
        "language": "Language",
        "service_select": "Select a service",
    },
    "am": {
        "brand": "አብርሃም ግዛው",
        "brand2": "ጠቅላላ ኮንስትራክሽን",
        "tagline": "ጥራት ያለው ግንባታ ለተሻለ ነገ",
        "nav_about": "ስለ እኛ",
        "nav_services": "አገልግሎቶች",
        "nav_values": "ለምን AGGC",
        "nav_process": "የስራ ሂደት",
        "nav_contact": "እውቂያ",
        "hero_kicker": "የተቀናጀ የግንባታና መሠረተ ልማት አገልግሎት",
        "hero_title": "ማህበረሰቦችን የሚያገናኝ እና እድገትን የሚደግፍ መሠረተ ልማት እንገነባለን።",
        "hero_text": "AGGC የመንገድ፣ ድልድይ፣ መስኖ፣ WASH፣ ኤሌክትሪክ መጫኛ እና የህንፃ ግንባታ አገልግሎቶችን በጥራት፣ በደህንነት እና በተግባራዊ የኢንጂነሪንግ መፍትሄ ላይ በማተኮር ይሰጣል።",
        "hero_cta": "አገልግሎቶቻችንን ይመልከቱ",
        "hero_cta2": "ዋጋ ይጠይቁ",
        "trust": ["ጥራት ያለው ስራ", "በጊዜ ማስረከብ", "ደህንነት ቅድሚያ", "ዘላቂ መሠረተ ልማት"],
        "about_kicker": "ስለ AGGC",
        "about_title": "ለሲቪል፣ ውሃ፣ ኤሌክትሪክ እና ህንፃ ስራዎች አንድ የግንባታ አጋር።",
        "about_text": "አብርሃም ግዛው ጠቅላላ ኮንስትራክሽን ለመሠረተ ልማትና ለህንፃ ፕሮጀክቶች ብዙ ዘርፎችን የሚያጣምር የግንባታ ድርጅት ነው። የሲቪል ስራ፣ የውሃና ሳኒቴሽን መሠረተ ልማት፣ የኤሌክትሪክ መጫኛ እና የህንፃ ግንባታን በአንድ የአፈፃፀም ቡድን ያቀናጃል።",
        "about_note": "ምስሎቹ የአገልግሎት ማብራሪያ ለማሳየት ናቸው። ከመጨረሻ ህትመት በፊት በተረጋገጡ የፕሮጀክት ፎቶዎች መተካት ይመከራል።",
        "services_kicker": "የስራ አቅማችን",
        "services_title": "አስፈላጊ መሠረተ ልማትን የሚያገለግሉ የግንባታ አገልግሎቶች።",
        "services_intro": "ከመንገድና ድልድይ እስከ ውሃ ስርዓት፣ መስኖ፣ ኤሌክትሪክ እና ህንፃ ድረስ AGGC የተቀናጀ የግንባታ ፓኬጅ ለማቅረብ የተዘጋጀ ነው።",
        "services": [
            {"title": "የመንገድ ግንባታ", "image": "road.webp", "desc": "ለተደራሽነት፣ ለመጓጓዣ እና ለዘላቂ የትራንስፖርት መሠረተ ልማት የመንገድ ስራዎች።", "bullets": ["የጠጠር መንገድ", "የኮንክሪት መንገድ", "የአስፋልት መንገድ"]},
            {"title": "የድልድይና ካልቨርት ግንባታ", "image": "bridge.webp", "desc": "ለአስተማማኝና ደህንነቱ የተጠበቀ መሻገሪያ መዋቅሮች።", "bullets": ["የብረት መዋቅር ድልድዮች", "የተጠናከረ ኮንክሪት ድልድዮች", "ካልቨርቶችና የፍሳሽ መሻገሪያዎች"]},
            {"title": "የመስኖ መዋቅሮችና ቦዮች", "image": "irrigation.webp", "desc": "ለመስኖ እና ለውሃ ማጓጓዣ የሚያገለግሉ መሠረተ ልማቶች።", "bullets": ["የመስኖ መዋቅሮች", "የቦይ ግንባታ", "ተያያዥ የውሃ መቆጣጠሪያ መዋቅሮች"]},
            {"title": "WASH እና የውሃ አቅርቦት ስራዎች", "image": "wash.webp", "desc": "ለማህበረሰብ፣ ህንፃ እና ተቋማት የውሃና ሳኒቴሽን መሠረተ ልማት።", "bullets": ["የውሃ አቅርቦት ስርዓቶች", "የውሃ ማጠራቀሚያና ፓምፕ ቤት", "የከርሰ ምድር ውሃ ልማት", "የወንዝ / የገጽታ ውሃ ልማት", "የፍሳሽ መስመሮች", "የህዝብ የውሃ ቧንቧ ተቋማት", "የህንፃ ውሃ አቅርቦትና ሳኒቴሽን ስራዎች"]},
            {"title": "የኤሌክትሪክ መጫኛ ስራዎች", "image": "electrical.webp", "desc": "ከኢንዱስትሪና ከህንፃ ፕሮጀክቶች ጋር የተቀናጀ የኤሌክትሪክ መጫኛ።", "bullets": ["ለፋብሪካዎች", "ለህንፃዎች", "ለድርጅቶችና ተቋማት"]},
            {"title": "የህንፃ ግንባታ", "image": "building.webp", "desc": "ለንግድ፣ ለመኖሪያና ለሎጂስቲክስ ፍላጎቶች የህንፃ ግንባታ።", "bullets": ["የተቀላቀለ አገልግሎት ህንፃዎች", "የመኖሪያ ህንፃዎች", "የመጋዘን ግንባታ"]},
        ],
        "values_kicker": "ለምን AGGC",
        "values_title": "በጥራት፣ በደህንነትና በተጠያቂነት ላይ የተመሠረተ የአፈፃፀም አቀራረብ።",
        "values": [("01", "ጥራት ያለው ስራ", "ጥንቃቄ ያለው አፈፃፀም፣ ተስማሚ ቁሳቁስና ዘላቂ የግንባታ ዝርዝሮች።"), ("02", "ደህንነት ቅድሚያ", "ሰዎችን፣ የስራ ደህንነትንና ኃላፊነት ያለው አፈፃፀምን ቅድሚያ የሚሰጥ የሳይት ባህል።"), ("03", "በጊዜ ማስረከብ", "የስራ እቅድ፣ ቅንጅትና ተግባራዊ የስራ ቅደም ተከተል።"), ("04", "የተቀናጀ አቅም", "የሲቪል፣ ውሃ፣ ኤሌክትሪክና ህንፃ ስራዎችን በአንድ አጋር ማቀናጀት።")],
        "process_kicker": "የስራ ሂደታችን",
        "process_title": "ከፕሮጀክት ጥያቄ እስከ ርክክብ ድረስ ግልጽ ሂደት።",
        "process": [("01", "ፍላጎቱን መረዳት", "የስራ ወሰን፣ የሳይት ሁኔታ፣ ቅድሚያዎችና የሚጠበቁ ውጤቶችን መመርመር።"), ("02", "ስራውን ማቀድ", "የግንባታ ዘዴ፣ ሀብት፣ የጊዜ ሰሌዳ፣ የደህንነት ቁጥጥርና ቅደም ተከተል ማዘጋጀት።"), ("03", "መገንባትና ማስተዳደር", "የሳይት ስራ፣ የጥራት ቁጥጥር፣ ቁሳቁስ፣ የሰው ኃይልና የሂደት ሪፖርት ማቀናጀት።"), ("04", "ማጠናቀቅና ማስረከብ", "ቀሪ ስራዎችን መዝጋት፣ ማጠናቀቂያ ማረጋገጥና ለርክክብ ማዘጋጀት።")],
        "contact_kicker": "ውይይት ይጀምሩ",
        "contact_title": "ምን መገንባት እንደሚፈልጉ ይንገሩን።",
        "contact_text": "የፕሮጀክቱን ዓይነት፣ ቦታና አጭር መግለጫ ያጋሩ። የተረጋገጠ የAGGC እውቂያ ከተጨመረ በኋላ ይህ ቅጽ የተደራጀ የዋጋ ጥያቄ ያዘጋጃል።",
        "form_name": "ስም",
        "form_org": "ድርጅት / ተቋም",
        "form_email": "ኢሜይል",
        "form_phone": "ስልክ",
        "form_service": "የሚፈለገው አገልግሎት",
        "form_location": "የፕሮጀክት ቦታ",
        "form_message": "የፕሮጀክት መግለጫ",
        "form_submit": "የዋጋ ጥያቄ አዘጋጅ",
        "form_success": "የዋጋ ጥያቄዎ ተዘጋጅቷል።",
        "form_download": "ጥያቄውን ያውርዱ",
        "contact_pending": "የተረጋገጠ ስልክ፣ ኢሜይልና አድራሻ ገና አልተጨመረም። ከህትመት በፊት በapp.py መጀመሪያ ያለውን COMPANY ክፍል ያዘምኑ።",
        "footer": "ለዘላቂ ልማት መሠረተ ልማት እንገነባለን።",
        "language": "ቋንቋ",
        "service_select": "አገልግሎት ይምረጡ",
    },
    "om": {
        "brand": "ABRAHAM GIZAW",
        "brand2": "GENERAL CONSTRUCTION",
        "tagline": "Ijaarsa Qulqullina Qabu Boruu Fooyya'aaf",
        "nav_about": "Waa'ee Keenya",
        "nav_services": "Tajaajiloota",
        "nav_values": "Maaliif AGGC",
        "nav_process": "Akkaataa Hojii",
        "nav_contact": "Nu Quunnamaa",
        "hero_kicker": "Tajaajila ijaarsaa fi bu'uuraalee misoomaa walitti makame",
        "hero_title": "Bu'uuraalee misoomaa hawaasa wal qunnamsiisanii guddina deeggaran ni ijaarra.",
        "hero_text": "AGGC tajaajila ijaarsa daandii, riqichaa, jallisii, WASH, dhaabbii elektirikii fi gamoo qulqullina hojii, nageenya fi furmaata injinariingii irratti xiyyeeffachuun ni kenna.",
        "hero_cta": "Tajaajila keenya ilaalaa",
        "hero_cta2": "Gatii gaafadhaa",
        "trust": ["Hojii qulqullinaa", "Yeroo irratti xumuru", "Nageenya dursa", "Bu'uura misoomaa waaraa"],
        "about_kicker": "Waa'ee AGGC",
        "about_title": "Hojii sivilii, bishaanii, elektirikii fi gamoo keessatti michuu ijaarsaa tokko.",
        "about_text": "Abraham Gizaw General Construction dhaabbata ijaarsaa damee hedduu walitti fiduun fedhii bu'uuraalee misoomaa fi gamoo tajaajiluudha. Dandeettiin keenya hojii sivilii, bu'uura bishaanii fi saniteeshinii, dhaabbii elektirikii fi ijaarsa gamoo garee raawwii tokko jalatti walitti qindeessa.",
        "about_note": "Suuraaleen kun dandeettii tajaajilaa ibsuuf kan fayyadamanidha. Maxxansa dhumaa dura suuraalee pirojektii mirkanaa'aniin bakka buusuun gaariidha.",
        "services_kicker": "Dandeettii keenya",
        "services_title": "Tajaajiloota ijaarsaa bu'uuraalee misoomaa barbaachisoo irratti hundaa'an.",
        "services_intro": "Daandii fi riqicha irraa kaasee hanga sirna bishaanii, jallisii, elektirikii fi gamootti AGGC hojii ijaarsaa walitti makame deeggaruuf qophaa'eera.",
        "services": [
            {"title": "Ijaarsa Daandii", "image": "road.webp", "desc": "Daandii dhaqqabummaa, sochii fi bu'uura geejjibaa waaraa deeggaru.", "bullets": ["Daandii cirrachaa", "Daandii konkiriitii", "Daandii asfaaltii"]},
            {"title": "Ijaarsa Riqichaa fi Kalvartii", "image": "bridge.webp", "desc": "Furmaata ce'umsa caasaa nageenya qabu fi amanamaa.", "bullets": ["Riqicha caasaa sibiilaa", "Riqicha konkiriitii cimsame", "Kalvartii fi ce'umsa bishaanii"]},
            {"title": "Caasaalee Jallisii fi Bo'oo", "image": "irrigation.webp", "desc": "Bu'uuraalee bishaan geessuu fi jallisii oomisha qonnaa deeggaran.", "bullets": ["Caasaalee jallisii", "Ijaarsa bo'oo jallisii", "Caasaalee to'annoo bishaanii walqabatan"]},
            {"title": "Hojii WASH fi Dhiyeessii Bishaanii", "image": "wash.webp", "desc": "Hojii bishaanii fi saniteeshinii hawaasa, gamoo fi dhaabbileef.", "bullets": ["Sirna dhiyeessii bishaanii", "Kuusaa bishaanii fi mana paampii", "Misooma bishaan lafa jalaa", "Misooma bishaan laga / irra keessaa", "Sarara dhangala'aa", "Bakka tajaajila tuuboo bishaan uummataa", "Dhiyeessii bishaanii fi hojii saniteeshinii gamoo"]},
            {"title": "Hojii Dhaabbii Elektirikii", "image": "electrical.webp", "desc": "Dhaabbii elektirikii pirojektoota industirii fi gamoo waliin walitti makame.", "bullets": ["Warshaalee", "Gamoota", "Dhaabbilee fi institushinoota"]},
            {"title": "Ijaarsa Gamoo", "image": "building.webp", "desc": "Ijaarsa gamoo daldalaa, jireenyaa fi kuusaa/logistics tajaajilu.", "bullets": ["Gamoo tajaajila walmakaa", "Gamoo jireenyaa", "Ijaarsa mana kuusaa"]},
        ],
        "values_kicker": "Maaliif AGGC",
        "values_title": "Akkaataa raawwii qulqullina, nageenya fi itti gaafatamummaa irratti hundaa'e.",
        "values": [("01", "Hojii qulqullinaa", "Raawwii of-eeggannoo qabu, meeshaalee sirrii fi bal'ina ijaarsaa waaraa irratti xiyyeeffachuu."), ("02", "Nageenya dursa", "Aadaa bakka hojii namoota, hojii nageenya qabuu fi raawwii itti gaafatamummaa dursa kennu."), ("03", "Yeroo irratti xumuru", "Karoora, qindoomina fi tartiiba hojii qabatamaa fayyadamuun milkaa'ina yeroon deeggaru."), ("04", "Dandeettii walitti makame", "Hojii sivilii, bishaanii, elektirikii fi gamoo michuu ijaarsaa tokkoon qindeessuu.")],
        "process_kicker": "Akkaataa hojii keenya",
        "process_title": "Gaaffii pirojektii irraa hanga dabarsuutti adeemsa ifaa.",
        "process": [("01", "Fedhii hubachuu", "Daangaa hojii, haala bakka, dursa fi bu'aa eegamu qorachuu."), ("02", "Hojii karoorsuu", "Mala ijaarsaa, qabeenya, sagantaa, to'annoo nageenyaa fi tartiiba raawwii qopheessuu."), ("03", "Ijaaruu fi bulchuu", "Hojii bakka, to'annoo qulqullinaa, meeshaalee, humna namaa fi gabaasa adeemsaa qindeessuu."), ("04", "Xumuruu fi dabarsuu", "Hojii hafan cufuu, xumura mirkaneessuu fi pirojektii dabarsuuf qopheessuu.")],
        "contact_kicker": "Mariin haa jalqabu",
        "contact_title": "Maal ijaaruu akka barbaaddan nutti himaa.",
        "contact_text": "Gosa pirojektii, bakka fi ibsa gabaabaa qoodaa. Erga odeeffannoon quunnamtii AGGC mirkanaa'e website irratti dabalamee booda, unki kun gaaffii gatii sirriitti qindaa'e qopheessa.",
        "form_name": "Maqaa keessan",
        "form_org": "Dhaabbata / organizashinii",
        "form_email": "Imeelii",
        "form_phone": "Bilbila",
        "form_service": "Tajaajila barbaachisu",
        "form_location": "Bakka pirojektii",
        "form_message": "Ibsa pirojektii",
        "form_submit": "Gaaffii gatii qopheessi",
        "form_success": "Gaaffiin gatii keessan qophaa'eera.",
        "form_download": "Gaaffii buufadhaa",
        "contact_pending": "Bilbilli, imeeliin fi teessoon mirkanaa'e amma hin dabalamin. Maxxansa uummataa dura kutaa COMPANY jalqaba app.py irratti jiru haaromsaa.",
        "footer": "Bu'uuraalee misoomaa waaraa ni ijaarra.",
        "language": "Afaan",
        "service_select": "Tajaajila filadhaa",
    },
}


def img_data_uri(filename: str) -> str:
    path = ASSETS / filename
    mime = "image/webp" if path.suffix.lower() == ".webp" else "image/png"
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


HERO_URI = img_data_uri("road.webp")
LOGO_URI = img_data_uri("header-logo.webp")

# Design system
st.markdown(
    f"""
<style>
:root {{
  --navy:#082b5c; --navy2:#04142d; --blue:#0d4f9f; --gold:#f4b31a;
  --gold2:#d99900; --ink:#10233d; --muted:#617087; --line:#dfe7f1;
  --soft:#f5f8fc; --white:#ffffff;
}}
html {{ scroll-behavior:smooth; }}
body, [data-testid="stAppViewContainer"] {{ background:#fff; color:var(--ink); }}
[data-testid="stHeader"] {{ background:rgba(255,255,255,.88); backdrop-filter:blur(12px); }}
[data-testid="stToolbar"], #MainMenu, footer {{ visibility:hidden; }}
.block-container {{ max-width:1380px; padding-top:0.8rem; padding-bottom:0; }}
[data-testid="stSidebar"] {{ display:none; }}

.aggc-top {{ display:flex; align-items:center; min-height:132px; padding:8px 0 12px; overflow:visible; }}
.aggc-logo-full {{ display:block; width:min(100%, 520px); max-width:520px; height:auto; object-fit:contain; object-position:left center; overflow:visible; filter:drop-shadow(0 8px 18px rgba(8,43,92,.10)); }}
.aggc-nav-shell {{ width:100%; background:#f8fbff; border:1px solid #e4ebf4; border-radius:16px; padding:10px 16px; margin:4px 0 14px; box-shadow:0 8px 22px rgba(15,23,42,.035); }}
.aggc-nav {{ display:flex; justify-content:center; align-items:center; gap:34px; flex-wrap:wrap; min-height:42px; }}
.aggc-nav a {{ color:#18314f !important; text-decoration:none !important; font-weight:850; font-size:1rem; letter-spacing:.01em; padding:8px 2px; }}
.aggc-nav a:hover {{ color:var(--blue) !important; }}
.lang-shell {{ width:100%; max-width:250px; margin-left:auto; padding-top:8px; }}
.lang-label {{ color:var(--navy); font-size:.86rem; font-weight:850; margin:0 0 .35rem 0.2rem; }}
div[data-baseweb="select"] > div {{ min-height:52px; border-radius:14px !important; border:1px solid #d6dfeb !important; box-shadow:0 6px 18px rgba(15,23,42,.05); background:#fff !important; }}
div[data-baseweb="select"] span {{ color:var(--navy) !important; font-weight:700; font-size:1rem; }}

.hero {{ position:relative; min-height:610px; border-radius:30px; overflow:hidden; margin:16px 0 26px; display:flex; align-items:center; background-image:linear-gradient(90deg, rgba(2,18,45,.95) 0%, rgba(6,35,81,.88) 46%, rgba(8,43,92,.30) 100%), url('{HERO_URI}'); background-size:cover; background-position:center; box-shadow:0 28px 70px rgba(8,43,92,.18); }}
.hero-inner {{ width:min(860px, 94%); padding:64px 64px 70px; color:#fff; }}
.motion-title-wrap {{ width:100%; max-width:780px; overflow:hidden; margin:0 0 22px; padding:9px 0; border-top:1px solid rgba(255,255,255,.16); border-bottom:1px solid rgba(255,255,255,.16); }}
.motion-title {{ display:inline-block; white-space:nowrap; max-width:100%; color:#ffd96d; font-size:.88rem; font-weight:900; letter-spacing:.13em; text-transform:uppercase; background:linear-gradient(90deg,#ffd15d 0%,#ffffff 35%,#ffd15d 70%,#ffffff 100%); background-size:220% auto; -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; animation:aggcShimmer 7s linear infinite, aggcDrift 8s ease-in-out infinite; will-change:transform,background-position; }}
@keyframes aggcShimmer {{ 0% {{ background-position:0% 50%; }} 100% {{ background-position:220% 50%; }} }}
@keyframes aggcDrift {{ 0%,100% {{ transform:translateX(0); }} 50% {{ transform:translateX(18px); }} }}
.kicker {{ display:inline-flex; align-items:center; color:#ffd15d; text-transform:uppercase; letter-spacing:.16em; font-weight:900; font-size:.8rem; }}
.hero h1 {{ color:#fff; font-size:clamp(2.75rem,4.1vw,4.3rem); line-height:1.02; letter-spacing:-.045em; margin:18px 0 22px; text-wrap:balance; max-width:820px; text-shadow:0 4px 20px rgba(0,0,0,.22); }}
.hero p {{ color:#f4f8ff; font-size:1.14rem; line-height:1.78; max-width:730px; font-weight:520; }}
.hero-actions {{ display:flex; gap:14px; flex-wrap:wrap; margin-top:30px; }}
.hero-btn {{ display:inline-flex; align-items:center; min-height:54px; padding:0 24px; border-radius:14px; text-decoration:none !important; font-weight:850; font-size:1rem; }}
.hero-btn.primary {{ background:var(--gold); color:#10233d !important; box-shadow:0 12px 28px rgba(244,179,26,.22); }}
.hero-btn.secondary {{ color:#fff !important; border:1px solid rgba(255,255,255,.3); background:rgba(255,255,255,.10); }}

.trust-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin:20px 0 82px; }}
.trust-card {{ border:1px solid var(--line); border-radius:16px; padding:20px; text-align:center; font-weight:850; color:var(--navy); background:#fff; box-shadow:0 8px 22px rgba(15,23,42,.035); font-size:1.02rem; }}
.trust-dot {{ color:var(--gold2); margin-right:7px; }}

.section-anchor {{ scroll-margin-top:92px; }}
.section-kicker {{ color:var(--gold2); text-transform:uppercase; letter-spacing:.15em; font-weight:900; font-size:.79rem; }}
.section-title {{ color:var(--navy); font-size:clamp(2.35rem,4vw,4.15rem); line-height:1.05; letter-spacing:-.04em; margin:.55rem 0 1rem; }}
.section-text {{ color:var(--muted); font-size:1.1rem; line-height:1.84; max-width:820px; }}
.section-space {{ height:86px; }}
.about-card {{ border:1px solid var(--line); border-radius:24px; padding:32px; background:linear-gradient(145deg,#fff,#f6f9fd); box-shadow:0 16px 38px rgba(15,23,42,.05); }}
.note {{ margin-top:20px; border-left:4px solid var(--gold); background:#fff8e8; color:#6e5719; padding:15px 17px; border-radius:10px; font-size:.95rem; line-height:1.65; }}

[data-testid="stImage"] img {{ border-radius:20px; }}
.service-title {{ color:var(--navy); font-size:1.52rem; font-weight:900; margin:.95rem 0 .5rem; }}
.service-desc {{ color:var(--muted); min-height:58px; line-height:1.75; font-size:1.03rem; }}
.service-list {{ color:#3f5065; line-height:1.85; padding-left:1.15rem; margin-top:.7rem; font-size:1.01rem; }}
.service-list li::marker {{ color:var(--gold2); }}
.service-wrap {{ border:1px solid var(--line); border-radius:22px; padding:14px 14px 22px; background:#fff; box-shadow:0 12px 30px rgba(15,23,42,.045); min-height:100%; }}

.dark-box {{ background:linear-gradient(135deg,#04142d,#082b5c 62%,#0d4f9f); border-radius:28px; padding:54px 46px; color:#fff; margin:20px 0 0; box-shadow:0 24px 60px rgba(8,43,92,.16); }}
.dark-box .section-title {{ color:#fff; max-width:900px; }}
.values-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:32px; }}
.value-card {{ border:1px solid rgba(255,255,255,.13); background:rgba(255,255,255,.06); border-radius:18px; padding:24px; min-height:235px; }}
.value-no {{ color:var(--gold); font-weight:900; font-size:.8rem; }}
.value-card h3 {{ margin:42px 0 10px; color:#fff; font-size:1.18rem; }}
.value-card p {{ color:rgba(255,255,255,.82); font-size:1rem; line-height:1.72; }}
.process-grid {{ display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-top:30px; }}
.process-card {{ border-top:4px solid var(--gold); border-radius:0 0 18px 18px; background:var(--soft); padding:24px; min-height:235px; }}
.process-card span {{ color:var(--gold2); font-weight:900; font-size:.8rem; }}
.process-card h3 {{ color:var(--navy); margin:38px 0 10px; font-size:1.16rem; }}
.process-card p {{ color:var(--muted); font-size:1rem; line-height:1.72; }}

.contact-panel {{ background:#eef4fa; border:1px solid #dde7f2; border-radius:26px; padding:38px; }}
.contact-list {{ display:grid; gap:9px; margin-top:24px; }}
.contact-item {{ background:#fff; border:1px solid var(--line); padding:13px 15px; border-radius:12px; }}
.contact-item small {{ color:var(--muted); display:block; font-size:.86rem; }}
.contact-item b, .contact-item a {{ color:var(--navy) !important; font-weight:850; text-decoration:none; font-size:1rem; }}
.pending {{ background:#fff8e6; border:1px solid #f1dfac; color:#6c5719; padding:15px; border-radius:12px; font-size:.95rem; line-height:1.65; }}

.stButton > button, .stDownloadButton > button {{ background:var(--navy); color:#fff; border:none; border-radius:12px; min-height:50px; font-weight:800; font-size:1rem; }}
.stButton > button:hover, .stDownloadButton > button:hover {{ background:var(--blue); color:#fff; border:none; }}
[data-baseweb="input"] > div, [data-baseweb="select"] > div, textarea {{ border-radius:11px !important; }}

.footer-panel {{ margin-top:90px; background:var(--navy2); color:rgba(255,255,255,.82); padding:36px 34px; border-radius:24px 24px 0 0; }}
.footer-panel strong {{ color:#fff; }}
.footer-panel .gold {{ color:var(--gold); font-weight:800; }}
.footer-small {{ font-size:.82rem; margin-top:8px; }}

@media (prefers-reduced-motion: reduce) {{
  .motion-title {{ animation:none; transform:none; background:none; -webkit-text-fill-color:#ffd96d; color:#ffd96d; }}
}}

@media (max-width: 1100px) {{
  .aggc-nav {{ gap:22px; }}
  .aggc-nav a {{ font-size:.96rem; }}
  .aggc-logo-full {{ max-width:460px; }}
}}
@media (max-width: 900px) {{
  .aggc-top {{ min-height:112px; }}
  .aggc-logo-full {{ max-width:390px; }}
  .aggc-nav-shell {{ padding:8px 10px; }}
  .aggc-nav {{ display:flex; gap:12px 20px; }}
  .aggc-nav a {{ font-size:.92rem; }}
  .hero {{ min-height:540px; }}
  .hero-inner {{ padding:54px 32px; width:100%; }}
  .hero h1 {{ font-size:clamp(2.7rem,7vw,4.1rem); }}
  .trust-grid, .values-grid, .process-grid {{ grid-template-columns:repeat(2,1fr); }}
  .dark-box {{ padding:40px 26px; }}
}}
@media (max-width: 620px) {{
  .block-container {{ padding-left:1rem; padding-right:1rem; }}
  .aggc-top {{ min-height:92px; padding:6px 0 8px; }}
  .aggc-logo-full {{ max-width:300px; }}
  .aggc-nav {{ justify-content:flex-start; gap:8px 16px; }}
  .aggc-nav a {{ font-size:.88rem; }}
  .hero {{ border-radius:22px; min-height:520px; background-position:62% center; }}
  .hero-inner {{ padding:42px 22px; }}
  .motion-title-wrap {{ max-width:100%; margin-bottom:18px; }}
  .motion-title {{ white-space:normal; font-size:.74rem; line-height:1.55; letter-spacing:.1em; animation:aggcShimmer 7s linear infinite; }}
  .hero h1 {{ font-size:2.5rem; line-height:1.05; }}
  .hero p {{ font-size:1.02rem; line-height:1.7; }}
  .trust-grid, .values-grid, .process-grid {{ grid-template-columns:1fr; }}
  .trust-grid {{ margin-bottom:56px; }}
  .section-space {{ height:62px; }}
  .contact-panel {{ padding:24px; }}
}}
</style>
""",
    unsafe_allow_html=True,
)

# Header: full professional logo + visible language + full-width navigation
h1, h2 = st.columns([5.2, 1.6], vertical_alignment="center")
with h1:
    st.markdown(
        f"""<div class="aggc-top"><img class="aggc-logo-full" src="{LOGO_URI}" alt="Abraham Gizaw General Construction – AGGC logo"></div>""",
        unsafe_allow_html=True,
    )
with h2:
    st.markdown('<div class="lang-shell"><div class="lang-label">Language / ቋንቋ / Afaan</div></div>', unsafe_allow_html=True)
    label = st.selectbox("Language", options=list(LANGS), label_visibility="collapsed", key="language")
lang = LANGS[label]
t = T[lang]

st.markdown(
    f"""<div class="aggc-nav-shell"><nav class="aggc-nav">
    <a href="#about">{t['nav_about']}</a>
    <a href="#services">{t['nav_services']}</a>
    <a href="#why">{t['nav_values']}</a>
    <a href="#process">{t['nav_process']}</a>
    <a href="#contact">{t['nav_contact']}</a>
    </nav></div>""",
    unsafe_allow_html=True,
)

# Hero
st.markdown(
    f"""
<section class="hero">
  <div class="hero-inner">
    <div class="motion-title-wrap"><span class="motion-title">{t['brand']} {t['brand2']} · {t['tagline']}</span></div>
    <div class="kicker">{t['hero_kicker']}</div>
    <h1>{t['hero_title']}</h1>
    <p>{t['hero_text']}</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="#services">{t['hero_cta']} →</a>
      <a class="hero-btn secondary" href="#contact">{t['hero_cta2']}</a>
    </div>
  </div>
</section>
<div class="trust-grid">
  {''.join(f'<div class="trust-card"><span class="trust-dot">◆</span>{x}</div>' for x in t['trust'])}
</div>
""",
    unsafe_allow_html=True,
)

# About
st.markdown('<div id="about" class="section-anchor"></div>', unsafe_allow_html=True)
a1, a2 = st.columns([1.05, 0.95], gap="large", vertical_alignment="center")
with a1:
    st.markdown(
        f"""<div class="section-kicker">{t['about_kicker']}</div><div class="section-title">{t['about_title']}</div><div class="section-text">{t['about_text']}</div>""",
        unsafe_allow_html=True,
    )
with a2:
    with st.container(border=True):
        st.image(str(ASSETS / "company-capabilities.webp"), use_container_width=True)
        st.markdown(f'<div class="note">{t["about_note"]}</div>', unsafe_allow_html=True)

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# Services
st.markdown('<div id="services" class="section-anchor"></div>', unsafe_allow_html=True)
st.markdown(
    f"""<div class="section-kicker">{t['services_kicker']}</div><div class="section-title">{t['services_title']}</div><div class="section-text">{t['services_intro']}</div>""",
    unsafe_allow_html=True,
)

services = t["services"]
for i in range(0, len(services), 2):
    cols = st.columns(2, gap="large")
    for col, service in zip(cols, services[i : i + 2]):
        with col:
            with st.container(border=True):
                st.image(str(ASSETS / service["image"]), use_container_width=True)
                bullets = "".join(f"<li>{b}</li>" for b in service["bullets"])
                st.markdown(
                    f"""<div class="service-title">{service['title']}</div><div class="service-desc">{service['desc']}</div><ul class="service-list">{bullets}</ul>""",
                    unsafe_allow_html=True,
                )
    st.write("")

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# Why AGGC
st.markdown('<div id="why" class="section-anchor"></div>', unsafe_allow_html=True)
values_html = "".join(
    f'<div class="value-card"><div class="value-no">{n}</div><h3>{title}</h3><p>{body}</p></div>'
    for n, title, body in t["values"]
)
st.markdown(
    f"""<section class="dark-box"><div class="section-kicker" style="color:var(--gold)">{t['values_kicker']}</div><div class="section-title">{t['values_title']}</div><div class="values-grid">{values_html}</div></section>""",
    unsafe_allow_html=True,
)

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# Process
st.markdown('<div id="process" class="section-anchor"></div>', unsafe_allow_html=True)
process_html = "".join(
    f'<div class="process-card"><span>{n}</span><h3>{title}</h3><p>{body}</p></div>'
    for n, title, body in t["process"]
)
st.markdown(
    f"""<div class="section-kicker">{t['process_kicker']}</div><div class="section-title">{t['process_title']}</div><div class="process-grid">{process_html}</div>""",
    unsafe_allow_html=True,
)

st.markdown('<div class="section-space"></div>', unsafe_allow_html=True)

# Contact + enquiry generator
st.markdown('<div id="contact" class="section-anchor"></div>', unsafe_allow_html=True)
c1, c2 = st.columns([0.86, 1.14], gap="large", vertical_alignment="top")
with c1:
    contact_parts = []
    if COMPANY["email"]:
        contact_parts.append(f'<div class="contact-item"><small>Email</small><a href="mailto:{COMPANY["email"]}">{COMPANY["email"]}</a></div>')
    if COMPANY["phone"]:
        contact_parts.append(f'<div class="contact-item"><small>Phone</small><a href="tel:{COMPANY["phone"]}">{COMPANY["phone"]}</a></div>')
    if COMPANY["address"]:
        contact_parts.append(f'<div class="contact-item"><small>Address</small><b>{COMPANY["address"]}</b></div>')
    if COMPANY["whatsapp"]:
        contact_parts.append(f'<div class="contact-item"><small>WhatsApp</small><a target="_blank" href="https://wa.me/{COMPANY["whatsapp"]}">Chat on WhatsApp</a></div>')
    contact_html = '<div class="contact-list">' + ''.join(contact_parts) + '</div>' if contact_parts else f'<div class="pending" style="margin-top:22px">{t["contact_pending"]}</div>'
    st.markdown(
        f"""<div class="contact-panel"><div class="section-kicker">{t['contact_kicker']}</div><div class="section-title" style="font-size:clamp(2rem,3vw,3.25rem)">{t['contact_title']}</div><div class="section-text">{t['contact_text']}</div>{contact_html}</div>""",
        unsafe_allow_html=True,
    )

with c2:
    service_labels = [s["title"] for s in services]
    with st.form("quote_form", clear_on_submit=False):
        f1, f2 = st.columns(2)
        with f1:
            name = st.text_input(t["form_name"])
            email = st.text_input(t["form_email"])
            service = st.selectbox(t["form_service"], [t["service_select"]] + service_labels)
        with f2:
            org = st.text_input(t["form_org"])
            phone = st.text_input(t["form_phone"])
            location = st.text_input(t["form_location"])
        message = st.text_area(t["form_message"], height=145)
        submitted = st.form_submit_button(t["form_submit"], use_container_width=True)

    if submitted:
        enquiry = dedent(
            f"""
            AGGC QUOTATION REQUEST
            ----------------------
            Name: {name or '-'}
            Company / Organization: {org or '-'}
            Email: {email or '-'}
            Phone: {phone or '-'}
            Service: {service if service != t['service_select'] else '-'}
            Project location: {location or '-'}

            Project description:
            {message or '-'}
            """
        ).strip()
        st.success(t["form_success"])
        st.code(enquiry, language=None)
        st.download_button(
            t["form_download"],
            data=enquiry.encode("utf-8"),
            file_name="AGGC_quotation_request.txt",
            mime="text/plain",
            use_container_width=True,
        )
        if COMPANY["email"]:
            subject = "AGGC quotation request"
            st.markdown(f'<a class="hero-btn primary" style="margin-top:8px" href="mailto:{COMPANY["email"]}?subject={subject}">Email AGGC</a>', unsafe_allow_html=True)

# Footer
st.markdown(
    f"""<div class="footer-panel"><strong>{t['brand']} <span class="gold">{t['brand2']}</span></strong><div class="footer-small">{t['tagline']} · {t['footer']}</div><div class="footer-small">© 2026 {COMPANY['name']}. All rights reserved.</div></div>""",
    unsafe_allow_html=True,
)
