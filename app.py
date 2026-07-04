import streamlit as st

st.set_page_config(
    page_title="Pooja Thakur — Graphic Designer",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# GLOBAL STYLE — single accent color (coral) on ink/paper neutrals only
# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Work+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500&display=swap');

:root{
    --ink:#1C1B1F;
    --paper:#FAF9F6;
    --coral:#E8465C;
    --gray:#6B6B6B;
    --line:#E4E1DA;
}

html, body, [class*="css"]{
    font-family:'Work Sans', sans-serif;
    color:var(--ink);
}

#MainMenu, header, footer {visibility:hidden;}
.block-container{ padding-top:1.2rem; padding-bottom:3rem; max-width:1000px;}
.stApp{ background:var(--paper); }

/* ---------- HERO ---------- */
.hero-wrap{
    position:relative;
    padding:3.2rem 3rem 3rem 3rem;
    background:var(--ink);
    border-radius:6px;
    overflow:hidden;
    margin-bottom:2rem;
}
.hero-wrap::before{
    content:"";
    position:absolute;
    top:-70px; right:-70px;
    width:240px; height:240px;
    border:2px solid var(--coral);
    border-radius:50%;
    opacity:0.55;
}
.eyebrow{
    font-family:'JetBrains Mono', monospace;
    letter-spacing:.18em;
    text-transform:uppercase;
    color:var(--coral);
    font-size:0.72rem;
    position:relative; z-index:2;
}
.hero-name{
    font-family:'Archivo Black', sans-serif;
    color:var(--paper);
    font-size:4.2rem;
    line-height:0.98;
    margin:.5rem 0 .3rem 0;
    position:relative; z-index:2;
    letter-spacing:-.01em;
}
.hero-role{
    font-family:'Archivo Black', sans-serif;
    color:var(--coral);
    font-size:1.4rem;
    margin-bottom:1.1rem;
    position:relative; z-index:2;
}
.hero-summary{
    color:#D8D5CE;
    font-size:1.02rem;
    line-height:1.65;
    max-width:560px;
    position:relative; z-index:2;
}
.hero-contact{
    margin-top:1.6rem;
    display:flex;
    flex-wrap:wrap;
    gap:1.1rem;
    position:relative; z-index:2;
}
.hero-contact a{
    color:var(--paper) !important;
    text-decoration:none;
    font-size:0.86rem;
    font-family:'JetBrains Mono', monospace;
    border-bottom:1px solid rgba(255,255,255,0.35);
    padding-bottom:2px;
}
.hero-contact a:hover{ border-color:var(--coral); color:var(--coral) !important; }

/* ---------- TABS ---------- */
.stTabs [data-baseweb="tab-list"]{
    gap:0;
    border-bottom:2px solid var(--line);
}
.stTabs [data-baseweb="tab"]{
    font-family:'Archivo Black', sans-serif;
    font-size:0.85rem;
    text-transform:uppercase;
    letter-spacing:.03em;
    color:var(--gray);
    padding:0.9rem 1.4rem;
}
.stTabs [aria-selected="true"]{
    color:var(--ink) !important;
    border-bottom:3px solid var(--coral) !important;
}
.tab-inner{ padding-top:1.8rem; }

.sec-note{ color:var(--gray); font-size:0.9rem; margin-bottom:1.3rem; }
.sec-note a{ color:var(--coral); font-weight:600; }

.mini-head{
    font-family:'Archivo Black', sans-serif;
    font-size:1.15rem;
    text-transform:uppercase;
    letter-spacing:-.01em;
    color:var(--ink) !important;
    border-bottom:2px solid var(--coral);
    display:inline-block;
    padding-bottom:.25rem;
    margin:1.8rem 0 1.1rem 0;
}
.mini-head:first-of-type{ margin-top:0; }

/* ---------- SKILL CARD ---------- */
.skill-card{
    background:#fff;
    border:1px solid var(--line);
    border-left:5px solid var(--coral);
    border-radius:4px;
    padding:1.1rem 1.3rem;
    margin-bottom:1rem;
}
.skill-top{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:.5rem;
}
.skill-name{
    font-family:'Archivo Black', sans-serif;
    font-size:1.05rem;
    color:var(--ink) !important;
}
.skill-level{
    font-family:'JetBrains Mono', monospace;
    font-size:0.68rem;
    letter-spacing:.05em;
    padding:.2rem .55rem;
    border-radius:20px;
    background:var(--ink);
    color:var(--paper) !important;
}
.skill-bar-track{
    width:100%; height:6px;
    background:var(--line);
    border-radius:4px;
    margin:.6rem 0 .8rem 0;
    overflow:hidden;
}
.skill-bar-fill{
    height:100%;
    background:var(--coral);
    border-radius:4px;
}
.skill-desc{
    font-size:0.84rem;
    color:var(--gray) !important;
    line-height:1.55;
}
.skill-desc b{ color:var(--ink) !important; }

/* ---------- PROJECT CARD ---------- */
.proj-card{
    background:#fff;
    border:1px solid var(--line);
    border-radius:6px;
    overflow:hidden;
    margin-bottom:1.6rem;
    transition:transform .15s ease, box-shadow .15s ease;
}
.proj-card:hover{
    transform:translateY(-3px);
    box-shadow:0 10px 24px rgba(0,0,0,0.08);
}
.proj-img-wrap{ width:100%; aspect-ratio:4/3; overflow:hidden; background:var(--line); }
.proj-img-wrap img{ width:100%; height:100%; object-fit:cover; display:block; }
.proj-body{ padding:1rem 1.15rem 1.2rem 1.15rem; }
.proj-title{ font-family:'Archivo Black', sans-serif; font-size:1.02rem; margin-bottom:.35rem; color:var(--ink) !important; }
.proj-tag{
    display:inline-block;
    font-family:'JetBrains Mono', monospace;
    font-size:0.68rem;
    background:#F1EFE9;
    color:var(--gray) !important;
    padding:.15rem .5rem;
    border-radius:4px;
    margin-bottom:.6rem;
}
.proj-link{
    font-size:0.82rem;
    font-weight:600;
    color:var(--coral) !important;
    text-decoration:none;
}
.proj-link:hover{ color:var(--ink) !important; }

/* ---------- TIMELINE / EDU / CERT ---------- */
.tl-item{
    border-left:2px solid var(--line);
    padding:.1rem 0 1.3rem 1.3rem;
    position:relative;
}
.tl-item::before{
    content:"";
    position:absolute;
    left:-6px; top:2px;
    width:10px; height:10px;
    background:var(--coral);
    border-radius:50%;
}
.tl-year{
    font-family:'JetBrains Mono', monospace;
    font-size:0.72rem;
    color:var(--coral) !important;
}
.tl-title{ font-family:'Archivo Black', sans-serif; font-size:1rem; margin:.15rem 0; color:var(--ink) !important; }
.tl-sub{ font-size:0.85rem; color:var(--gray) !important; }

/* ---------- STRENGTH PILLS ---------- */
.pill{
    display:inline-block;
    font-size:0.82rem;
    font-weight:600;
    padding:.45rem 1rem;
    margin:0 .5rem .5rem 0;
    border-radius:30px;
    border:1.5px solid var(--coral);
    color:var(--coral) !important;
    background:transparent;
}

/* ---------- FOOTER CTA ---------- */
.cta-wrap{
    background:var(--ink);
    border-radius:6px;
    padding:2.6rem 3rem;
    text-align:center;
    margin-top:1rem;
}
.cta-title{
    font-family:'Archivo Black', sans-serif;
    color:var(--paper) !important;
    font-size:2rem;
    margin-bottom:.6rem;
}
.cta-sub{ color:#D8D5CE !important; margin-bottom:1.4rem; }
.cta-btn{
    display:inline-block;
    background:var(--coral);
    color:#fff !important;
    font-weight:700;
    padding:.75rem 2rem;
    border-radius:30px;
    text-decoration:none;
    font-size:0.95rem;
}
.cta-btn:hover{ background:#fff; color:var(--ink) !important; }

@media (max-width:700px){
    .hero-name{ font-size:2.4rem; }
    .hero-wrap{ padding:2.2rem 1.5rem; }
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# HERO (always visible above the tabs)
# ----------------------------------------------------------------------------
st.markdown("""
<div class="hero-wrap">
    <div class="eyebrow">PORTFOLIO / 2026</div>
    <div class="hero-name">POOJA<br>THAKUR</div>
    <div class="hero-role">Graphic Designer</div>
    <div class="hero-summary">
        Creative graphic designer skilled in Adobe Photoshop, Illustrator, Figma, and Canva —
        passionate about branding, social media creatives, packaging design, and visual
        storytelling. Seeking to bring that eye for detail to a professional design team.
    </div>
    <div class="hero-contact">
        <a href="tel:7011873291">📞 7011873291</a>
        <a href="mailto:poojakhuswha7012@gmail.com">✉ poojakhuswha7012@gmail.com</a>
        <a href="https://www.behance.net/poojakhuswha" target="_blank">🎨 Behance</a>
        <a href="https://www.linkedin.com/in/pooja-thakur" target="_blank">in LinkedIn</a>
        <a href="#">📍 Noida, Sector 62</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# TABS (2 windows: Profile, Work)
# ----------------------------------------------------------------------------
tab_profile, tab_work = st.tabs(["Profile", "Selected Work"])

# ---------------- PROFILE TAB (skills + education + strengths) ----------------
with tab_profile:
    st.markdown('<div class="tab-inner">', unsafe_allow_html=True)

    st.markdown('<div class="mini-head">Skills & Tools</div>', unsafe_allow_html=True)

    skills = [
        {
            "name": "Adobe Photoshop", "level": "ADVANCED", "pct": 92,
            "desc": "<b>Core:</b> Photo editing, retouching, background removal, image manipulation, color correction, layer management, clipping masks, smart objects.<br><b>Output:</b> Typography design, mockup editing, print prep, export optimization."
        },
        {
            "name": "Adobe Illustrator", "level": "INTERMEDIATE", "pct": 72,
            "desc": "<b>Core:</b> Pen tool, shape builder, pathfinder, vector illustration, typography, color palette development.<br><b>Output:</b> Logo & brand identity, packaging, business cards, flyers/posters, icons, print-ready artwork."
        },
        {
            "name": "Figma", "level": "INTERMEDIATE", "pct": 70,
            "desc": "<b>Core:</b> Wireframing, auto layout, components, design systems, interactive prototypes, responsive basics.<br><b>Output:</b> Mobile app UI, website & landing page layouts, UI screens."
        },
        {
            "name": "Canva", "level": "ADVANCED", "pct": 90,
            "desc": "<b>Core:</b> Brand kit management, content creation, template customization.<br><b>Output:</b> Social posts & carousels, stories, posters, presentations, marketing creatives."
        },
    ]

    for s in skills:
        st.markdown(f"""
        <div class="skill-card">
            <div class="skill-top">
                <span class="skill-name">{s['name']}</span>
                <span class="skill-level">{s['level']}</span>
            </div>
            <div class="skill-bar-track"><div class="skill-bar-fill" style="width:{s['pct']}%;"></div></div>
            <div class="skill-desc">{s['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="mini-head">Education & Certifications</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tl-item">
        <div class="tl-year">2022 — 2025</div>
        <div class="tl-title">Bachelor of Arts (Honours)</div>
        <div class="tl-sub">Aryabhatta College, University of Delhi</div>
    </div>
    <div class="tl-item">
        <div class="tl-year">CERTIFICATION</div>
        <div class="tl-title">Graphic Design Certification</div>
        <div class="tl-sub">Ducat Institute, Noida</div>
    </div>
    <div class="tl-item">
        <div class="tl-year">CERTIFICATION</div>
        <div class="tl-title">UI/UX Design Certification</div>
        <div class="tl-sub">Ducat Institute, Noida</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="mini-head">Strengths</div>', unsafe_allow_html=True)
    strengths = ["Creative Thinking", "Visual Storytelling", "Attention to Detail", "Communication Skills",
                 "Problem Solving", "Time Management", "Adaptability"]
    st.markdown("".join([f'<span class="pill">{s}</span>' for s in strengths]), unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- WORK TAB (portfolio + contact) ----------------
with tab_work:
    st.markdown('<div class="tab-inner">', unsafe_allow_html=True)
    st.markdown("""
    <p class="sec-note">Pulled straight from
    <a href="https://www.behance.net/poojakhuswha" target="_blank">behance.net/poojakhuswha</a>
    — click any piece to view the full case study.</p>
    """, unsafe_allow_html=True)

    projects = [
        {
            "title": "Shre Jewelry — Brand Identity & Marketing Design",
            "tag": "BRANDING",
            "img": "https://mir-s3-cdn-cf.behance.net/projects/404/b63f7e250565427.Y3JvcCwxMTIzLDg3OCwwLDE4MjM.jpg",
            "link": "https://www.behance.net/gallery/250565427/Shre-Jewelry-Brand-Identity-Marketing-Design",
        },
        {
            "title": "NEXTIN Branding",
            "tag": "LOGO & IDENTITY",
            "img": "https://mir-s3-cdn-cf.behance.net/projects/404/4cc7df249880479.Y3JvcCw4MDgsNjMyLDcwLDA.png",
            "link": "https://www.behance.net/gallery/249880479/NEXTIN-Branding",
        },
        {
            "title": "Social Media Poster Design",
            "tag": "SOCIAL CREATIVE",
            "img": "https://mir-s3-cdn-cf.behance.net/projects/404/f6ea7a251748379.Y3JvcCwyMzYyLDE4NDcsMCw0MTU.png",
            "link": "https://www.behance.net/gallery/251748379/SOCIAL-MEDIA-POSTER-DESIGN",
        },
        {
            "title": "Poster Design",
            "tag": "PRINT",
            "img": "https://mir-s3-cdn-cf.behance.net/projects/404/72697a251131707.Y3JvcCwxMzA5LDEwMjQsMTEzLDA.png",
            "link": "https://www.behance.net/gallery/251131707/Poster-design",
        },
        {
            "title": "Corousal",
            "tag": "SOCIAL CREATIVE",
            "img": "https://mir-s3-cdn-cf.behance.net/projects/404/08f9d1251945673.Y3JvcCwyMzYyLDE4NDcsMCwyNTc.png",
            "link": "https://www.behance.net/gallery/251945673/corousal",
        },
    ]

    cols = st.columns(3)
    for i, p in enumerate(projects):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="proj-card">
                <div class="proj-img-wrap"><img src="{p['img']}" /></div>
                <div class="proj-body">
                    <span class="proj-tag">{p['tag']}</span>
                    <div class="proj-title">{p['title']}</div>
                    <a class="proj-link" href="{p['link']}" target="_blank">View case study →</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with cols[len(projects) % 3]:
        st.markdown("""
        <div class="proj-card">
            <div class="proj-img-wrap" style="display:flex;align-items:center;justify-content:center;background:var(--ink);">
                <span style="font-family:'Archivo Black',sans-serif; color:#fff; font-size:1.1rem; text-align:center; padding:1rem;">PACKAGING<br>DESIGN</span>
            </div>
            <div class="proj-body">
                <span class="proj-tag">PACKAGING</span>
                <div class="proj-title">Packaging Design Concept</div>
                <div style="font-size:0.82rem; color:var(--gray);">Product packaging mockups with label design and print-ready artwork, built in Illustrator.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="cta-wrap">
        <div class="cta-title">Let's design something great together.</div>
        <div class="cta-sub">Open to graphic design roles — branding, social media, and packaging.</div>
        <a class="cta-btn" href="mailto:poojakhuswha7012@gmail.com">poojakhuswha7012@gmail.com</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
